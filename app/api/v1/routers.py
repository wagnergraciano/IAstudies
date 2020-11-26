import schemas

from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


@router.get("/greedy_search")
def greedy_search():
    return {"Hello": "World"}


@router.get("/a_star")
def a_star():
    return {"Hello": "World"}
