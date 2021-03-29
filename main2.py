import pulp
import pandas as pd
import numpy as np




# pulp.pulpTestAll()

df = pd.read_csv('data2.csv', header=None)

row, col = df.shape

print(row, col)

row_ = row
col_ = col

cost_lst = []

for i in range(0, row):
    for j in range(0, col):
        cost_lst.append(df[j][i])

# print(cost_lst)

cost = np.array(cost_lst)

print(cost)


var_count = (row)*(col)
cons_count = row + col

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

print(coeff)

resource_lst = []

resource_lst.append([1] * cons_count)

# print(resource_lst)

resource = np.array(resource_lst)

print(resource)
