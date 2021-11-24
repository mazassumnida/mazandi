from typing import Optional
from fastapi import FastAPI, Response
from httpx import AsyncClient

from utils import create_solved_dict, boj_rating_to_lv, get_starting_day, get_tomorrow
import mapping


app = FastAPI()

@app.get("/api/{handle}")
async def generate_bedge(handle: str):
    # api = os.environ['API_SERVER']
    api = 'https://solved.ac/api/v3/user'
    user_info_url = api + '/show?handle=' + handle
    timestamp_url = api + '/history?handle=' + handle + '&topic=solvedCount'
    solved_dict = {}
    
    async with AsyncClient() as client:
        user_info = await client.get(user_info_url)
        timestamp = await client.get(timestamp_url)
        
    if user_info.status_code == 200 and timestamp.status_code == 200:
        user_info = user_info.json()
        timestamp = timestamp.json()
        solved_dict = create_solved_dict(timestamp)
    
    # TODO: 색 지정
    rating = user_info['rating']
    tier = mapping.TIERS[boj_rating_to_lv(rating)]
    
    # TODO: 잔디 그리기
    svg = """
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="350" height="170" viewBox="0 0 350 170">
        <defs>
            <clipPath id="clip-Gold_-_1">
            <rect width="350" height="170"/>
            </clipPath>
        </defs>
        <g id="Gold_-_1" data-name="Gold - 1" clip-path="url(#clip-Gold_-_1)">
            <rect width="350" height="170" fill="#2c2c2c"/>
            <rect id="사각형_1" data-name="사각형 1" width="350" height="170" rx="14" fill="#fff"/>
            <text id="handle" transform="translate(23 32)" fill="#ffbe70" font-size="14" font-family="NotoSansKR-Black, Noto Sans KR" font-weight="800"><tspan x="0" y="0">{handle}</tspan></text>
            <text id="tier" data-name="tier" transform="translate(327 32)" fill="#febe70" font-size="12" font-family="NotoSansKR-Black, Noto Sans KR" font-weight="800"><tspan x="-38.376" y="0">{tier}</tspan></text>
    """.format(handle=handle, tier=tier)
    
    idx = 0
    today, now_in_loop = get_starting_day()
    print(today, now_in_loop)
    while True:
        color = "#F5F3F0"
        if solved_dict.get(now_in_loop) != None:
            color = "#FEBE70"
        
        nemo = '\n<rect id="사각형_2" data-name="사각형 2" width="15" height="15" rx="4"\
                transform="translate({x} {y})" fill="{color}"/>'.format(x=23 + (idx // 7) * 17, y=44 + (idx % 7) * 16, color=color)
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
