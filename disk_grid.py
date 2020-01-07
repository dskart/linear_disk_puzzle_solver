from abc import ABC, abstractmethod
import copy
import queue


class DiskGrid():
    def __init__(self, grid):
        self._grid = grid
        self._length = len(grid)
        self._num_disks = sum(i > 0 for i in grid)
        self._move = ()

    def grid_copy(self):
        return copy.deepcopy(self)

    def print_grid(self):
        print(self._grid)

    def perform_move(self, move):
        self._move = move

        from_cell = move[0]
        to_cell = move[1]

        init_cell_value = self._grid[from_cell]

        self._grid[from_cell] = 0
        self._grid[to_cell] = init_cell_value

    def get_move(self):
        return self._move

    def get_state(self):
        return tuple(self._grid)

    def solve(self):
        frontier = queue.Queue()
        frontier.put(self.grid_copy())

        came_from = {}
        came_from[self.get_state()] = None

        while not frontier.empty():
            current_node = frontier.get()
            if current_node.is_solved():
                return []
            for new_node in current_node.neighbors():
                new_state = new_node.get_state()
                if new_node.is_solved():
                    came_from[new_state] = current_node
                    solution_moves = self.backtrack_moves(came_from, new_node)
                    return solution_moves

                if new_state not in came_from.keys():
                    frontier.put(new_node)
                    came_from[new_state] = current_node

        return None

    def neighbors(self):
        for cell_idx, cell_val in enumerate(self._grid):
            if cell_val:
                move1 = (cell_idx, cell_idx+1)
                move2 = (cell_idx, cell_idx+2)
                move3 = (cell_idx, cell_idx-1)
                move4 = (cell_idx, cell_idx-2)
                possible_moves = (move1, move2, move3, move4)
                for move in possible_moves:
                    if self.move_is_legal(move):
                        puzzle_grid_copy = self.grid_copy()
                        puzzle_grid_copy.perform_move(move)
                        yield puzzle_grid_copy

    @abstractmethod
    def is_solved(self):
        pass

    def backtrack_moves(self, came_from, goal):
        start_state = self.get_state()
        current_node = goal
        current_state = current_node.get_state()
        path = []

        while current_state != start_state:
            path.insert(0, current_node.get_move())
            current_node = came_from[current_state]
            current_state = current_node.get_state()

        return path

    def move_is_legal(self, move):
        grid = self._grid
        from_cell = move[0]
        to_cell = move[1]
        move_len = to_cell-from_cell

        if from_cell >= self._length or to_cell >= self._length:
            return 0

        if from_cell < 0 or to_cell < 0:
            return

        if grid[from_cell] == 0:
            return 0

        if grid[to_cell] != 0:
            return 0

        if abs(move_len) != 2 and abs(move_len) != 1:
            return 0

        if move_len == 2 and grid[to_cell-1] < 1:
            return 0

        if move_len == -2 and grid[to_cell+1] < 1:
            return 0

        return 1


class IdenditicalDiskGrid(DiskGrid):
    def is_solved(self):
        num_disks = self._num_disks
        for disk in self._grid[-1:-(num_disks+1):-1]:
            if not disk:
                return False

        return True


class DistinctDiskGrid(DiskGrid):
    def is_solved(self):
        num_disks = self._num_disks
        expected_disk_value = 1
        for disk in self._grid[-1:-(num_disks+1):-1]:
            if disk != expected_disk_value:
                return False
            expected_disk_value += 1

        return True


def create_identical_disk_grid(length, n):
    grid = [0 for l in range(length)]
    for i in range(n):
        grid[i] = 1

    return IdenditicalDiskGrid(grid)


def create_distinct_disk_grid(length, n):
    grid = [0 for l in range(length)]
    for i in range(n):
        grid[i] = i + 1

    return DistinctDiskGrid(grid)


def solve_identical_disks(length, n):
    puzzle = create_identical_disk_grid(length, n)

    solution = puzzle.solve()
    return solution


def solve_distinct_disks(length, n):
    puzzle = create_distinct_disk_grid(length, n)

    solution = puzzle.solve()
    return solution
