# -*- coding: utf-8 -*-

from binary_decision_matrix import BinaryDecisionMatrix
from players import PlayerContainer

pc = PlayerContainer(3)

player_alive_conditions = (pc.get_player(0).is_alive,
                           pc.get_player(1).is_alive,
                           pc.get_player(2).is_alive)

dm = BinaryDecisionMatrix(player_alive_conditions)
dm.set_all_actions({(1, 0, 0): lambda: pc.give_points({0: 2}), # Players 1 and 2 die.
                    (0, 1, 0): lambda: pc.give_points({1: 2}), # Players 0 and 2 die.
                    (0, 0, 1): lambda: pc.give_points({2: 2}), # Players 0 and 1 die.
                    (0, 1, 1): lambda: pc.give_points({1: 1, 2: 1}), # Player 0 dies.
                    (1, 0, 1): lambda: pc.give_points({0: 1, 2: 1}), # Player 1 dies.
                    (1, 1, 0): lambda: pc.give_points({0: 1, 1: 1})}) #Player 2 dies.
# No points are awarded when all players or none die.

def end_round():
    dm.print_axis_values()
    dm.run()
    pc.print_scores()
    pc.revive_the_dead()
    print()

# Players 0 and 2 die.
pc.get_player(0).kill()
pc.get_player(2).kill()
end_round()

# Player 1 dies.
pc.get_player(1).kill()
end_round()

# No player dies.
end_round()

# All players die.
pc.get_player(0).kill()
pc.get_player(1).kill()
pc.get_player(2).kill()
end_round()
