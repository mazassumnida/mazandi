from typing import Optional
from fastapi import FastAPI, Response
from httpx import AsyncClient
from utils import create_solved_dict

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/{handle}")
async def generate_bedge(handle: str):
    # api = os.environ['API_SERVER']
    api = 'https://solved.ac/api/v3/user'
    user_info_url = api + '/show?handle=' + handle
    timestamp_url = api + '/history?handle=' + handle + '&topic=solvedCount'
    
    async with AsyncClient() as client:
        user_info = await client.get(user_info_url)
        timestamp = await client.get(timestamp_url)
        
    if user_info.status_code == 200 and timestamp.status_code == 200:
        user_info = user_info.json()
        timestamp = timestamp.json()
        print(create_solved_dict(timestamp))
    
    svg = """
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="350" height="170" viewBox="0 0 350 170">
        <defs>
            <clipPath id="clip-맞춤형_크기_1">
            <rect width="350" height="170"/>
            </clipPath>
        </defs>
    </svg>
    """.format(handle=handle)
    
    response = Response(content=svg, media_type='image/svg+xml')
    response.headers['Cache-Control'] = 'no-cache'
    
    return response
