"""CSC148 Assignment 2

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: Diane Horton, David Liu, Mario Badr, Sophia Huynh, Misha Schwartz,
and Jaisie Sin

All of the files in this directory and all subdirectories are:
Copyright (c) Diane Horton, David Liu, Mario Badr, Sophia Huynh,
Misha Schwartz, and Jaisie Sin

=== Module Description ===

This file contains the hierarchy of Goal classes.
"""
from __future__ import annotations
import math
import random
from typing import List, Tuple
from block import Block
from settings import colour_name, COLOUR_LIST


def generate_goals(num_goals: int) -> List[Goal]:
    """Return a randomly generated list of goals with length num_goals.

    All elements of the list must be the same type of goal, but each goal
    must have a different randomly generated colour from COLOUR_LIST. No two
    goals can have the same colour.

    Precondition:
        - num_goals <= len(COLOUR_LIST)
    """
    g_lst = []
    r = random.random()
    i = 0
    c_used = []
    while i < num_goals:
        rc = random.randint(0, len(COLOUR_LIST) - 1)
        while rc in c_used:
            rc = random.randint(0, len(COLOUR_LIST) - 1)
        c_used.append(rc)
        i += 1
    if r < 0.5:
        for num in c_used:
            g_lst.append(PerimeterGoal(COLOUR_LIST[num]))
    else:
        for num in c_used:
            g_lst.append(BlobGoal(COLOUR_LIST[num]))
    return g_lst


def _flatten(block: Block) -> List[List[Tuple[int, int, int]]]:
    """Return a two-dimensional list representing <block> as rows and columns of
    unit cells.

    Return a list of lists L, where,
    for 0 <= i, j < 2^{max_depth - self.level}
        - L[i] represents column i and
        - L[i][j] represents the unit cell at column i and row j.

    Each unit cell is represented by a tuple of 3 ints, which is the colour
    of the block at the cell location[i][j]

    L[0][0] represents the unit cell in the upper left corner of the Block.
    """
    if len(block.children) == 0:
        re = []
        for r in range(2**(block.max_depth - block.level)):
            re.append([])
            c = 0
            while c < math.pow(2, (block.max_depth - block.level)):
                re[r].append(block.colour)
                c += 1
        return re
    else:
        re = []
        f0 = _flatten(block.children[0])
        f1 = _flatten(block.children[1])
        f2 = _flatten(block.children[2])
        f3 = _flatten(block.children[3])
        for i in range(len(f1)):
            re.append(f1[i] + f2[i])
        for i in range(len(f0)):
            re.append(f0[i] + f3[i])
        return re


class Goal:
    """A player goal in the game of Blocky.

    This is an abstract class. Only child classes should be instantiated.

    === Attributes ===
    colour:
        The target colour for this goal, that is the colour to which
        this goal applies.
    """
    colour: Tuple[int, int, int]

    def __init__(self, target_colour: Tuple[int, int, int]) -> None:
        """Initialize this goal to have the given target colour.
        """
        self.colour = target_colour

    def score(self, board: Block) -> int:
        """Return the current score for this goal on the given board.

        The score is always greater than or equal to 0.
        """
        raise NotImplementedError

    def description(self) -> str:
        """Return a description of this goal.
        """
        raise NotImplementedError


class PerimeterGoal(Goal):
    """A perimeter goal. A child class of Goal. The perimeter goal
    is to put the most possible units of a given colour on the outer
    perimeter of the board.
    """
    def score(self, board: Block) -> int:
        """Return the score given the current state of the <board>. The
        score is an integer calculated in terms of the number of unit cells
        on the perimeter of the Block. The corner unit cells count as
        two points.

        """
        f_b = _flatten(board)
        score = 0
        for item in f_b[0]:
            if item == self.colour:
                score += 1
        for item in f_b[-1]:
            if item == self.colour:
                score += 1
        for item in f_b:
            if item[0] == self.colour:
                score += 1
            if item[-1] == self.colour:
                score += 1
        return score

    def description(self) -> str:
        return 'Perimeter Goal: Put most unit cell ' \
               'of ' + colour_name(self.colour) + \
               ' on the outer perimeter.'


class BlobGoal(Goal):
    """A blob goal. A child class of Goal. The goal is to make the biggest
    blob on the board. A blob is a group of connected blocks with the
    same colour. Two blocks are connected if their sides are touching.
    """
    def score(self, board: Block) -> int:
        """Returns the score given the current state of the <board>. The score
        is the number of unit cells in the largest blob on the board.
        """
        f_b = _flatten(board)
        visited = []
        leng = len(f_b)
        for i in range(leng):
            visited.append([])
            j = 0
            while j < leng:
                visited[i].append(-1)
                j += 1
        max_b = 0
        for i_0 in range(leng):
            for j_0 in range(len(f_b[0])):
                b = self._undiscovered_blob_size((i_0, j_0), f_b, visited)
                if b > max_b:
                    max_b = b
        return max_b

    def _undiscovered_blob_size(self, pos: Tuple[int, int],
                                board: List[List[Tuple[int, int, int]]],
                                visited: List[List[int]]) -> int:
        """Return the size of the largest connected blob that (a) is of this
        Goal's target colour, (b) includes the cell at <pos>, and (c) involves
        only cells that have never been visited.

        If <pos> is out of bounds for <board>, return 0.

        <board> is the flattened board on which to search for the blob.
        <visited> is a parallel structure that, in each cell, contains:
            -1 if this cell has never been visited
            0  if this cell has been visited and discovered
               not to be of the target colour
            1  if this cell has been visited and discovered
               to be of the target colour

        Update <visited> so that all cells that are visited are marked with
        either 0 or 1.
        """
        x = pos[0]
        y = pos[1]
        if not ((0 <= x < len(board)) and (0 <= y < len(board))):
            return 0
        elif board[x][y] != self.colour:
            visited[x][y] = 0
            return 0
        elif visited[x][y] == 1:
            return 0
        else:
            visited[x][y] = 1
            s1 = self._undiscovered_blob_size((x+1, y), board, visited)
            s2 = self._undiscovered_blob_size((x, y+1), board, visited)
            s3 = self._undiscovered_blob_size((x-1, y), board, visited)
            s4 = self._undiscovered_blob_size((x, y-1), board, visited)
            return 1 + s1 + s2 + s3 + s4

    def description(self) -> str:
        return 'Blob Goal: Create the largest “blob” of ' \
               + colour_name(self.colour) + '.'


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'allowed-import-modules': [
            'doctest', 'python_ta', 'random', 'typing', 'block', 'settings',
            'math', '__future__'
        ],
        'max-attributes': 15
    })
