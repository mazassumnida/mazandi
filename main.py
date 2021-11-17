from typing import Optional
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/{handle}")
def generate_bedge(handle: str):
    
    svg = """
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="350" height="170" viewBox="0 0 350 170">
        <defs>
            <clipPath id="clip-맞춤형_크기_1">
            <rect width="350" height="170"/>
            </clipPath>
        </defs>
        <g id="맞춤형_크기_1" data-name="맞춤형 크기 – 1" clip-path="url(#clip-맞춤형_크기_1)">
            <rect width="350" height="170" fill="#2c2c2c"/>
            <rect id="사각형_1" data-name="사각형 1" width="350" height="170" rx="14" fill="#fff"/>
            <text id="{handle}" transform="translate(23 32)" fill="#ffbe70" font-size="14" font-family="NotoSansKR-Black, Noto Sans KR" font-weight="800"><tspan x="0" y="0">ccoco</tspan></text>
            <text id="Gold_1" data-name="Gold 1" transform="translate(327 32)" fill="#febe70" font-size="12" font-family="NotoSansKR-Black, Noto Sans KR" font-weight="800"><tspan x="-38.376" y="0">Gold 1</tspan></text>
            <rect id="사각형_2" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(23 44)" fill="#f5f3f0"/>
            <rect id="사각형_2-2" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(40 44)" fill="#f5f3f0"/>
            <rect id="사각형_2-3" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(57 44)" fill="#f5f3f0"/>
            <rect id="사각형_2-4" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(74 44)" fill="#f5f3f0"/>
            <rect id="사각형_2-5" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(91 44)" fill="#febe70"/>
            <rect id="사각형_2-6" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(108 44)" fill="#f48554"/>
            <rect id="사각형_2-7" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(125 44)" fill="#f5f3f0"/>
            <rect id="사각형_2-8" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(142 44)" fill="#f5f3f0"/>
            <rect id="사각형_2-9" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(159 44)" fill="#fde7b4"/>
            <rect id="사각형_2-10" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(176 44)" fill="#f5f3f0"/>
            <rect id="사각형_2-11" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(193 44)" fill="#f5f3f0"/>
            <rect id="사각형_2-12" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(210 44)" fill="#febe70"/>
            <rect id="사각형_2-13" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(227 44)" fill="#febe70"/>
            <rect id="사각형_2-14" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(244 44)" fill="#f5f3f0"/>
            <rect id="사각형_2-15" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(261 44)" fill="#f5f3f0"/>
            <rect id="사각형_2-16" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(278 44)" fill="#f5f3f0"/>
            <rect id="사각형_2-17" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(295 44)" fill="#fde7b4"/>
            <rect id="사각형_2-18" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(312 44)" fill="#f5f3f0"/>
            <rect id="사각형_2-19" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(23 60)" fill="#f5f3f0"/>
            <rect id="사각형_2-20" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(40 60)" fill="#f5f3f0"/>
            <rect id="사각형_2-21" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(57 60)" fill="#f5f3f0"/>
            <rect id="사각형_2-22" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(74 60)" fill="#f5f3f0"/>
            <rect id="사각형_2-23" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(91 60)" fill="#f5f3f0"/>
            <rect id="사각형_2-24" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(108 60)" fill="#fde7b4"/>
            <rect id="사각형_2-25" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(125 60)" fill="#f5f3f0"/>
            <rect id="사각형_2-26" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(142 60)" fill="#f5f3f0"/>
            <rect id="사각형_2-27" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(159 60)" fill="#fde7b4"/>
            <rect id="사각형_2-28" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(176 60)" fill="#f5f3f0"/>
            <rect id="사각형_2-29" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(193 60)" fill="#fde7b4"/>
            <rect id="사각형_2-30" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(210 60)" fill="#f48554"/>
            <rect id="사각형_2-31" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(227 60)" fill="#f5f3f0"/>
            <rect id="사각형_2-32" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(244 60)" fill="#f5f3f0"/>
            <rect id="사각형_2-33" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(261 60)" fill="#f5f3f0"/>
            <rect id="사각형_2-34" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(278 60)" fill="#f5f3f0"/>
            <rect id="사각형_2-35" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(295 60)" fill="#f5f3f0"/>
            <rect id="사각형_2-36" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(312 60)" fill="#fde7b4"/>
            <rect id="사각형_2-37" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(23 76)" fill="#f5f3f0"/>
            <rect id="사각형_2-38" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(40 76)" fill="#f5f3f0"/>
            <rect id="사각형_2-39" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(57 76)" fill="#f5f3f0"/>
            <rect id="사각형_2-40" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(74 76)" fill="#f5f3f0"/>
            <rect id="사각형_2-41" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(91 76)" fill="#f5f3f0"/>
            <rect id="사각형_2-42" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(108 76)" fill="#f5f3f0"/>
            <rect id="사각형_2-43" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(125 76)" fill="#f5f3f0"/>
            <rect id="사각형_2-44" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(142 76)" fill="#f5f3f0"/>
            <rect id="사각형_2-45" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(159 76)" fill="#f5f3f0"/>
            <rect id="사각형_2-46" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(176 76)" fill="#f5f3f0"/>
            <rect id="사각형_2-47" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(193 76)" fill="#fde7b4"/>
            <rect id="사각형_2-48" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(210 76)" fill="#febe70"/>
            <rect id="사각형_2-49" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(227 76)" fill="#f5f3f0"/>
            <rect id="사각형_2-50" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(244 76)" fill="#fde7b4"/>
            <rect id="사각형_2-51" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(261 76)" fill="#f5f3f0"/>
            <rect id="사각형_2-52" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(278 76)" fill="#f5f3f0"/>
            <rect id="사각형_2-53" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(295 76)" fill="#f48554"/>
            <rect id="사각형_2-54" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(312 76)" fill="#ffbe70"/>
            <rect id="사각형_2-55" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(23 92)" fill="#f5f3f0"/>
            <rect id="사각형_2-56" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(40 92)" fill="#f5f3f0"/>
            <rect id="사각형_2-57" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(57 92)" fill="#f5f3f0"/>
            <rect id="사각형_2-58" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(74 92)" fill="#f5f3f0"/>
            <rect id="사각형_2-59" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(91 92)" fill="#f5f3f0"/>
            <rect id="사각형_2-60" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(108 92)" fill="#f5f3f0"/>
            <rect id="사각형_2-61" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(125 92)" fill="#febe70"/>
            <rect id="사각형_2-62" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(142 92)" fill="#f5f3f0"/>
            <rect id="사각형_2-63" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(159 92)" fill="#f5f3f0"/>
            <rect id="사각형_2-64" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(176 92)" fill="#fde7b4"/>
            <rect id="사각형_2-65" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(193 92)" fill="#f5f3f0"/>
            <rect id="사각형_2-66" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(210 92)" fill="#fde7b4"/>
            <rect id="사각형_2-67" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(227 92)" fill="#f5f3f0"/>
            <rect id="사각형_2-68" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(244 92)" fill="#f5f3f0"/>
            <rect id="사각형_2-69" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(261 92)" fill="#f5f3f0"/>
            <rect id="사각형_2-70" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(278 92)" fill="#f5f3f0"/>
            <rect id="사각형_2-71" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(295 92)" fill="#fde7b4"/>
            <rect id="사각형_2-72" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(312 92)" fill="#febe70"/>
            <rect id="사각형_2-73" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(23 108)" fill="#f5f3f0"/>
            <rect id="사각형_2-74" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(40 108)" fill="#f5f3f0"/>
            <rect id="사각형_2-75" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(57 108)" fill="#f5f3f0"/>
            <rect id="사각형_2-76" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(74 108)" fill="#f5f3f0"/>
            <rect id="사각형_2-77" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(91 108)" fill="#fde7b4"/>
            <rect id="사각형_2-78" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(108 108)" fill="#f5f3f0"/>
            <rect id="사각형_2-79" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(125 108)" fill="#f5f3f0"/>
            <rect id="사각형_2-80" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(142 108)" fill="#febe70"/>
            <rect id="사각형_2-81" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(159 108)" fill="#f5f3f0"/>
            <rect id="사각형_2-82" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(176 108)" fill="#f48554"/>
            <rect id="사각형_2-83" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(193 108)" fill="#febe70"/>
            <rect id="사각형_2-84" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(210 108)" fill="#febe70"/>
            <rect id="사각형_2-85" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(227 108)" fill="#f5f3f0"/>
            <rect id="사각형_2-86" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(244 108)" fill="#f5f3f0"/>
            <rect id="사각형_2-87" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(261 108)" fill="#f5f3f0"/>
            <rect id="사각형_2-88" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(278 108)" fill="#febe70"/>
            <rect id="사각형_2-89" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(295 108)" fill="#f5f3f0"/>
            <rect id="사각형_2-90" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(312 108)" fill="#f5f3f0"/>
            <rect id="사각형_2-91" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(23 124)" fill="#f5f3f0"/>
            <rect id="사각형_2-92" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(40 124)" fill="#f5f3f0"/>
            <rect id="사각형_2-93" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(57 124)" fill="#f5f3f0"/>
            <rect id="사각형_2-94" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(74 124)" fill="#fde7b4"/>
            <rect id="사각형_2-95" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(91 124)" fill="#febe70"/>
            <rect id="사각형_2-96" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(108 124)" fill="#f5f3f0"/>
            <rect id="사각형_2-97" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(125 124)" fill="#f5f3f0"/>
            <rect id="사각형_2-98" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(142 124)" fill="#f5f3f0"/>
            <rect id="사각형_2-99" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(159 124)" fill="#f5f3f0"/>
            <rect id="사각형_2-100" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(176 124)" fill="#febe70"/>
            <rect id="사각형_2-101" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(193 124)" fill="#fde7b4"/>
            <rect id="사각형_2-102" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(210 124)" fill="#f5f3f0"/>
            <rect id="사각형_2-103" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(227 124)" fill="#fde7b4"/>
            <rect id="사각형_2-104" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(244 124)" fill="#f5f3f0"/>
            <rect id="사각형_2-105" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(261 124)" fill="#f5f3f0"/>
            <rect id="사각형_2-106" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(278 124)" fill="#fde7b4"/>
            <rect id="사각형_2-107" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(295 124)" fill="#f5f3f0"/>
            <rect id="사각형_2-108" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(312 124)" fill="#fde7b4"/>
            <rect id="사각형_2-109" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(23 140)" fill="#f5f3f0"/>
            <rect id="사각형_2-110" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(40 140)" fill="#f5f3f0"/>
            <rect id="사각형_2-111" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(57 140)" fill="#f5f3f0"/>
            <rect id="사각형_2-112" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(74 140)" fill="#f5f3f0"/>
            <rect id="사각형_2-113" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(91 140)" fill="#fde7b4"/>
            <rect id="사각형_2-114" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(108 140)" fill="#f5f3f0"/>
            <rect id="사각형_2-115" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(125 140)" fill="#fde7b4"/>
            <rect id="사각형_2-116" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(142 140)" fill="#f5f3f0"/>
            <rect id="사각형_2-117" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(159 140)" fill="#fde7b4"/>
            <rect id="사각형_2-118" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(176 140)" fill="#f5f3f0"/>
            <rect id="사각형_2-119" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(193 140)" fill="#febe70"/>
            <rect id="사각형_2-120" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(210 140)" fill="#f5f3f0"/>
            <rect id="사각형_2-121" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(227 140)" fill="#f5f3f0"/>
            <rect id="사각형_2-122" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(244 140)" fill="#f5f3f0"/>
            <rect id="사각형_2-123" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(261 140)" fill="#f5f3f0"/>
            <rect id="사각형_2-124" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(278 140)" fill="#f5f3f0"/>
            <rect id="사각형_2-125" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(295 140)" fill="#fde7b4"/>
            <rect id="사각형_2-126" data-name="사각형 2" width="15" height="15" rx="4" transform="translate(312 140)" fill="#f5f3f0"/>
        </g>
    </svg>
    """.format(handle=handle)
    response = Response(content=svg, media_type='image/svg+xml')
    response.headers['Cache-Control'] = 'no-cache'
    return response
