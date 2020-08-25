# -*- coding: utf-8 -*-

from decision_matrix import DecisionMatrix
from os import system

if __name__ != "__main__":
    exit(0)

exponent = input("Enter an integral exponent: ")
exponent = int(exponent)

exponent_axis = [lambda: exponent == 24,
                 lambda: exponent == 21,
                 lambda: exponent == 18,
                 lambda: exponent == 15,
                 lambda: exponent == 12,
                 lambda: exponent == 9,
                 lambda: exponent == 6,
                 lambda: exponent == 3,
                 lambda: exponent == 2,
                 lambda: exponent == 1,
                 lambda: exponent == -1,
                 lambda: exponent == -2,
                 lambda: exponent == -3,
                 lambda: exponent == -6,
                 lambda: exponent == -9,
                 lambda: exponent == -12,
                 lambda: exponent == -15,
                 lambda: exponent == -18,
                 lambda: exponent == -21,
                 lambda: exponent == -24]

def print_prefix(prefix, symbol):
    if prefix is None or symbol is None:
        print("The SI does not have a prefix for 10^{}."
              .format(exponent))
    else:
        print("The SI prefix for 10^{} is \"{}\" ({})."
              .format(exponent, prefix, symbol))

dm = DecisionMatrix(exponent_axis)
dm.set_all_actions({(0,): lambda: print_prefix("yotta", "Y"),
                    (1,): lambda: print_prefix("zetta", "Z"),
                    (2,): lambda: print_prefix("exa", "E"),
                    (3,): lambda: print_prefix("peta", "P"),
                    (4,): lambda: print_prefix("tera", "T"),
                    (5,): lambda: print_prefix("giga", "G"),
                    (6,): lambda: print_prefix("mega", "M"),
                    (7,): lambda: print_prefix("kilo", "k"),
                    (8,): lambda: print_prefix("hecto", "h"),
                    (9,): lambda: print_prefix("deca", "da"),
                    (10,): lambda: print_prefix("deci", "d"),
                    (11,): lambda: print_prefix("centi", "c"),
                    (12,): lambda: print_prefix("milli", "m"),
                    (13,): lambda: print_prefix("micro", "µ"),
                    (14,): lambda: print_prefix("nano", "n"),
                    (15,): lambda: print_prefix("pico", "p"),
                    (16,): lambda: print_prefix("femto", "f"),
                    (17,): lambda: print_prefix("atto", "a"),
                    (18,): lambda: print_prefix("zepto", "z"),
                    (19,): lambda: print_prefix("yocto", "y")})
dm.set_default_action(lambda: print_prefix(None, None))
dm.print_axis_values()
dm.run()

system("pause")
