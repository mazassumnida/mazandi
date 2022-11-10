from typing import Optional
from fastapi import FastAPI, Response
from httpx import AsyncClient

from utils import create_solved_dict, boj_rating_to_lv, get_starting_day, get_tomorrow, get_tier_name
from randoms import random_user, random_timestamp
import mapping

app = FastAPI()

def make_heatmap_svg(handle: str, tier: str, solved_dict: dict, color_theme: dict):
  tier_name = tier.split(' ')[0]
  solved_max = solved_dict['solved_max'] if 'solved_max' in solved_dict else 0

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
      <g id="zandies">
          <rect id="background" width="349" height="169" rx="14" fill="{bgcolor}" style="stroke-width:0.5; stroke:{border};"/>
          <text id="handle" transform="translate(23 32)" fill="{color}" font-size="14" font-family="NotoSansKR-Black, Noto Sans KR" font-weight="800" style="animation-delay:100ms">{handle}</text>
          <text id="tier" transform="translate(327 32)" fill="{color}" font-size="12" font-family="NotoSansKR-Black, Noto Sans KR" font-weight="800" text-anchor="end" style="animation-delay:300ms">{tier}</text>
  """.format(
    handle=handle,
    tier=tier,
    color=color_theme[tier_name][5],
    border=color_theme['border'],
    bgcolor=color_theme['background']
  )

  idx = 0
  today, now_in_loop = get_starting_day()

  while True:
      # solved.ac streak specs:
      # n := clamp (solved_max) to [4, 50]
      # [0, 0], [1, 0.1n), [0.1n, 0.3n), [0.3n, 0.6n), [0.6n, 1.0n] -- all values are rounded up
      if not solved_dict.get(now_in_loop):
          color = color_theme[tier_name][0]
      elif (solved_dict[now_in_loop]) >= ((solved_max * 6 + 9) // 10):
          color = color_theme[tier_name][4]
      elif (solved_dict[now_in_loop]) >= ((solved_max * 3 + 9) // 10):
          color = color_theme[tier_name][3]
      elif (solved_dict[now_in_loop]) >= ((solved_max * 1 + 9) // 10) and (solved_dict[now_in_loop]) > 1:
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

      if now_in_loop == today:
          break
      now_in_loop = get_tomorrow(now_in_loop)
  
  svg += """
      </g>
  </svg>
  """
  return svg

@app.get("/api")
async def generate_bedge(handle: str, theme: Optional[str] = "warm"):
    api = 'https://solved.ac/api/v3/user'
    user_info_url = api + '/show?handle=' + handle
    timestamp_url = api + '/history?handle=' + handle + '&topic=solvedCount'
    solved_dict = {}
    # 테마 색상표 (기본값: WARM)
    theme = theme if theme.upper() in mapping.THEMES else 'warm'
    color_theme = mapping.THEMES[theme.upper()]
    
    async with AsyncClient() as client:
        user_info = await client.get(user_info_url)
        timestamp = await client.get(timestamp_url)
        
    if user_info.status_code == 200 and timestamp.status_code == 200:
        user_info = user_info.json()
        timestamp = timestamp.json()
        
        print(timestamp)
        solved_dict = create_solved_dict(timestamp)
        
        rating = user_info['rating']
        tier = mapping.TIERS[boj_rating_to_lv(rating)]
    else:
        user_info = {'handle': handle, 'rating': 0, 'solved': 0}
        tier = 'Unknown'
    
    svg = make_heatmap_svg(handle, tier, solved_dict, color_theme)
    
    response = Response(content=svg, media_type='image/svg+xml')
    response.headers['Cache-Control'] = 'no-cache'
    
    return response


@app.get("/api/random")
async def generate_random_badge(
  tier: Optional[str] = None,
  theme: Optional[str] = "warm"):
  user = random_user(tier)
  handle = user['handle']
  solved_dict = create_solved_dict(random_timestamp())
  theme = theme if theme.upper() in mapping.THEMES else 'warm'
  color_theme = mapping.THEMES[theme.upper()]

  svg = make_heatmap_svg(handle, get_tier_name(user['tier']), solved_dict, color_theme)

  response = Response(content=svg, media_type='image/svg+xml')
  response.headers['Cache-Control'] = 'no-cache'

  return response
