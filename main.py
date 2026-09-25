# Build a Graphing Calculator - FCC College Algebra with Python
import numpy as np

def evaluate(expr, x):
    allowed = {'x': x}
    return eval(expr, {"__builtins__": {}}, {**allowed, 'abs': abs, 'sin': np.sin, 'cos': np.cos, 'tan': np.tan, 'sqrt': np.sqrt, 'log': np.log, 'exp': np.exp, 'pi': np.pi, 'e': np.e})

def make_table(expr, x_min, x_max, points=11):
    xs = np.linspace(x_min, x_max, points)
    rows = []
    for x in xs:
        try:
            rows.append((round(float(x), 3), round(float(evaluate(expr, x)), 3)))
        except Exception:
            rows.append((round(float(x), 3), None))
    return rows

if __name__ == '__main__':
    for row in make_table('x**2 - 4', -3, 3, 7):
        print(row)
