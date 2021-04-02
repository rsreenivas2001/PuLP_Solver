from pulp import *
import numpy as np
import pandas as pd

df=pd.read_csv('problem1.csv')
#df


nvar=6*6
city=[1,2,3,4,5,6]
dist=df.iloc[0:6,0:6].to_numpy()
print(dist)
dist1 = df.to_numpy()
print(dist1)
cost = dict(((a,b),dist[a-1][b-1]) for a in city for b in city if a!=b)
print(cost)
model=LpProblem("lp",LpMinimize)
x = LpVariable.dicts('x',cost, 0,1,LpBinary)
model+=lpSum([x[(i,j)]*cost[(i,j)] for (i,j) in cost])

for k in city:
    model+= lpSum([ x[(i,k)] for i in city if (i,k) in x]) ==1 ##i to j
    model+=lpSum([ x[(k,i)] for i in city if (k,i) in x]) ==1  ##j to i

z = LpVariable.dicts('z', city, 0, len(city)-1, LpInteger)
for i in city:
    for j in city:
        if i != j and (i != 1 and j!= 1) and (i,j) in x:
            model += z[i] - z[j] <= (6)*(1-x[(i,j)]) - 1
model

status=model.solve(PULP_CBC_CMD(msg=0))

print(f"status: {model.status},{LpStatus[model.status]}")
print(f"Objective= {model.objective.value()}")

for var in x.values():
  print("{}={}".format(var.name,var.value()))

for var in z.values():
      print("{}={}".format(var.name,var.value()))


starting_city = 1
s_route=[]##shortest route
s_route.append(city.pop(0))

while len(city) > 0:

    for k in city:
        if x[(starting_city,k)].varValue ==1:
            s_route.append( city.pop( city.index(k)))
            starting_city=k
            break

s_route.append(1)
print(s_route)
shortest_route_length = [cost[(s_route[i-1], s_route[i])] for i in range(1,len(s_route))]

print('Shortest Path  Travelling by Mr.Iyer :')
flag=True
for cty in s_route:
    if flag:
        print(cty,end='')
        flag = False
    else:
        print(f' -> {cty}',end='')
print(f"\nMinimum cost of the tour for mr.Iyer from his home city to  travel other 5 \
cities with min cost and returning back to its home city :{sum(shortest_route_length)}")