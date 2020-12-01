import uvicorn

from core import settings
from fastapi import FastAPI
from api.v1 import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)
app.include_router(api_router, prefix=settings.API_V1_STR)
app.add_middleware(
    CORSMiddleware, allow_origins=settings.ORIGINS,
    allow_credentials=settings.ALLOOW_CREDENTIALS,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT,
                log_level=settings.LOG_LEVEL)
