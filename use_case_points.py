# -*- coding: utf-8 -*-

from decision_matrix import DecisionMatrix
from loop_index.loop_index import LoopIndex

class Player:

    def __init__(self):
        self._points = 0
        self.revive()

    def get_points(self):
        return self._points

    def give_points(self, points_given):
        self._points += points_given

    def is_alive(self):
        return self._is_alive

    def kill(self):
        self._is_alive = False

    def revive(self):
        self._is_alive = True

players = (Player(), Player(), Player())

def give_points(player_points_dict):
    for player_index, points in player_points_dict.items():
        players[player_index].give_points(points)

def print_scores():
    print("SCORES")
    player_index = LoopIndex(len(players))
    while player_index.iterate():
        i = player_index.get_value()
        print("Player " + str(i) + ": " + str(players[i].get_points()))

def revive_the_dead():
    for player in players:
        player.revive()

player0_axis = (
    lambda: not players[0].is_alive(),
    lambda: players[0].is_alive())
player1_axis = (
    lambda: not players[1].is_alive(),
    lambda: players[1].is_alive())
player2_axis = (
    lambda: not players[2].is_alive(),
    lambda: players[2].is_alive())

dm = DecisionMatrix(player0_axis, player1_axis, player2_axis)

# All three players die.
dm.set_action(lambda: give_points({0: 0, 1: 0, 2: 0}), 1, 1, 1)

# Two players die.
dm.set_action(lambda: give_points({0: 2}), 1, 0, 0)
dm.set_action(lambda: give_points({1: 2}), 0, 1, 0)
dm.set_action(lambda: give_points({2: 2}), 0, 0, 1)

# One player dies.
dm.set_action(lambda: give_points({1: 1, 2: 1}), 0, 1, 1)
dm.set_action(lambda: give_points({0: 1, 2: 1}), 1, 0, 1)
dm.set_action(lambda: give_points({0: 1, 1: 1}), 1, 1, 0)

# No player dies.
dm.set_action(lambda: give_points({0: 0, 1: 0, 2: 0}), 0, 0, 0)

def end_round():
    dm.run()
    print_scores()
    revive_the_dead()
    print()

# Players 0 and 2 die.
players[0].kill()
players[2].kill()
end_round()

# Player 1 dies.
players[1].kill()
end_round()

# No player dies.
end_round()

# All players die.
players[0].kill()
players[1].kill()
players[2].kill()
end_round()
