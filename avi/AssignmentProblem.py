from pulp import *
import numpy as np
import pandas as pd

#df=pd.read_csv  ('Q1(data).csv')
#df.head()

nvar = 9
ncons = 6
cost = np.array([120, 100, 80, 80, 90, 110, 110, 140, 120])

Coff = np.array([[1, 1, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 1, 1],
                 [1, 0, 0, 1, 0, 0, 1, 0, 0],
                 [0, 1, 0, 0, 1, 0, 0, 1, 0],
                 [0, 0, 1, 0, 0, 1, 0, 0, 1]])

resources = [1, 1, 1, 1, 1, 1]

print(Coff)

#Define th model
model=LpProblem("LPP",LpMinimize)

#Define the decision variable
x = {i: LpVariable(name=f"x{i}", lowBound=0 , cat='Integer') for i in range(1,nvar+1)}

# Define The objective
model += lpSum(cost[i-1]*x[i] for i in range(1,nvar+1))


#Add Constraints

for j in range(ncons):
  model += lpSum(Coff[j,i-1]*x[i] for i in range(1,nvar+1))==resources[j]

#Print model
print(model)

# Solve the optimization problem
status = model.solve()

# Get the results
print('##############Solution of LPP is #################n\n')
print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")

for var in x.values():
  print(f"{var.name}: {var.value()}")

status = model.solve()
print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")

for var in x.values():
    print(f"{var.name}: {var.value()}")

for var in y.values():
    print(f"{var.name}: {var.value()}")

for var in z.values():
    print(f"{var.name}: {var.value()}")