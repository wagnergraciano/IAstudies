import schemas

from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

'''
    Base para como enviar o Json

    {
		"data": [
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
			[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
			[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
			[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
			[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
			[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
			[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
			[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
			[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
			[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
			[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
			[3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
		],

		* hall:      1
		* shelf:     0
		* robots:    3
		* delivery:  4
		* dead zone: 2
    }

'''


@router.post("/greedy_search")
def greedy_search(item: schemas.GreedySearchSchemas) -> Any:
    '''
        Pegar dados e passar para o Schema referente ao algoritmo Busca Gulosa
    '''
    return item


@router.post("/a_star")
def a_star(item: schemas.AStarSchemas) -> Any:
    '''
        Pegar dados e passar para o Schema referente ao algoritmo A*
    '''

    return item
