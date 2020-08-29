# -*- coding: utf-8 -*-

from loop_index.loop_index import LoopIndex

class Player:

    def __init__(self):
        self._points = 0
        self.revive() # Creates attribute _is_alive.

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

class PlayerContainer:

    def __init__(self, player_num):
        self._players = tuple(Player() for x in range(player_num))
        self._player_count = player_num

    def get_player(self, player_index):
        return self._players[player_index]

    def get_player_count(self):
        return self._player_count

    def give_points(self, player_points_dict):
        for player_index, points in player_points_dict.items():
            self._players[player_index].give_points(points)

    def print_scores(self):
        print("SCORES")
        player_index = LoopIndex(self._player_count)
        while player_index.iterate():
            i = player_index.get_value()
            points = self._players[i].get_points()
            print("Player " + str(i) + ": " + str(points))

    def revive_the_dead(self):
        for player in self._players:
            player.revive()
