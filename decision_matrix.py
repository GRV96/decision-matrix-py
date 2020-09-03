# -*- coding: utf-8 -*-

from copy import deepcopy
from loop_index.loop_index import LoopIndex

class DecisionMatrix:
    """
    This class is a matrix containing actions at given coordinates. Its axes
    are tuplists of conditions (callable objects returning boolean values). A
    coordinate is true if the condition to which it corresponds is true.
    When an instance is run, the actions whose coordinates are true are invoked.
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
        self._matrix = dict()
        self.set_default_action(None)

    def _build_axes(self, condition_axes):
        axis_list = list()

        for ca in condition_axes:
            ca_tuple = tuple(ca)
            axis_list.append(ca_tuple)

        self._axes = tuple(axis_list)
        self._axis_count = len(self._axes)

    def _check_presence_of_axes(self):
        if self._axis_count < 1:
            raise ValueError("DecisionMatrix needs at least one axis."
                             + " It was not given any.")

    def _check_coordinates(self, coordinates):
        if not self.has_coordinates(coordinates):
            self._raise_coord_value_error(coordinates)

    def clear_actions(self):
        """
        Deletes all actions stored in this matrix except the default action.
        In order to delete it, call set_default_action(None).
        """
        self._matrix.clear()

    def _coordinate_is_true(self, axis, coordinate):
        return self._axes[axis][coordinate]()

    def _coordinates_are_true(self, coordinates):
        index = LoopIndex(self._axis_count)
        while index.iterate():
            i = index.get_value()
            coordinate = coordinates[i]

            if not self._coordinate_is_true(i, coordinate):
                return False

        return True

    def _get_all_axis_lengths(self):
        lengths = list()
        axis_index = LoopIndex(self._axis_count)
        while axis_index.iterate():
            i = axis_index.get_value()
            lengths.append(self._get_axis_length(i))
        return tuple(lengths)

    def get_axis_count(self):
        """
        Accessor of the number of axes.

        Returns:
            int: the number of axes of this DecisionMatrix.
        """
        return self._axis_count

    def _get_axis_length(self, axis):
        return len(self._axes[axis])

    def has_coordinates(self, coordinates):
        """
        Determines whether the given coordinates exist in this matrix.

        Args:
            coordinates (tuplist): must be integral numbers.

        Returns:
            bool: True if the coordinates exist in this matrix, False otherwise.
        """
        coord_length = len(coordinates)

        if coord_length != self._axis_count:
            return False

        coord_index = LoopIndex(coord_length)
        while coord_index.iterate():
            i = coord_index.get_value()
            coordinate = coordinates[i]
            if coordinate < 0 or coordinate >= self._get_axis_length(i):
                return False

        return True

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

    def _raise_coord_value_error(self, coordinates):
        raise ValueError("Coordinates " + str(coordinates)
                         + " are not valid. This matrix has "
                         + str(self._axis_count) + " axes whose lengths are "
                         + str(self._get_all_axis_lengths()) + ".")

    def run(self):
        """
        Browses the matrix checking the truth value of every coordinate set. If
        the coordinates are true, the associated action is invoked. If no action
        is invoked after the browsing and a default action has been specified,
        that action is performed.
        """
        action_performed = False

        for coordinates, action in self._matrix.items():
            if self._coordinates_are_true(coordinates):
                action()
                action_performed = True

        if not action_performed and self._default_action is not None:
            self._default_action()

    def set_action(self, coordinates, action):
        """
        Stores an action in the matrix at the specified coordinates.

        Args:
            coordinates (tuplist): integral values indicating where the action
                will be stored in the matrix.
            action: a callable object. Its return value will not be recorded
                or used.

        Raises:
            ValueError: if action is not callable or the coordinates are invalid,
                i.e. has_coordinates returns False.
        """
        if type(coordinates) is not tuple:
            coordinates = tuple(coordinates)

        self._check_coordinates(coordinates)

        if not callable(action):
            raise ValueError("Argument action must be a callable object.")

        self._matrix[coordinates] = action

    def set_all_actions(self, coord_action_dict, overwrite=True):
        """
        Stores the actions from dictionary coord_action_dict in the matrix at
        the coordinates with which they are paired. The actions currently stored
        in this instance will remain if they are not overwritten with a new
        action. To delete all the actions stored in this instance, use method
        clear_actions.

        Args:
            coord_action_dict (dictionary): contains actions (values) paired
                with their coordinates (keys) where they must be stored.
                Coordinates must be represented by tuples.
            overwrite (bool, optional): if True, the actions in coord_action_dict
                will overwrite the actions currently stored at their coordinates.
                Defaults to True.

        Raises:
            ValueError: if a key in coord_action_dict is invalid, i.e.
                has_coordinates returns False or if a value in
                coord_action_dict is not a callable object.
        """
        for coordinates, action in coord_action_dict.items():
            if overwrite or self._matrix.get(coordinates) is None:
                self.set_action(coordinates, action)

    def set_default_action(self, action):
        """
        The specified action will be performed if all conditions are false. The
        default action can be set to None if it is not wanted. On instantiation,
        DecisionMatrix does not have a default action. The action will only be
        set as default if it is None or callable.

        Args:
            action: a callable object. Its return value will not be recorded
                or used.

        Raises:
            ValueError: if action is not None and is not a callable object.
        """
        if action is None or callable(action):
            self._default_action = action
        else:
            raise ValueError(
                "The default action must be None or a callable object.")
