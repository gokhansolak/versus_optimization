
import math

"""
   h1 function is a slight modification of h1 function from DEAP library.
   See https://github.com/DEAP/deap
"""


def eval(sol):
    # map to 2 dimensions
    sol_new = [(sol[0] + sol[1]), sol[2]]
    # map to -25 25
    sol_new[0] = (sol_new[0] / 200 * 50) - 25
    sol_new[1] = (sol_new[1] / 100 * 50) - 25
    # calc objective function
    return _h1(sol_new) * 100


def _h1(individual):
    num = (math.sin(individual[0] - individual[1] / 8))**2 + (math.sin(individual[1] + individual[0] / 8))**2
    denum = ((individual[0] - 4)**2 + (individual[1] - 2)**2)**0.5 + 1
    return num / denum