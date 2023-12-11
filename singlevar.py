from sympy import symbols, Eq, solve, simplify, tan, sin, cos, log, asin, acos, atan, ln, sympify
import re

def solve_single_variable_equation(equation_str):
    x = symbols('x')

    # Use regex
    equation_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', equation_str)

    if 'tan' in equation_str or 'sin' in equation_str or 'cos' in equation_str or 'log' in equation_str or 'ln' in equation_str:
        try:
            # Replace tan⁻¹ with atan, cos¹ with acos, sin⁻¹ with asin
            equation_str = equation_str.replace("tan⁻¹", "atan").replace("cos¹", "acos").replace("sin⁻¹", "asin")

            equation = Eq(sympify(equation_str), 0)
            solution = solve(equation, x)

            return solution
        except Exception as e:
            return f"Error: {e}"
    else:
        try:
            equation = Eq(eval(equation_str), 0)
            solution = solve(equation, x)

            return solution
        except Exception as e:
            return f"Error: {e}"


