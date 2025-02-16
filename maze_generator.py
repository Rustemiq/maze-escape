from random import choice

MAZE_WIDTH = MAZE_HEIGHT = 15
MAZE_START = 0, 0
NEIGHBOURS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Board:
    def __init__(self):
        self.board = [[1] * MAZE_WIDTH
                      for _ in range(MAZE_WIDTH)]
        self.current_cell = MAZE_START
        self.stack = []

    def break_walls(self, x, y):
        x = x * 2 + 1
        y = y * 2 + 1
        walls = []
        for neighbour in NEIGHBOURS:
            wall = x + neighbour[0], y + neighbour[1]
            behind_wall = x + neighbour[0] * 2, y + neighbour[1] * 2
            if MAZE_WIDTH > behind_wall[0] >= 0 and MAZE_HEIGHT > behind_wall[1] >= 0:
                if self.board[behind_wall[1]][behind_wall[0]] == 1:
                    walls.append((wall, behind_wall))
        if len(walls) != 0:
            wall, behind_wall = choice(walls)
            self.board[wall[1]][wall[0]] = 0
            self.current_cell = ((behind_wall[0] - 1) // 2,
                                 (behind_wall[1] - 1) // 2)
            return True
        return False

    def open_cell(self, x, y):
        self.board[y * 2 + 1][x * 2 + 1] = 0

    def generate_maze(self):
        while True:
            self.open_cell(*self.current_cell)
            is_successfully = self.break_walls(*self.current_cell)
            if is_successfully:
                self.stack.append(self.current_cell)
            else:
                if len(self.stack) != 0:
                    self.current_cell = self.stack.pop()
                else:
                    break
        with open('maze.txt', 'w') as maze_file:
            maze_file.writelines(
                [''.join(map(str, line)) + '\n' for line in self.board])

Board().generate_maze()