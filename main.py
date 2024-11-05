import math
from decimal import Decimal
class Equation(object):
    def __init__(self, left_side, right_side):
        self.left_side = left_side
        self.right_side = right_side

def append_decimal(starting_number, number_to_append, zeros_for_append_number):
    proper_number_to_append = number_to_append / (10 ** zeros_for_append_number)
    final_value = starting_number + proper_number_to_append
    return final_value

def equation_solver(equation):
    if equation.left_side is None or equation.left_side == "":
        print("Left Side is empty")
        return
    if equation.right_side is None or equation.right_side == "":
        print("Right Side is empty")
        return

    variable = 0.0
    increment = 0.1
    equation_solved = False

    # Used to prevent over running
    max_times_ran = 100000
    current_times_ran = 0

    while not equation_solved:
        if isinstance(equation.left_side, str) and "x" in equation.left_side:
            solved_left_side = equation.left_side.replace("x", "(" + str(variable) + ")")
            solved_left_side = solved_left_side.replace("e", str(math.e))

        try:
            left_value = eval(solved_left_side)
        except Exception as e:
            print(f"Error evaluating equation: {e}")
            return

        if left_value > Decimal(equation.right_side):
            variable -= increment
            increment /= 10
            print("New Variable: " + str(variable))
        elif left_value < Decimal(equation.right_side):
            variable += increment
        else:
            print("Solved Variable: " + str(variable))
            equation_solved = True

        if  current_times_ran >= max_times_ran:
            print("Stopping to avoid infinite loop.")
            break

        current_times_ran += 1

equation = Equation("x * math.e**x", "2")
equation_solver(equation)

equation = Equation("math.sin(x)", "0.5")
equation_solver(equation)

#double_check_answer = .8526055020137255 * math.e ** .8526055020137255
#print("Double Check: " + str(double_check_answer))
