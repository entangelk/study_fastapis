from fastapi import FastAPI
app = FastAPI()
from routes.homes import router as event_router
from fastapi import Request
from fastapi.templating import Jinja2Templates
app.include_router(event_router, prefix="/home")

# html 들이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

from fastapi.middleware.cors import CORSMiddleware
# No 'Access-Control-Allow-Origin'
# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 접근 가능한 도메인만 허용하는 것이 좋습니다.
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root(Request:Request):
    # return {"message": "jisu World"}
    return templates.TemplateResponse("index.html",{'request':Request})

