from copy import deepcopy
from loop_index.loop_index import LoopIndex

class DecisionMatrix:

    def __init__(self, *condition_axes):
        self._build_axes(condition_axes)
        self._build_matrix()

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
            axis_length = len(self._axes[i])
            submatrix = [deepcopy(submatrix) for x in range(axis_length)]

        self._matrix = submatrix

    def get_axis_count(self):
        return self._axis_count

    def print_axis_values(self):
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
        self._run_submatrix(0, self._matrix)

    def _run_submatrix(self, axis, submatrix):
        index = LoopIndex(len(submatrix))
        while index.iterate():
            i = index.get_value()

            if self._axes[axis][i]():
                next_axis = axis + 1
                subsub = submatrix[i]

                if callable(subsub):
                    subsub()
                elif subsub is not None and next_axis<self._axis_count:
                    self._run_submatrix(next_axis, subsub)

    def set_action(self, action, *coordinates):
        submatrix = self._matrix

        coord_index = LoopIndex(len(coordinates)-1)
        while coord_index.iterate():
            i = coord_index.get_value()
            coordinate = coordinates[i]
            submatrix = submatrix[coordinate]

        submatrix[coordinates[self._axis_count-1]] = action
