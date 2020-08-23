# -*- coding: utf-8 -*-

from decision_matrix import DecisionMatrix

DEG_C = "C"
DEG_F = "F"
KELVIN = "K"

input_temp = 23
output_temp = input_temp

def convert_c_to_f():
    print("Converting °C to °F")
    output_temp = input_temp * 9 / 5 + 32

def convert_c_to_k():
    print("Converting °C to K")
    output_temp = input_temp + 273.15

def convert_f_to_c():
    print("Converting °F to °C")
    output_temp = (input_temp - 32) * 5 / 9

def convert_f_to_k():
    print("Converting °F to K")
    output_temp = (input_temp + 459.67) * 5 / 9

def convert_k_to_c():
    print("Converting K to °C")
    output_temp = input_temp - 273.15

def convert_k_to_f():
    print("Converting K to °F")
    output_temp = input_temp * 9 / 5 - 459.67

input_scale = "C"
output_scale = "F"

input_scale_axis = [
    lambda: input_scale == DEG_C,
    lambda: input_scale == DEG_F,
    lambda: input_scale == KELVIN]
output_scale_axis = [
    lambda: output_scale == DEG_C,
    lambda: output_scale == DEG_F,
    lambda: output_scale == KELVIN]

dm = DecisionMatrix(input_scale_axis, output_scale_axis)

dm.set_action(convert_c_to_f, 0, 1)
dm.set_action(convert_c_to_k, 0, 2)
dm.set_action(convert_f_to_c, 1, 0)
dm.set_action(convert_f_to_k, 1, 2)
dm.set_action(convert_k_to_c, 2, 0)
dm.set_action(convert_k_to_f, 2, 1)

dm.run()
