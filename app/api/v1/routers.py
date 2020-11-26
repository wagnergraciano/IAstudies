import schemas

from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

'''
    Base para como enviar o Json

    {
		"data": [
			[0,  0,  0,  0,   0,  0,  0,   0,  0,  0,   0,  0,  0,   0,    0],
			[1,  0,  11, 31,  0,  41, 51,  0,  61, 71,  0,  81, 91,  0,  101],
			[2,  0,  12, 32,  0,  42, 52,  0,  62, 72,  0,  82, 92,  0,  102],
			[3,  0,  13, 33,  0,  43, 53,  0,  63, 73,  0,  83, 93,  0,  103],
			[4,  0,  14, 34,  0,  44, 54,  0,  64, 74,  0,  84, 94,  0,  104],
			[5,  0,  15, 35,  0,  45, 55,  0,  65, 75,  0,  85, 95,  0,  105],
			[6,  0,  16, 36,  0,  46, 56,  0,  66, 76,  0,  86, 96,  0,  106],
			[7,  0,  17, 37,  0,  47, 57,  0,  67, 77,  0,  87, 97,  0,  107],
			[8,  0,  18, 38,  0,  48, 58,  0,  68, 78,  0,  88, 98,  0,  108],
			[9,  0,  19, 39,  0,  49, 59,  0,  69, 79,  0,  89, 99,  0,  109],
			[10, 0,  20, 40,  0,  50, 60,  0,  70, 80,  0,  90, 100, 0,  110], 
			[0,  0,  0,  0,   0,  0,  0,   0,  0,  0,   0,  0,  0,   0,   55],  
			[2,  2,  2,  2,   2,  8,  8,   8,  8,  8,   8,  8,  8,   8,   88] 
	    ]
    }

'''

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
