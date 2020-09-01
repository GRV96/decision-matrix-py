# -*- coding: utf-8 -*-

from copy import deepcopy
from loop_index.loop_index import LoopIndex

class DecisionMatrix:
    """
    This class is a matrix containing actions at given coordinates. Its axes
    are tuplists of conditions: callable objects returning boolean values. When
    an instance is run, the actions whose coordinates match true conditions
    are performed.
    """

    def __init__(self, *condition_axes):
        """
        The DecisionMatrix constructor.

        Args:
            *condition_axes: tuplists containing conditions. DecisionMatrix
                needs at least one axis. Each axis must contain at least one
                condition.
        """
        self._build_axes(condition_axes)
        self._check_presence_of_axes()
        self._build_matrix()
        self.set_default_action(None)

    def _build_axes(self, condition_axes):
        axis_list = list()

        for ca in condition_axes:
            ca_tuple = tuple(ca)
            axis_list.append(ca_tuple)

        self._axes = tuple(axis_list)
        self._axis_count = len(self._axes)

    def _build_matrix(self):
        submatrix = None

        axis_index = LoopIndex(0, -1, self._axis_count-1)
        while axis_index.iterate():
            i = axis_index.get_value()
            axis_length = self._get_axis_length(i)
            submatrix = [deepcopy(submatrix) for x in range(axis_length)]

        self._matrix = submatrix

    def _check_presence_of_axes(self):
        if self._axis_count <= 0:
            raise ValueError("DecisionMatrix needs at least one axis."
                             + " It was not given any.")

    def get_axis_count(self):
        """
        Accessor of the number of axes.

        Returns:
            int: the number of axes of this DecisionMatrix.
        """
        return self._axis_count

    def _get_axis_length(self, axis):
        return len(self._axes[axis])

    def print_axis_values(self):
        """
        This method is a tool for debugging. It displays the boolean value of
        all conditions of all axes in the console. False and True are represented
        with 0 and 1 respectively.
        """
        axis_index = LoopIndex(self._axis_count)
        while axis_index.iterate():
            i = axis_index.get_value()
            current_axis = self._axes[i]
            axis_values = list()

            condition_index = LoopIndex(len(current_axis))
            while condition_index.iterate():
                j = condition_index.get_value()
                if current_axis[j]():
                    axis_values.append(1)
                else:
                    axis_values.append(0)

            print("Axis " + str(i) + ": " + str(axis_values))

    def run(self):
        """
        Browses the matrix checking the truth value of every coordinate set. If
        the coordinates are true, the associated action is performed. If no action
        is performed after the browsing and a default action has been specified,
        that action is performed.
        """
        action_performed = self._run_submatrix(0, self._matrix)

        if not action_performed and self._default_action is not None:
            self._default_action()

    def _run_submatrix(self, axis, submatrix):
        action_performed = False

        index = LoopIndex(len(submatrix))
        while index.iterate():
            i = index.get_value()

            if self._axes[axis][i]():
                next_axis = axis + 1
                subsub = submatrix[i]

                if callable(subsub):
                    subsub()
                    action_performed = True
                elif subsub is not None and next_axis < self._axis_count:
                    next_iter_value = self._run_submatrix(next_axis, subsub)
                    action_performed = action_performed or next_iter_value

        return action_performed

    def set_action(self, action, *coordinates):
        """
        Stores an action in the matrix at the specified coordinates.

        Args:
            action: a callable object. Its return value will not be recorded
                or used.
            *coordinates: integral values indicating where the action will be
                stored in the matrix.
        """
        submatrix = self._matrix

        coord_index = LoopIndex(len(coordinates)-1)
        while coord_index.iterate():
            i = coord_index.get_value()
            coordinate = coordinates[i]
            submatrix = submatrix[coordinate]

        submatrix[coordinates[self._axis_count-1]] = action

    def set_all_actions(self, coord_action_dict):
        """
        Receives actions in a dictionary and stores them in the matrix.

        Args:
            coord_action_dict (dictionary): contains actions (values) paired with
            the coordinates (keys) where they must be stored.
        """
        self._set_all_actions_rec(self._matrix, [], coord_action_dict)

    def _set_all_actions_rec(self, submatrix, submat_coord, coord_action_dict):
        index = LoopIndex(len(submatrix))
        while index.iterate():
            i = index.get_value()
            subsub = submatrix[i]
            subsub_coord = submat_coord + [i]

            if type(subsub) is list:
                self._set_all_actions_rec(subsub, subsub_coord,
                                          coord_action_dict)
            else:
                submatrix[i] = coord_action_dict.get(tuple(subsub_coord))

    def set_default_action(self, action):
        """
        The specified action will be performed if all conditions are false. The
        default action can be set to None if it is not wanted. On instantiation,
        DecisionMatrix does not have a default action. The action will only be
        set as default if it is None or callable.

        Args:
            action: a callable object. Its return value will not be recorded
                or used.

        Returns:
            bool: True if action was set as the default action, False otherwise.
        """
        if action is None or callable(action):
            self._default_action = action
            return True
        else:
            return False
