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
    'R0': (12, 0),
    'R1': (12, 1),
    'R2': (12, 2),
    'R3': (12, 3),
    'R4': (12, 4)
}

@router.post("/greedy_search")
async def greedy_search(item: schemas.GreedySearchSchemas) -> list:
    '''
        Pegar dados e passar para o Schema referente ao algoritmo Busca Gulosa
    '''
    return {}


@router.post("/a_star")
async def a_star(item: schemas.AStarSchemas) -> list:
    '''
        Pegar dados e passar para o Schema referente ao algoritmo A*
    '''

    result = AStar().search(item.package)
    return result


class AStar:

    def view_content(self, i, j) -> int:
        """Visualiza o conteúdo de uma posição qualquer da matriz/grid.
        """
        return grid[i][j]

    def choose_best_robot(self, start) -> str:
        """ Definido um start para procurar o robô, essa função calcula com base
            na heuristica, Manhattan distance, qual o robô mais próximo do start e retorna
            sua chave no dict de robôs da aplicação.
        """
        costs = {}
        for robot in robots.keys():
            costs[robot] = self.heuristic(robots[robot], start)
        
        return min(costs.items(), key=lambda x: x[1])[0]

    def find_real_start(self, start) -> tuple:
        """ Define a posição inicial para busca, considerando um (i, j) pertecente a 
            um corredor qualquer mais próximo do (i_0, j_0) da posição inicial.
        """

        # Verifica a direita
        if (start[1] + 1 < len(grid[0])) and (self.view_content(start[0], start[1] + 1) not in [0, 2, 4]):
            return (start[0], start[1] + 1)
        # Verifica a esquerda
        if (start[1] - 1) >= 0 and (self.view_content(start[0], start[1] - 1) not in [0, 2, 4]):
            return (start[0], start[1] - 1)

    def heuristic(self, cord0, cord1) -> int:
        """Implementa uma heuristica com base na distância de manhattan.
        """
        return abs(cord0[0] - cord1[0]) + abs(cord0[1] - cord1[1])

    def expand_nodes(self, queue: list) -> Node:
        expands = 0
        node = queue[0]

        # se o conteudo da célula atual for um robo achou
        if self.view_content(node.position[0], node.position[1]) == 3:
            # path.append('{}:{}'.format(node.position[0], node.position[1]))
            return node

        # caso contrario expande para as direcoes possiveis

        # Verifica 1 passo para baixo
        if (node.position[0] - 1) >= 0 and (self.view_content(node.position[0] - 1, node.position[1]) not in [0, 2, 4]):
            # verifica se é um ciclo (neto = avô)
            if node.parent == None or (node.position[0] - 1, node.position[1]) != node.parent.position:
                expands += 1
                queue.append(
                    Node(node,
                        (node.position[0] - 1, node.position[1]),
                        self.heuristic(
                            (node.position[0] - 1, node.position[1]), robots[node.robot]) + node.steps,
                        node.robot,
                        node.steps + 1))

        # Verifica 1 passo para cima
        if (node.position[0] + 1) < len(grid) and (self.view_content(node.position[0] + 1, node.position[1]) not in [0, 2, 4]):
            if node.parent == None or (node.position[0] + 1, node.position[1]) != node.parent.position:
                expands += 1
                queue.append(
                    Node(node,
                        (node.position[0] + 1, node.position[1]),
                        self.heuristic(
                            (node.position[0] + 1, node.position[1]), robots[node.robot]) + node.steps,
                        node.robot, 
                        node.steps + 1))

        # Verifica 1 passo para esquerda
        if (node.position[1] - 1 >= 0) and (self.view_content(node.position[0], node.position[1] - 1) not in [0, 2, 4]):
            if node.parent == None or (node.position[0], node.position[1] - 1) != node.parent.position:
                expands += 1
                queue.append(
                    Node(node,
                        (node.position[0], node.position[1] - 1),
                        self.heuristic(
                            (node.position[0], node.position[1] - 1), robots[node.robot]) + node.steps,
                        node.robot,
                        node.steps + 1))

        # Verifica 1 passo para direita
        if (node.position[1] + 1 < len(grid[0])) and (self.view_content(node.position[0], node.position[1] + 1) not in [0, 2, 4]):
            if node.parent == None or (node.position[0], node.position[1] + 1) != node.parent.position:
                expands += 1
                queue.append(
                    Node(
                        node,
                        (node.position[0], node.position[1] + 1),
                        self.heuristic(
                            (node.position[0], node.position[1] + 1), robots[node.robot]) + node.steps,
                        node.robot,
                        node.steps + 1))

        del queue[0]
        queue = sorted(queue, key=lambda x: x.cost)
        
        return self.expand_nodes(queue)

    def search(self, start) -> list:
        real_start = self.find_real_start(start)
        robot = self.choose_best_robot(real_start)
        
        # Cria o nó inicial para a real posição inicial
        node = Node(None, real_start, 0, robot, 1)
        queue_to_expand = [ node ]

        node = self.expand_nodes(queue_to_expand)      

        # Atualizando conteúdo do grid e posição do robo
        grid[robots[robot][0]][robots[robot][1]] = 1
        grid[start[0]][start[1]] = 3
        robots[robot] = tuple(start)

        # Montando o retorno    
        result = []

        while node.parent != None:
            result.append('{}:{}'.format(node.position[0], node.position[1]))
            node = node.parent

        result.append('{}:{}'.format(real_start[0], real_start[1]))
        result.append('{}:{}'.format(start[0], start[1]))

        print(robots)

        return {
            'robot': robot,
            'result': result
        }

class GreedySearch:
    
    def search(self, start) -> list:
        pass

