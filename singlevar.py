from sympy import symbols, Eq, solve, simplify
import re

def solve_single_variable_equation(equation_str):
    x = symbols('x')

    # Use regex
    equation_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', equation_str)

    try:
        equation = Eq(simplify(equation_str), 0)
        solution = solve(equation, x)

        return solution
    except Exception as e:
        return f"Error: {e}"
