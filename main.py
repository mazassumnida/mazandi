from typing import Optional
from fastapi import FastAPI, Response
from httpx import AsyncClient

from utils import create_solved_dict, boj_rating_to_lv, get_starting_day, get_tomorrow
import mapping


app = FastAPI()

@app.get("/api")
async def generate_bedge(handle: str, theme: Optional[str] = "warm"):
    # api = os.environ['API_SERVER']
    api = 'https://solved.ac/api/v3/user'
    user_info_url = api + '/show?handle=' + handle
    timestamp_url = api + '/history?handle=' + handle + '&topic=solvedCount'
    solved_dict = {}
    solved_max = 0
    color_theme = mapping.COLOR_COLD if theme == "cold" else mapping.COLOR_WARM
    
    async with AsyncClient() as client:
        user_info = await client.get(user_info_url)
        timestamp = await client.get(timestamp_url)
        
    if user_info.status_code == 200 and timestamp.status_code == 200:
        user_info = user_info.json()
        timestamp = timestamp.json()
        solved_dict = create_solved_dict(timestamp)
        solved_max = solved_dict['solved_max']
    
    # TODO: 색 지정
    rating = user_info['rating']
    tier = mapping.TIERS[boj_rating_to_lv(rating)]
    tier_name = tier.split(' ')[0]
    
    # TODO: 잔디 그리기
    svg = """
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="350" height="170" viewBox="0 0 350 170">
        <style type="text/css">
            <![CDATA[
                @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=block');
                @keyframes fadeIn {{
                    0% {{ opacity: 0; }}
                    40% {{ opacity: 0; }}
                    100% {{ opacity: 1; }}
                }}
                .zandi {{
                    opacity: 0;
                    animation: fadeIn 0.5s ease-in-out forwards;
                }}
                #handle {{
                    opacity: 0;
                    animation: fadeIn 0.5s ease-in-out forwards;
                }}
                #tier {{
                    opacity: 0;
                    animation: fadeIn 0.5s ease-in-out forwards;
                }}
            ]]>
        </style>
        <defs>
            <clipPath id="clip-Gold_-_1">
            <rect width="350" height="170"/>
            </clipPath>
        </defs>
        <g id="Gold_-_1" data-name="Gold - 1" clip-path="url(#clip-Gold_-_1)">
            <rect id="rect_1" width="349" height="169" rx="14" fill="#fdfdfd" style="stroke-width:0.5; stroke:#bfbfbf;"/>
            <text id="handle" transform="translate(23 32)" fill="{color}" font-size="14" font-family="NotoSansKR-Black, Noto Sans KR" font-weight="800" style="animation-delay:100ms">{handle}</text>
            <text id="tier" data-name="tier" transform="translate(327 32)" fill="{color}" font-size="12" font-family="NotoSansKR-Black, Noto Sans KR" font-weight="800" text-anchor="end" style="animation-delay:300ms">{tier}</text>
    """.format(handle=handle, tier=tier, color=color_theme[tier_name][4])

    idx = 0
    today, now_in_loop = get_starting_day()
    # print(today, now_in_loop)
    while True:
        if not solved_dict.get(now_in_loop):
            color = color_theme[tier_name][0]
        elif (solved_dict[now_in_loop] / solved_max) > 0.667:
            color = color_theme[tier_name][3]
        elif (solved_dict[now_in_loop] / solved_max) > 0.334:
            color = color_theme[tier_name][2]
        else:
            color = color_theme[tier_name][1]
        
        nemo = '\n<rect class="zandi"\
                width="15" height="15" rx="4"\
                transform="translate({x} {y})" \
                fill="{color}"\
                style="animation-delay:{delay}ms"/>\
                '.format(x=23 + (idx // 7) * 17,
                         y=44 + (idx % 7) * 16,
                        color=color,
                        delay=500 + (idx % 7) * 50 + idx * 4)
        svg += nemo
        idx += 1
        # print(now_in_loop, today)
        if now_in_loop == today:
            break
        now_in_loop = get_tomorrow(now_in_loop)
    
    svg += """
        </g>
    </svg>
    """
    
    response = Response(content=svg, media_type='image/svg+xml')
    response.headers['Cache-Control'] = 'no-cache'
    
    return response
