#!/usr/bin/python3
"""
island_perimeter function to calculate the perimeter of the island.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): A list of list of integers where
        0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four sides (up, down, left, right)
                if i == 0 or grid[i - 1][j] == 0:  # check top
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # check bottom
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # check left
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # check right
                    perimeter += 1

    return perimeter
