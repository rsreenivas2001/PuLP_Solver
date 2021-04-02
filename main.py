import pulp
import pandas as pd
import numpy as np
from utils.transport_utils import *
from utils.assign_utils import *
from utils.tsmp_utils import *


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

    cost = assign_find_cost(data_frame,row, col)
    coeff = assign_find_coeff(row, col)
    resource = assign_find_resource(data_frame,row, col)

    #print(cost,coeff,resource,sep="\n")
    assign_solver(cost, coeff, resource, row, col)


def tsmp():
    data_frame = pd.read_csv('problem1.csv')
    #print(data_frame)
    row, col = data_frame.shape

    print(row,col)
    cost , city = tsmp_find_cost(data_frame,row,col)

    tsmp_solver(cost, city)


def main():
    
    inp = int(input("choice : "))
    if inp == 1:
        transportation()
    elif inp == 2:
        assignment()
    elif inp == 3:
        tsmp()



if __name__ == '__main__':
    main()
    

