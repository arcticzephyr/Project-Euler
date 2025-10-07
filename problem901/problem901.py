#The Well Drilling problem

#Not working

from scipy import optimize 
import numpy as np

N = 15
epsilon = 0.000000000000001

def f(x):
    sum = x[0]
    for i in range(N-1):
        sum += np.exp(-x[i])*x[i+1]
    return sum

cons = [
    {'type': 'ineq', 'fun': lambda v, i=i: v[i + 1] - v[i] - epsilon}
    for i in range(N - 1)
]

cons += [
    {'type': 'ineq', 'fun': lambda v, i=i: v[i] - epsilon}
    for i in range(N)
]

result = optimize.minimize(f, np.linspace(1e-3, 10, N), constraints = cons)
print(result.x)
print(result.fun)