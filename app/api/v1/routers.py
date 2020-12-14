import math
import schemas

from typing import Any, List
from heuristic.node import Node
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

grid: list = [
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
    [3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
]

robots: dict = {
    'R1': (12, 0),
    'R2': (12, 1),
    'R3': (12, 2),
    'R4': (12, 3),
    'R5': (12, 4)
}

path: list = []
start: tuple = (1, 14)


@router.post("/greedy_search")
async def greedy_search(item: schemas.GreedySearchSchemas) -> list:
    '''
        Pegar dados e passar para o Schema referente ao algoritmo Busca Gulosa
    '''

    node = Node(None, start, 0, 'R1')
    expand_nodes(node)
    print(f'\nGreedy Search: \n{path[:: -1]} \nItem: {item} \n\n')
    return path[:: -1]


@router.post("/a_star")
async def a_star(item: schemas.AStarSchemas) -> list:
    '''
        Pegar dados e passar para o Schema referente ao algoritmo A*
    '''

    node = Node(None, start, 0, 'R1')
    expand_nodes(node)
    print(f'\A Star: \n{path[:: -1]} \nItem: {item} \n\n')
    return path[:: -1]


# Trabalhando com a classe
def heuristic(cord0, cord1) -> None:
    return abs(cord0[0] - cord1[0]) + abs(cord0[1] - cord1[1])


def view_content(i, j) -> list:
    return grid[i][j]


def expand_nodes(node: Node) -> None:

    # se o conteudo da célula atual for um robo achou
    if view_content(node.position[0], node.position[1]) == 3:
        # print(node)
        return

    expand_node = []

    # caso contrario expande para as direcoes possiveis

    # Verifica 1 passo para baixo
    if (node.position[0] - 1) >= 0 and (view_content(node.position[0] - 1, node.position[1]) not in [0, 2, 4]):

        # verifica se é um ciclo (neto = avô)
        if node.parent == None or (node.position[0] - 1, node.position[1]) != node.parent.position:
            expand_node.append(
                Node(node,
                     (node.position[0] - 1, node.position[1]),
                     heuristic(
                         (node.position[0] - 1, node.position[1]), robots['R1']),
                     'R1'))

    # Verifica 1 passo para cima
    if (node.position[0] + 1) < len(grid) and (view_content(node.position[0] + 1, node.position[1]) not in [0, 2, 4]):
        if node.parent == None or (node.position[0] + 1, node.position[1]) != node.parent.position:
            expand_node.append(
                Node(node,
                     (node.position[0] + 1, node.position[1]),
                     heuristic(
                         (node.position[0] + 1, node.position[1]), robots['R1']),
                     'R1'))

    # Verifica 1 passo para esquerda
    if (node.position[1] - 1 >= 0) and (view_content(node.position[0], node.position[1] - 1) not in [0, 2, 4]):
        if node.parent == None or (node.position[0], node.position[1] - 1) != node.parent.position:
            expand_node.append(
                Node(node,
                     (node.position[0], node.position[1] - 1),
                     heuristic(
                         (node.position[0], node.position[1] - 1), robots['R1']),
                     'R1'))

    # Verifica 1 passo para direita
    if (node.position[1] + 1 < len(grid[0])) and (view_content(node.position[0], node.position[1] + 1) not in [0, 2, 4]):
        if node.parent == None or (node.position[0], node.position[1] + 1) != node.parent.position:
            expand_node.append(Node(
                node,
                (node.position[0], node.position[1] + 1),
                heuristic(
                    (node.position[0], node.position[1] + 1), robots['R1']),
                'R1'
            ))

    less_cost = math.inf
    node_to_expand = None

    for node in expand_node:
        if node.cost < less_cost:
            less_cost = node.cost
            node_to_expand = node

    path.append(
        f'{node_to_expand.position[0]}:{node_to_expand.position[1]}')

    expand_nodes(node_to_expand)
