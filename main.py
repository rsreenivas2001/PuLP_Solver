import pulp
import pandas as pd
import numpy as np
from utils.transport_utils import *
from utils.assign_utils import *

'''def find_cost(r, c):
    cost_lst = []
    for i in range(0, row-1):
        for j in range(0, col-1):
            cost_lst.append(df[j][i])
    # print(cost_lst)
    cost = np.array(cost_lst)

# pulp.pulpTestAll()

df = pd.read_csv('data.csv', header=None)

row, col = df.shape

print(row, col)

row_ = row - 1
col_ = col - 1

cost_lst = []

for i in range(0, row-1):
    for j in range(0, col-1):
        cost_lst.append(df[j][i])

# print(cost_lst)

cost = np.array(cost_lst)

print(cost)


var_count = (row_)*(col_)
cons_count = row_ + col_

# print(type(row))
# print(type(col))

coeff_lst = []

count = int(var_count)
for i in range(0, cons_count):
    r = [0] * var_count
    # print(r)
    coeff_lst.append(r)

# print(coeff_lst)


buff = 0
for i in range(0, row_):
    for j in range(0, col_):
        coeff_lst[i][j + buff] = 1
    buff += col_

buff = 0
for i in range(row_, cons_count):
    for j in range(0, var_count, col_):
        coeff_lst[i][j + buff] = 1
    buff += 1

# print(coeff_lst)

coeff = np.array(coeff_lst)

print(coeff)

resource_lst = []

for i in range(0, row_):
    resource_lst.append(df[col_][i])

for j in range(0, col_):
    resource_lst.append(df[j][row_])

# print(resource_lst)

resource = np.array(resource_lst)

print(resource)
'''
def transportation():
    data_frame = pd.read_csv('data.csv', header=None)

    row, col = data_frame.shape

    print(row, col)

    cost = transport_find_cost(data_frame,row, col)
    coeff = transport_find_coeff(row, col)
    resource = transport_find_resource(data_frame,row, col)

    #print(a,b,c,sep="\n")
    transport_solver(cost, coeff, resource, row, col)


def assignment():
    data_frame = pd.read_csv('data2.csv', header=None)

    row, col = data_frame.shape

    print(row, col)

    a = assign_find_cost(data_frame,row, col)
    b = assign_find_coeff(row, col)
    c = assign_find_resource(data_frame,row, col)

    print(a,b,c,sep="\n")


def main():
    
    inp = int(input("choice : "))
    if inp == 1:
        transportation()
    else:
        assignment()


if __name__ == '__main__':
    main()
    

