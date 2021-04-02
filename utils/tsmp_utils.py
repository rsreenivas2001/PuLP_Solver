import numpy as np
from pulp import *


def tsmp_find_cost(df, r, c):
    values = df.to_numpy()
    city = []
    for i in range(1,c+1):
        city.append(i)
    print(city)
    cost = dict(((a,b),values[a-1][b-1]) for a in city for b in city if a!=b)

    return cost , city


def tsmp_solver(cost, city):
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
    tsmp_answer(x, city, cost)



def tsmp_answer(x, city, cost):

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

    print('Shortest Path Travelling :')
    flag=True
    for cty in s_route:
        if flag:
            print(cty,end='')
            flag = False
        else:
            print(f' -> {cty}',end='')
    print(f"\nMinimum cost of the tour [StartNode -> All other nodes -> StartNode] : {sum(shortest_route_length)}")