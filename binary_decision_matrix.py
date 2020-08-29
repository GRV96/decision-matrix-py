# -*- coding: utf-8 -*-

from copy import deepcopy
from decision_matrix import DecisionMatrix
from loop_index.loop_index import LoopIndex

class BinaryDecisionMatrix(DecisionMatrix):

    def __init__(self, conditions):
        self._conditions = tuple(conditions)
        self._axis_count = len(self._conditions)
        self._check_presence_of_axes()
        self._build_matrix()
        self.set_default_action(None)

    def _get_axis_length(self, axis):
        return 2

    def print_axis_values(self):
        axis_index = LoopIndex(self._axis_count)
        while axis_index.iterate():
            i = axis_index.get_value()
            if self._conditions[i]():
                axis = "[0, 1]"
            else:
                axis = "[1, 0]"
            print("Axis " + str(i) + ": " + axis)

    def _run_submatrix(self, axis, submatrix):
        action_performed = False

        if callable(submatrix):
            submatrix()
            action_performed = True

        elif submatrix is not None and axis < self._axis_count:
            if self._conditions[axis]():
                subsub = submatrix[1]
            else:
                subsub = submatrix[0]

            action_performed = self._run_submatrix(axis+1, subsub)

        return action_performed
