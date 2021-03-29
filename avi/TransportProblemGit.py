from pulp import *
import pandas as pd
import numpy as np
import math
source = input('Enter the no.of sources : ')
destination = input('Enter the no.of destinations : ')
nvar = int(source) * int(destination)
ncons= int(source) + int(destination)
#cost = np.zeros((nvar),dtype=int)
#for i in range(nvar):
#    print('Cost for source-',math.floor(i/int(source))+1,' destination-',(i%int(destination))+1)
#    cost[i]=input()
cost= np.array([5,2,4,3,4,8,1,6,4,6,7,5])

Coff=np.array([[1,1,1,1,0,0,0,0,0,0,0,0],
               [0,0,0,0,1,1,1,1,0,0,0,0],
               [0,0,0,0,0,0,0,0,1,1,1,1],
               [1,0,0,0,1,0,0,0,1,0,0,0],
               [0,1,0,0,0,1,0,0,0,1,0,0],
               [0,0,1,0,0,0,1,0,0,0,1,0],
               [0,0,0,1,0,0,0,1,0,0,0,1]])

#resources = np.zeros((ncons),dtype=int)

resources=[22,15,8,7,12,17,9]
'''for i in range(int(source)):
    print('Supply from source-',i+1)
    resources[i]=input()

for i in range(int(source),int(source)+int(destination)):
    print('Supply from source-',i+1)
    resources[i]=input()'''
#Define th model
model=LpProblem("LPP",LpMinimize)

#Define the decision variable
x = {i: LpVariable(name=f"x{i}", lowBound=0) for i in range(1,nvar+1)}

# Define The objective
model += lpSum(cost[i-1]*x[i] for i in range(1,nvar+1))


#Add Constraints

for j in range(ncons):
  model += lpSum(Coff[j,i-1]*x[i] for i in range(1,nvar+1))==resources[j]

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