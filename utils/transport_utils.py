import numpy as np
from pulp import *

def transport_find_cost(df,r, c):
    cost_lst = []
    row = r-1
    col = c-1
    for i in range(0, row):
        for j in range(0, col):
            cost_lst.append(df[j][i])
    
    # print(cost_lst)
    cost = np.array(cost_lst)
    return cost


def transport_find_coeff(r,c):
    coeff_lst = []
    row = r-1
    col = c-1
    var_count = (row)*(col)
    cons_count = row + col
    
    for i in range(0, cons_count):
        r = [0] * var_count
        # print(r)
        coeff_lst.append(r)

    buff = 0
    for i in range(0, row):
        for j in range(0, col):
            coeff_lst[i][j + buff] = 1
        buff += 4

    buff = 0
    for i in range(row, cons_count):
        for j in range(0, var_count, 4):
            coeff_lst[i][j + buff] = 1
        buff += 1

    # print(coeff_lst)
    coeff = np.array(coeff_lst)
    return coeff


def transport_find_resource(df,r,c):
    resource_lst = []
    row_ = r-1
    col_ = c-1
    for i in range(0, row_):
        resource_lst.append(df[col_][i])

    for j in range(0, col_):
        resource_lst.append(df[j][row_])

    # print(resource_lst)

    resource = np.array(resource_lst)

    return resource


def transport_solver(cost,coeff,resources,r,c):
    model=LpProblem("LPP",LpMinimize)

    row = r-1
    col = c-1
    var_count = (row)*(col)
    cons_count = row + col 
    #Define the decision variable
    x = {i: LpVariable(name=f"x{i}", lowBound=0) for i in range(1,var_count+1)}

    # Define The objective
    model += lpSum(cost[i-1]*x[i] for i in range(1,var_count+1))
    #Add Constraints
    for j in range(cons_count):
        model += lpSum(coeff[j,i-1]*x[i] for i in range(1,var_count+1))==resources[j]
    #Print model
    print(model)
    # Solve the optimization problem
    status = model.solve(PULP_CBC_CMD(msg=0))
    # Get the results
    print('##############Solution of LPP is #################n\n')
    print(f"status: {model.status}, {LpStatus[model.status]}")
    print(f"objective: {model.objective.value()}")

    for var in x.values():
        print(f"{var.name}: {var.value()}")