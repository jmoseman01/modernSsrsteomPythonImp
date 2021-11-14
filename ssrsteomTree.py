'''
Created on Nov 13, 2021

@author: jmose
'''
from math import factorial
from decimal import Decimal



class ssrsteomTree(object):

    def __init__(self, initial_output_list, start_x_value,delta_x):
        initial_output_list = list(map(Decimal,initial_output_list))
        self.ssrsteomList = []
        
        self.coeffecientList = []
        self.deltax = delta_x 
        self.highestLevel = 0
        self.start_x_value = start_x_value
        
        self.genTree(initial_output_list)

        self.highestDegree = self.highestLevel - 1
        self.coeffecient_of_highest_degree = self.terminatingEntity / (Decimal(self.deltax) ** self.highestDegree * factorial(self.highestDegree))
        
    def genTree(self, ssrsteom_tree_row):
        self.highestLevel+=1
        self.ssrsteomList.append(ssrsteom_tree_row)

        # this is purely to see if there is an the term that iterates itself over and over
        ssrsteom_tree_row_set = set(ssrsteom_tree_row)
        
        if len(ssrsteom_tree_row_set) == 0:
            raise Exception("SSRSTEOM tree row passed is of size 0")
        elif len(ssrsteom_tree_row_set) == 1:
            self.terminatingEntity = ssrsteom_tree_row_set.pop()
        else:
            next_row = []
            for i in range(0, len(ssrsteom_tree_row) - 1):
                difference_quotient = ssrsteom_tree_row[i+1] - ssrsteom_tree_row[i]
                next_row.append(difference_quotient)
            next_row = list(map(Decimal,next_row))
            self.genTree(next_row)
        
    def solve(self, localSsrsteomTree):
        self.coeffecientList.append(localSsrsteomTree.coeffecient_of_highest_degree)
        successive_polynomial_list = []
        
        for i in range(len(localSsrsteomTree.ssrsteomList[0])):
            next_val = localSsrsteomTree.coeffecient_of_highest_degree * Decimal(str(localSsrsteomTree.start_x_value+i*localSsrsteomTree.deltax))**localSsrsteomTree.highestDegree
            successive_polynomial_list.append(localSsrsteomTree.ssrsteomList[0][i] - next_val)
            
        nextDegreeTree = ssrsteomTree(successive_polynomial_list, self.start_x_value, self.deltax)
        degreeDeviation = localSsrsteomTree.highestDegree - nextDegreeTree.highestDegree
        if degreeDeviation > 1:
            for i in range(degreeDeviation - 1):
                self.coeffecientList.append(0)
        if len(localSsrsteomTree.ssrsteomList) > 1:
            self.solve(nextDegreeTree)