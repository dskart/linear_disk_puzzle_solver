# Linear Disk Puzzle Solver

The starting configuration of this puzzle is a row of ℓ cells, with disks located on cells 0 through n−1. The goal is to move the disks to the end of the row using a constrained set of actions. At each step, a disk can only be moved to an adjacent empty cell, or to an empty cell two spaces away, provided another disk is located on the intervening square. Given these restrictions, it can be seen that in many cases, no movements will be possible for the majority of the disks. For example, from the starting position, the only two options are to move the last disk from cell n−1 to cell n, or to move the second-to-last disk from cell n−2 to cell n.

This was made as an exercise to implement a breadth-first graph search algorithm in order to solve a puzzle. So please take in account that this code was written in a few days without any professional review/standard .

## Getting Started

The file ["disk_gird.py"](disk_gird.py) contains all the code and breadth-first algorithm to solve our puzzle.

There are two versions of the puzzle:

- identical_disks where the order of the disks doesn't matter
- distinct_disks where the order of the disks matter. More concretely, if we abbreviate length as ℓ, then a desired solution moves the first disk from cell 0 to cell ℓ−1, the second disk from cell 1 to cell ℓ−2, ⋯, and the last disk from cell n−1 to cell ℓ−n.

### Prerequisites

- [tkinter](https://docs.python.org/3/library/tkinter.html)

## Running the puzzle solver

To solve the identical disk puzzle, call this function:

```[python]
solve_identical_disks(length, n)
```

To solve the distinct disk puzzle, call this function:

```[python]
solve_distinct_disks(length, n)
```

For both functions, "length" is the number of cells in the row and "n" is the number of disks

## Authors

- **Raphael Van Hoffelen** - [github](https://github.com/dskart) - [website](https://www.raphaelvanhoffelen.com/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
