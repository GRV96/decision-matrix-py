# decision_matrix_py

Classes DecisonMatrix and BinaryDecisionMatrix can be used to start the
appropriate processes in a situation comprising definite parameters.

### Definitions

**Action**: a callable object stored in the DecisonMatrix. Any value returned by
an action will not be recorded or used.

**Condition**: a callable object that compares a parameter to one of its possible
values. It returns True if the parameter matches the given value or False otherwise.

**Parameter**: a data characterizing the situation in which the DecisonMatrix
is used.

**Tuplist**: any object whose type is list or tuple.

### Principle

Each axis of a DecisonMatrix represents a parameter. It consists of a tuplist
that should contain one condition for every possible value of the parameter.
The DecisonMatrix receives its axes through its constructor. They cannot be
modified after the instantiation. The size of an axis must be 1 or more.
A DecisonMatrix must have at least one axis.

Coordinates in the matrix represent a set of parameter values. In other words,
coordinates are indices identifying conditions on their axis. They can therefore
be used to determine whether the parameters have certain values. Coordinates are
true if all the conditions to which they correspond are true.

DecisonMatrix contains actions at definite coordinates. When the matrix is run,
the actions whose coordinates are true are invoked. After DecisonMatrix is
instantiated, the actions can be set all together with method set_all_actions
or individually with method set_action. The former takes a dictionary associating
coordinates to an action and erases all previously set actions. The latter takes
an action and its coordinates.

BinaryDecisionMatrix is a subclass of DecisonMatrix. It is designed for situations
whose parameters are boolean. Instead of axes, its constructor takes individual
conditions. BinaryDecisionMatrix does not work with axes actually, but simulates
axes of length 2 using these conditions. If a condition is true, coordinates 0
and 1 of the corresponding axis are false and true respectively. If a condition
is false, it is the opposite. Thus, the coordinates of a BinaryDecisionMatrix
can only be 0 or 1 and represent the boolean value of their simulated axis.