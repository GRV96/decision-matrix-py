# -*- coding: utf-8 -*-

from decision_matrix import DecisionMatrix
from math import isnan, nan

class TempConverter:

    def __init__(self, temp_to_convert):
        self.set_temp_to_convert(temp_to_convert)
        self._result = nan

    def convert_c_to_f(self):
        print("Converting °C to °F")
        self._result = self._temp_to_convert * 9 / 5 + 32

    def convert_c_to_k(self):
        print("Converting °C to K")
        self._result = self._temp_to_convert + 273.15

    def convert_f_to_c(self):
        print("Converting °F to °C")
        self._result = (self._temp_to_convert - 32) * 5 / 9

    def convert_f_to_k(self):
        print("Converting °F to K")
        self._result = (self._temp_to_convert + 459.67) * 5 / 9

    def convert_k_to_c(self):
        print("Converting K to °C")
        self._result = self._temp_to_convert - 273.15

    def convert_k_to_f(self):
        print("Converting K to °F")
        self._result = self._temp_to_convert * 9 / 5 - 459.67

    def get_result(self):
        return self._result

    def set_temp_to_convert(self, temp_to_convert):
        self._temp_to_convert = temp_to_convert

input_temp = 23
converter = TempConverter(input_temp)

DEG_C = "C"
DEG_F = "F"
KELVIN = "K"

input_scale = "F"
output_scale = "K"

input_scale_axis = [
    lambda: input_scale == DEG_C,
    lambda: input_scale == DEG_F,
    lambda: input_scale == KELVIN]
output_scale_axis = [
    lambda: output_scale == DEG_C,
    lambda: output_scale == DEG_F,
    lambda: output_scale == KELVIN]

dm = DecisionMatrix(input_scale_axis, output_scale_axis)

dm.set_action(converter.convert_c_to_f, 0, 1)
dm.set_action(converter.convert_c_to_k, 0, 2)
dm.set_action(converter.convert_f_to_c, 1, 0)
dm.set_action(converter.convert_f_to_k, 1, 2)
dm.set_action(converter.convert_k_to_c, 2, 0)
dm.set_action(converter.convert_k_to_f, 2, 1)

dm.print_axis_values()
dm.run()

output_temp = converter.get_result()
if isnan(converter.get_result()):
    output_temp = input_temp

print(output_temp)
