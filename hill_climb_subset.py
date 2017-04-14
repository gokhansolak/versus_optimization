
import objective_function as objective
import random
import copy

# create an initial solution
current_solution = []

# assign random int between 0, 100
for i in range(3):
    x = random.randint(0, 100)
    current_solution.append(x)

current_evaluation = objective.eval(current_solution)

terminate = False

while not terminate:

    # generate and evaluate the neighborhood
    neighbors = []

    for i in range(3):
        n1 = copy.copy(current_solution)
        n1[i] += 1

        n1_eval = objective.eval(n1)

        n1_dict = {'solution': n1,
                   'evaluation': n1_eval}

        neighbors.append(n1_dict)

        n2 = copy.copy(current_solution)
        n2[i] -= 1

        n2_eval = objective.eval(n2)

        n2_dict = {'solution': n2,
                   'evaluation': n2_eval}

        neighbors.append(n2_dict)

    # choose the best neighbor
    best = {'solution': current_solution, 'evaluation': current_evaluation}

    random.shuffle(neighbors)
    for n in neighbors:
        if n['evaluation'] > best['evaluation']:
            best = n
            break

    # no improvement?
    if best['evaluation'] <= current_evaluation:
        terminate = True
    else:
        current_solution = best['solution']
        current_evaluation = best['evaluation']

print('solution:' + str(current_solution))
print('evaluation:' + str(current_evaluation))