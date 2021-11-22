import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint

"""Решение с помощью SymPy"""
x = Symbol('x')
y = Function('y')
diffeq = Eq(y(x).diff(x), -2 * y(x))
res = dsolve(diffeq, y(x), ics={y(0): sqrt(2)})
evalfunc = lambdify(x, res.rhs, 'numpy')

data_x = np.linspace(0, 10, 1000)
data_y = evalfunc(data_x)

plt.plot(data_x, data_y, linewidth=2, color='red')
plt.title("SymPy")
plt.grid(True)
plt.show()
plt.clf()

"""Решение с помощью Scipy"""


def dy(y, x):
    return -2 * y


y0 = np.sqrt(2)
y = odeint(dy, y0, data_x)
y = np.array(y).flatten()
plt.grid(True)
plt.title("SciPy")
plt.plot(data_x, data_y)
plt.show()

plt.clf()

"""Разность решений SciPy и SymPy"""
plt.plot(data_x, np.abs(data_y - y))
plt.grid(True)
plt.show()