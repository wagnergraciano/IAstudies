from fastapi import APIRouter

from api.v1 import routers

api_router = APIRouter()
api_router.include_router(
    routers.router, prefix='/algorithms', tags=['algorithms'])
