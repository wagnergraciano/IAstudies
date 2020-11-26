import schemas

from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


@router.post("/greedy_search", response_model=schemas.AlgorithmsResponseSchemas)
def greedy_search(*, product_in: schemas.GreedySearchSchemas) -> Any:
    '''
        Pegar dados e passar para o Schema referente ao algoritmo Busca Gulosa
    '''
    return {"Hello": "World"}


@router.post("/a_star", response_model=schemas.AlgorithmsResponseSchemas)
def a_star(*, product_in: schemas.AStarSchemas) -> Any:
    '''
        Pegar dados e passar para o Schema referente ao algoritmo A*
    '''
    return {"Hello": "World"}
