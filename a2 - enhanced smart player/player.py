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
Misha Schwartz, and Jaisie Sin.

=== Module Description ===

This file contains the hierarchy of player classes.
"""
from __future__ import annotations
from typing import List, Optional, Tuple
import random
import pygame

from block import Block
from goal import Goal, generate_goals

from actions import KEY_ACTION, ROTATE_CLOCKWISE, ROTATE_COUNTER_CLOCKWISE, \
    SWAP_HORIZONTAL, SWAP_VERTICAL, SMASH, PASS, PAINT, COMBINE


def create_players(num_human: int, num_random: int, smart_players: List[int]) \
        -> List[Player]:
    """Return a new list of Player objects.

    <num_human> is the number of human player, <num_random> is the number of
    random players, and <smart_players> is a list of difficulty levels for each
    SmartPlayer that is to be created.

    The list should contain <num_human> HumanPlayer objects first, then
    <num_random> RandomPlayer objects, then the same number of SmartPlayer
    objects as the length of <smart_players>. The difficulty levels in
    <smart_players> should be applied to each SmartPlayer object, in order.
    """
    player_lst = []
    goals = generate_goals(num_human + num_random + len(smart_players))
    for i in range(num_human):
        player_lst.append(HumanPlayer(i, goals[i]))
    for i in range(num_human, num_random + num_human):
        player_lst.append(RandomPlayer(i, goals[i], 100))
    for i in range(num_random + num_human, num_random + num_human +
                   len(smart_players)):
        player_lst.append(SmartPlayer(i, goals[i], goals[0],
                                      smart_players[i - (num_random
                                                         + num_human)]))
    return player_lst


def _get_block(block: Block, location: Tuple[int, int], level: int) -> \
        Optional[Block]:
    """Return the Block within <block> that is at <level> and includes
    <location>. <location> is a coordinate-pair (x, y).

    A block includes all locations that are strictly inside of it, as well as
    locations on the top and left edges. A block does not include locations that
    are on the bottom or right edge.

    If a Block includes <location>, then so do its ancestors. <level> specifies
    which of these blocks to return. If <level> is greater than the level of
    the deepest block that includes <location>, then return that deepest block.

    If no Block can be found at <location>, return None.

    Preconditions:
        - 0 <= level <= max_depth
    """
    x = location[0]
    y = location[1]
    if (not block.position[0] <= x < block.position[0] + block.size) \
            or (not block.position[1] <= y < block.position[1] + block.size):
        return None
    elif block.level == level:
        return block
    elif len(block.children) == 0:
        return block
    else:
        for child in block.children:
            c_b = _get_block(child, location, level)
            if isinstance(c_b, Block):
                return c_b
        return None


def _random_block(board: Block) -> Block:
    """Returns a randomly generated Block from the given <board>.
    A private helper function
    """
    if len(board.children) == 0:
        return board
    else:
        r_c = random.randint(0, 4)
        if r_c == 0:
            return _random_block(board.children[0])
        if r_c == 1:
            return _random_block(board.children[1])
        if r_c == 2:
            return _random_block(board.children[2])
        if r_c == 3:
            return _random_block(board.children[3])
        else:
            return board


def _random_move(p: Player, board: Block) -> \
        Optional[Tuple[str, Optional[int], Block]]:
    """Returns a random move on <board> for player <p>. Returns None if there is
    no possible moves.
    A private helper function.
    """
    b = _random_block(board)
    r = random.randint(0, 6)
    counter = 0
    if board.max_depth == 0 and board.colour == p.goal.colour:
        return None
    while True:
        if r == 0:
            bc = board.create_copy()
            b_b = _get_block(bc, b.position, b.level)
            if b_b.rotate(1):
                return ROTATE_CLOCKWISE + (b,)
            else:
                r += 1
        if r == 1:
            bc = board.create_copy()
            b_b = _get_block(bc, b.position, b.level)
            if b_b.rotate(3):
                return ROTATE_COUNTER_CLOCKWISE + (b,)
            else:
                r += 1
        if r == 2:
            bc = board.create_copy()
            b_b = _get_block(bc, b.position, b.level)
            if b_b.swap(0):
                return SWAP_HORIZONTAL + (b,)
            else:
                r += 1
        if r == 3:
            bc = board.create_copy()
            b_b = _get_block(bc, b.position, b.level)
            if b_b.swap(1):
                return SWAP_VERTICAL + (b,)
            else:
                r += 1
        if r == 4:
            bc = board.create_copy()
            b_b = _get_block(bc, b.position, b.level)
            if b_b.smash():
                return SMASH + (b,)
            else:
                r += 1
        if r == 5:
            bc = board.create_copy()
            b_b = _get_block(bc, b.position, b.level)
            if b_b.paint(p.goal.colour):
                return PAINT + (b,)
            else:
                r += 1
        if r == 6:
            bc = board.create_copy()
            b_b = _get_block(bc, b.position, b.level)
            if b_b.combine():
                return COMBINE + (b,)
            else:
                r = 0
        counter += 1
        if counter > 2:
            b = _random_block(board)


class Player:
    """A player in the Blocky game.

    This is an abstract class. Only child classes should be instantiated.

    === Public Attributes ===
    id:
        This player's number.
    goal:
        This player's assigned goal for the game.
    """
    id: int
    goal: Goal

    def __init__(self, player_id: int, goal: Goal) -> None:
        """Initialize this Player.
        """
        self.goal = goal
        self.id = player_id

    def get_selected_block(self, board: Block) -> Optional[Block]:
        """Return the block that is currently selected by the player.

        If no block is selected by the player, return None.
        """
        raise NotImplementedError

    def process_event(self, event: pygame.event.Event) -> None:
        """Update this player based on the pygame event.
        """
        raise NotImplementedError

    def generate_move(self, board: Block) -> \
            Optional[Tuple[str, Optional[int], Block]]:
        """Return a potential move to make on the game board.

        The move is a tuple consisting of a string, an optional integer, and
        a block. The string indicates the move being made (i.e., rotate, swap,
        or smash). The integer indicates the direction (i.e., for rotate and
        swap). And the block indicates which block is being acted on.

        Return None if no move can be made, yet.
        """
        raise NotImplementedError


def _create_move(action: Tuple[str, Optional[int]], block: Block) -> \
        Tuple[str, Optional[int], Block]:
    return action[0], action[1], block


class HumanPlayer(Player):
    """A human player.
    """
    # === Private Attributes ===
    # _level:
    #     The level of the Block that the user selected most recently.
    # _desired_action:
    #     The most recent action that the user is attempting to do.
    #
    # == Representation Invariants concerning the private attributes ==
    #     _level >= 0
    _level: int
    _desired_action: Optional[Tuple[str, Optional[int]]]

    def __init__(self, player_id: int, goal: Goal) -> None:
        """Initialize this HumanPlayer with the given <renderer>, <player_id>
        and <goal>.
        """
        Player.__init__(self, player_id, goal)

        # This HumanPlayer has not yet selected a block, so set _level to 0
        # and _selected_block to None.
        self._level = 0
        self._desired_action = None

    def get_selected_block(self, board: Block) -> Optional[Block]:
        """Return the block that is currently selected by the player based on
        the position of the mouse on the screen and the player's desired level.

        If no block is selected by the player, return None.
        """
        mouse_pos = pygame.mouse.get_pos()
        block = _get_block(board, mouse_pos, min(self._level, board.max_depth))

        return block

    def process_event(self, event: pygame.event.Event) -> None:
        """Respond to the relevant keyboard events made by the player based on
        the mapping in KEY_ACTION, as well as the W and S keys for changing
        the level.
        """
        if event.type == pygame.KEYDOWN:
            if event.key in KEY_ACTION:
                self._desired_action = KEY_ACTION[event.key]
            elif event.key == pygame.K_w:
                self._level = max(0, self._level - 1)
                self._desired_action = None
            elif event.key == pygame.K_s:
                self._level += 1
                self._desired_action = None

    def generate_move(self, board: Block) -> \
            Optional[Tuple[str, Optional[int], Block]]:
        """Return the move that the player would like to perform. The move may
        not be valid.

        Return None if the player is not currently selecting a block.
        """
        block = self.get_selected_block(board)

        if block is None or self._desired_action is None:
            return None
        else:
            move = _create_move(self._desired_action, block)

            self._desired_action = None
            return move


class RandomPlayer(Player):
    """A No so smart Player. It generates a move by analyzing the scores of a
    number of random moves and pick the one that gives the highest score.
    """
    # === Private Attributes ===
    # _proceed:
    #   True when the player should make a move, False when the player should
    #   wait.
    # _difficulty:
    #   A number indicating how many random moves that the smart player should
    #   pick from.
    _proceed: bool
    _difficulty: int

    def __init__(self, player_id: int, goal: Goal, difficulty: int) -> None:
        Player.__init__(self, player_id, goal)
        self._difficulty = difficulty
        self._proceed = False

    def get_selected_block(self, board: Block) -> Optional[Block]:
        return None

    def process_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._proceed = True

    def generate_move(self, board: Block) -> \
            Optional[Tuple[str, Optional[int], Block]]:
        """Return a valid move by assessing multiple valid moves and choosing
        the move that results in the highest score for this player's goal (i.e.,
        disregarding penalties).

        A valid move is a move other than PASS that can be successfully
        performed on the <board>. If no move can be found that is better than
        the current score, this player will pass.

        This function does not mutate <board>.
        """
        if not self._proceed:
            return None  # Do not remove
        final_move = PASS + (board,)
        max_score = self.goal.score(board)
        for _ in range(self._difficulty):
            bc = board.create_copy()
            move = _random_move(self, bc)
            b = _get_block(board, move[-1].position, move[-1].level)
            if move[:2] == ('rotate', 1):
                move[-1].rotate(1)
                temp_score = self.goal.score(bc)
                if temp_score > max_score:
                    final_move = move[:-1] + (b,)
                    max_score = temp_score
            elif move[:2] == ('rotate', 3):
                move[-1].rotate(3)
                temp_score = self.goal.score(bc)
                if temp_score > max_score:
                    final_move = move[:-1] + (b,)
                    max_score = temp_score
            elif move[:2] == ('swap', 0):
                move[-1].swap(0)
                temp_score = self.goal.score(bc)
                if temp_score > max_score:
                    final_move = move[:-1] + (b,)
                    max_score = temp_score
            elif move[:2] == ('swap', 1):
                move[-1].swap(1)
                temp_score = self.goal.score(bc)
                if temp_score > max_score:
                    final_move = move[:-1] + (b,)
                    max_score = temp_score
            elif move[:2] == ('smash', None):
                move[-1].smash()
                temp_score = self.goal.score(bc)
                if temp_score > max_score:
                    final_move = move[:-1] + (b,)
                    max_score = temp_score
            elif move[:2] == ('combine', None):
                move[-1].combine()
                temp_score = self.goal.score(bc)
                if temp_score > max_score:
                    final_move = move[:-1] + (b,)
                    max_score = temp_score
            elif move[:2] == ('paint', None):
                move[-1].paint(self.goal.colour)
                temp_score = self.goal.score(bc)
                if temp_score > max_score:
                    final_move = move[:-1] + (b,)
                    max_score = temp_score
        self._proceed = False  # Must set to False before returning!
        return final_move


class SmartPlayer(Player):
    """A Smart Player. It generates a move by analyzing the scores of a number
    of random moves and pick the one that gives the highest score.
    """
    # === Private Attributes ===
    # _proceed:
    #   True when the player should make a move, False when the player should
    #   wait.
    # _difficulty:
    #   A number indicating how many random moves that the smart player should
    #   pick from.
    # _op_goal:
    #   Goal of the human opponent.
    _proceed: bool
    _difficulty: int
    _op_goal: Goal

    def __init__(self, player_id: int, goal: Goal, oppo_goal: Goal,
                 difficulty: int) -> None:
        Player.__init__(self, player_id, goal)
        self._difficulty = difficulty
        self._proceed = False
        self._op_goal = oppo_goal

    def get_selected_block(self, board: Block) -> Optional[Block]:
        return None

    def process_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._proceed = True

    def generate_move(self, board: Block) ->\
            Optional[Tuple[str, Optional[int], Block]]:
        """Return a valid move by assessing multiple valid moves and choosing
        the move that results in the highest score for this player's goal (i.e.,
        disregarding penalties).

        A valid move is a move other than PASS that can be successfully
        performed on the <board>. If no move can be found that is better than
        the current score, this player will pass.

        This function does not mutate <board>.
        """
        if not self._proceed:
            return None  # Do not remove
        # final_move1 = PASS + (board,)
        final_move2 = PASS + (board,)
        min_op_score = self._op_goal.score(board)
        op_current = self._op_goal.score(board)
        my_current = self.goal.score(board)
        scores = [my_current]
        moves = [PASS + (board,)]
        oppo = [op_current]
        max_score = self.goal.score(board)
        for i in range(3):
            for _ in range(self._difficulty):
                bc = board.create_copy()
                move = _random_move(self, bc)
                b = _get_block(board, move[-1].position, move[-1].level)
                if move[:2] == ('rotate', 1):
                    move[-1].rotate(1)
                    temp_score = self.goal.score(bc)
                    if temp_score > max_score:
                        final_move1 = move[:-1] + (b,)
                        moves[i] = final_move1
                        max_score = temp_score
                        scores[i] = max_score
                        oppo[i] = self._op_goal.score(bc)
                elif move[:2] == ('rotate', 3):
                    move[-1].rotate(3)
                    temp_score = self.goal.score(bc)
                    if temp_score > max_score:
                        final_move1 = move[:-1] + (b,)
                        moves[i] = final_move1
                        max_score = temp_score
                        scores[i] = max_score
                        oppo[i] = self._op_goal.score(bc)
                elif move[:2] == ('swap', 0):
                    move[-1].swap(0)
                    temp_score = self.goal.score(bc)
                    if temp_score > max_score:
                        final_move1 = move[:-1] + (b,)
                        moves[i] = final_move1
                        max_score = temp_score
                        scores[i] = max_score
                        oppo[i] = self._op_goal.score(bc)
                elif move[:2] == ('swap', 1):
                    move[-1].swap(1)
                    temp_score = self.goal.score(bc)
                    if temp_score > max_score:
                        final_move1 = move[:-1] + (b,)
                        moves[i] = final_move1
                        max_score = temp_score
                        scores[i] = max_score
                        oppo[i] = self._op_goal.score(bc)
                elif move[:2] == ('smash', None):
                    move[-1].smash()
                    temp_score = self.goal.score(bc) - 3
                    if temp_score > max_score:
                        final_move1 = move[:-1] + (b,)
                        moves[i] = final_move1
                        max_score = temp_score
                        scores[i] = max_score
                        oppo[i] = self._op_goal.score(bc)
                elif move[:2] == ('combine', None):
                    move[-1].combine()
                    temp_score = self.goal.score(bc) - 1
                    if temp_score > max_score:
                        final_move1 = move[:-1] + (b,)
                        moves[i] = final_move1
                        max_score = temp_score
                        scores[i] = max_score
                        oppo[i] = self._op_goal.score(bc)
                elif move[:2] == ('paint', None):
                    move[-1].paint(self.goal.colour)
                    temp_score = self.goal.score(bc) - 1
                    if temp_score > max_score:
                        final_move1 = move[:-1] + (b,)
                        moves[i] = final_move1
                        max_score = temp_score
                        scores[i] = max_score
                        oppo[i] = self._op_goal.score(bc)
            scores.append(my_current)
            moves.append(PASS + (board,))
            oppo.append(op_current)
        max_diff = []
        for j in range(len(scores)):
            max_diff.append(scores[j] - oppo[j])
        final_move1 = moves[max_diff.index(max(max_diff))]
        for _ in range(self._difficulty):
            bc2 = board.create_copy()
            op_move = _random_move(self, bc2)
            b = _get_block(board, op_move[-1].position, op_move[-1].level)
            if op_move[:2] == ('rotate', 1):
                op_move[-1].rotate(1)
                temp_opscore = self._op_goal.score(bc2)
                if (self.goal.score(bc2) - my_current) < (
                        temp_opscore - op_current):
                    continue
                if temp_opscore < min_op_score:
                    final_move2 = op_move[:-1] + (b,)
                    min_op_score = temp_opscore
            elif op_move[:2] == ('rotate', 3):
                op_move[-1].rotate(3)
                temp_opscore = self._op_goal.score(bc2)
                if (self.goal.score(bc2) - my_current) < (
                        temp_opscore - op_current):
                    continue
                if temp_opscore < min_op_score:
                    final_move2 = op_move[:-1] + (b,)
                    min_op_score = temp_opscore
            elif op_move[:2] == ('swap', 0):
                op_move[-1].swap(0)
                temp_opscore = self._op_goal.score(bc2)
                if (self.goal.score(bc2) - my_current) < (
                        temp_opscore - op_current):
                    continue
                if temp_opscore < min_op_score:
                    final_move2 = op_move[:-1] + (b,)
                    min_op_score = temp_opscore
            elif op_move[:2] == ('swap', 1):
                op_move[-1].swap(1)
                temp_opscore = self._op_goal.score(bc2)
                if (self.goal.score(bc2) - my_current) < (
                        temp_opscore - op_current):
                    continue
                if temp_opscore < min_op_score:
                    final_move2 = op_move[:-1] + (b,)
                    min_op_score = temp_opscore
            elif op_move[:2] == ('smash', None):
                op_move[-1].smash()
                temp_opscore = self._op_goal.score(bc2)
                if (self.goal.score(bc2) - my_current) < (
                        temp_opscore - op_current):
                    continue
                if temp_opscore < min_op_score - 3:
                    final_move2 = op_move[:-1] + (b,)
                    min_op_score = temp_opscore
            elif op_move[:2] == ('combine', None):
                op_move[-1].combine()
                temp_opscore = self._op_goal.score(bc2)
                if (self.goal.score(bc2) - my_current) < (
                        temp_opscore - op_current):
                    continue
                if temp_opscore < min_op_score - 1:
                    final_move2 = op_move[:-1] + (b,)
                    min_op_score = temp_opscore
            elif op_move[:2] == ('paint', None):
                op_move[-1].paint(self.goal.colour)
                temp_opscore = self._op_goal.score(bc2)
                if (self.goal.score(bc2) - my_current) < (
                        temp_opscore - op_current):
                    continue
                if temp_opscore < min_op_score - 1:
                    final_move2 = op_move[:-1] + (b,)
                    min_op_score = temp_opscore
        my_diff = max_score - my_current
        op_diff = op_current - min_op_score
        if my_diff >= op_diff:
            final_move = final_move1
        else:
            final_move = final_move2
        self._proceed = False  # Must set to False before returning!
        return final_move


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'allowed-io': ['process_event'],
        'allowed-import-modules': [
            'doctest', 'python_ta', 'random', 'typing', 'actions', 'block',
            'goal', 'pygame', '__future__'
        ],
        'max-attributes': 10,
        'generated-members': 'pygame.*'
    })
