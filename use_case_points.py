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

# Player 1 wins the round by killing players 0 and 2.
players[0].kill()
players[2].kill()

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

dm.set_action(lambda: give_points({0: 1}), 1, 0, 0)
dm.set_action(lambda: give_points({1: 1}), 0, 1, 0)
dm.set_action(lambda: give_points({2: 1}), 0, 0, 1)

dm.run()

print_scores()
