import schemas

from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


@router.post("/greedy_search")
def greedy_search():
    return {"Hello": "World"}


@router.post("/a_star")
def a_star():
    return {"Hello": "World"}
