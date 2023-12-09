from sympy import symbols, Eq, solve, simplify

def solve_single_variable_equation(equation_str):

    x = symbols('x')

    try:
        # Parse the input equation
        equation = Eq(simplify(equation_str), 0)

        # Solve the equation for x
        solution = solve(equation, x)

        return solution
    except Exception as e:
        return f"Error: {e}"