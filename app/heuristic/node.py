class Node:

    def __init__(self, parent, position, cost, robot):
        self.parent = parent
        self.position = position
        self.cost = cost
        self.robot = robot

    def __str__(self):
        return '({}, {}) to {} with cost {}'.format(
            self.position[0], self.position[1], self.robot, self.cost
        )

    def __repr__(self):
        return '({}, {}) to {} with cost {}'.format(
            self.position[0], self.position[1], self.robot, self.cost
        )
