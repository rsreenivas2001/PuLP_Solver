import numpy as np

def assign_find_cost(df,r, c):
    cost_lst = []
    row = r
    col = c
    for i in range(0, row):
        for j in range(0, col):
            cost_lst.append(df[j][i])

    # print(cost_lst)

    cost = np.array(cost_lst)

    return cost


def assign_find_coeff(r,c):
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


def assign_find_resource(df,r,c):
    resource_lst = []
    
    var_count = r*c
    cons_count = r + c
    resource_lst.append([1] * cons_count)

    # print(resource_lst)

    resource = np.array(resource_lst)

    return resource