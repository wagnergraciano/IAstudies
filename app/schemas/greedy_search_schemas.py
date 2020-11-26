from typing import Union
from pydantic import BaseModel


class GreedySearchSchemas(BaseModel):
    # Optional[list]  # np.zeros((13, 15))
    data: Union[list, list]


class GreedySearchSchemasResponse(GreedySearchSchemas):
    pass


'''
    Breve Representação da nossa matriz
    [
        [00, 00,  00, 00,  00,  00, 00,  00,  00, 00,  00,  00, 00,  00,   00],  ->   00    := Caminho
        [1,  00,  11, 31,  00,  41, 51,  00,  61, 71,  00,  81, 91,  00,  101],
        [2,  00,  12, 32,  00,  42, 52,  00,  62, 72,  00,  82, 92,  00,  102],
        [3,  00,  13, 33,  00,  43, 53,  00,  63, 73,  00,  83, 93,  00,  103],
        [4,  00,  14, 34,  00,  44, 54,  00,  64, 74,  00,  84, 94,  00,  104],
        [5,  00,  15, 35,  00,  45, 55,  00,  65, 75,  00,  85, 95,  00,  105],
        [6,  00,  16, 36,  00,  46, 56,  00,  66, 76,  00,  86, 96,  00,  106],
        [7,  00,  17, 37,  00,  47, 57,  00,  67, 77,  00,  87, 97,  00,  107],
        [8,  00,  18, 38,  00,  48, 58,  00,  68, 78,  00,  88, 98,  00,  108],
        [9,  00,  19, 39,  00,  49, 59,  00,  69, 79,  00,  89, 99,  00,  109],
        [10, 00,  20, 40,  00,  50, 60,  00,  70, 80,  00,  90, 100, 00,  110],  -> 1...110 := Estantes
        [00, 00,  00, 00,  00,  00, 00,  00,  00, 00,  00,  00, 00,  00,   XX],  ->   XX    := Recebedor (a)
        [22, 22,  22, 22,  22,  88, 88,  88,  88, 88,  88,  88, 88,  88,   88]   ->   22    := Robo 
                                                                                 ->   88    := Caminho Inválido
    ]
'''
