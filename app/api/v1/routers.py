import schemas

from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


# response_model=schemas.GreedySearchSchemasResponse
@router.post("/greedy_search")
def greedy_search(item: schemas.GreedySearchSchemas) -> Any:
    '''
        Pegar dados e passar para o Schema referente ao algoritmo Busca Gulosa
    '''
    return item


# response_model=schemas.AStarSchemasResponse
@router.post("/a_star")
def a_star(item: schemas.AStarSchemas) -> Any:
    '''
        Pegar dados e passar para o Schema referente ao algoritmo A*
    '''

    return item
