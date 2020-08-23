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
            # Deep copies are created.
            submatrix = [submatrix for x in range(axis_length)]

        self._matrix = submatrix

    def get_axis_count(self):
        return self._axis_count

    def run(self):
        self._run_submatrix(0, 0)

    def _run_submatrix(self, axis, coordinate):
        if self._axes[axis][coordinate]():
            pass
        if coordinate < len(self._axes[axis])-1:
            self._run_submatrix(axis, coordinate+1)
        elif axis < self._axis_count-1:
            self._run_submatrix(axis+1, 0)

    def set_action(self, action, *coordinates):
        submatrix = self._matrix

        index = LoopIndex(len(coordinates)-1)
        while index.iterate():
            i = index.get_value()
            submatrix = submatrix[i]

        submatrix[coordinates[self._axis_count-1]] = action
