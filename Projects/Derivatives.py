import sympy as sp

# Ask the user for the type of differentiation

print("Choose differentiation type:")
print("1. Explicit (e.g., y = x**2 + 3*x + 5)")
print("2. Parametric (e.g., x = t**2, y = t**3)")
print("3. Implicit (e.g., x**2 + y**2 - 4 = 0)")
choice = input("Enter 1, 2, or 3: ")


if choice == "1":
    # Explicit Differentiation
    expr = input("Enter the function to differentiate (e.g., x**2 + 3*x + 5): ")
    var = input("Enter the variable with respect to which you want to differentiate (e.g., x): ")

    x = sp.symbols(var)
    function = sp.sympify(expr)

    derivative = sp.diff(function, x)
    print(f"The derivative of {expr} with respect to {var} is: {derivative}")

elif choice == "2":
    # Parametric Differentiation
    t = sp.symbols('t')
    x_expr = input("Enter x in terms of t (e.g., t**2): ")
    y_expr = input("Enter y in terms of t (e.g., t**3): ")

    x_func = sp.sympify(x_expr)
    y_func = sp.sympify(y_expr)

    dx_dt = sp.diff(x_func, t)
    dy_dt = sp.diff(y_func, t)

    dydx = dy_dt / dx_dt  # Chain rule dy/dx = (dy/dt) / (dx/dt)

    print(f"dx/dt = {dx_dt}")
    print(f"dy/dt = {dy_dt}")
    print(f"dy/dx = {dydx}")

elif choice == "3":
    # Implicit Differentiation
    expr = input("Enter the implicit equation (e.g., x**2 + y**2 - 4): ")
    
    x, y = sp.symbols('x y')
    function = sp.sympify(expr)

    dydx = sp.diff(function, x).simplify() / (-sp.diff(function, y).simplify())

    print(f"The derivative dy/dx for the implicit function {expr} = 0 is: {dydx}")

else:
    print("Invalid choice! Please enter 1, 2, or 3.")
