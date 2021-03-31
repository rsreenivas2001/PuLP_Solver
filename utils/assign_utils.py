import numpy as np
from pulp import *

def assign_find_cost(df, r, c):
    cost_lst = []
    row = r
    col = c
    for i in range(0, row):
        for j in range(0, col):
            cost_lst.append(df[j][i])

    # print(cost_lst)

    cost = np.array(cost_lst)

    return cost


def assign_find_coeff(r, c):
    coeff_lst = []

    row = r
    col = c
    var_count = (row)*(col)
    cons_count = row + col

    count = int(var_count)
    for i in range(0, cons_count):
        rw = [0] * var_count
        # print(r)
        coeff_lst.append(rw)

    # print(coeff_lst)

    buff = 0
    for i in range(0, row):
        for j in range(0, col):
            coeff_lst[i][j + buff] = 1
        buff += col

    buff = 0
    for i in range(row, cons_count):
        for j in range(0, var_count, col):
            coeff_lst[i][j + buff] = 1
        buff += 1

    # print(coeff_lst)

    coeff = np.array(coeff_lst)

    return coeff


def assign_find_resource(df, r, c):
    
    var_count = r*c
    cons_count = r + c
    resource_lst = ([1] * cons_count)

    # print(resource_lst)

    resource = np.array(resource_lst)

    return resource


def assign_solver(cost, coeff, resources, r, c):
    # Define the model
    model = LpProblem("LPP", LpMinimize)

    var_count = r * c
    cons_count = r + c
    print(var_count, cons_count)
    # Define the decision variable
    x = {i: LpVariable(name=f"x{i}", lowBound=0, cat='Integer') for i in range(1, var_count+1)}

    # Define The objective
    model += lpSum(cost[i-1]*x[i] for i in range(1, var_count+1))

    # Add Constraints
    for j in range(cons_count):
        model += lpSum( coeff[j, i-1] * x[i] for i in range(1, var_count+1)) == resources[j]

    # Print model
    print(model)

    # Solve the optimization problem
    status = model.solve(PULP_CBC_CMD(msg=False))

    # Get the results
    print('##############Solution of LPP is #################n\n')
    print(f"status: {model.status}, {LpStatus[model.status]}")
    print(f"objective: {model.objective.value()}")

    for var in x.values():
        print(f"{var.name}: {var.value()}")


