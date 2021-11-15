'''
Created on Nov 13, 2021

@author: jmose
'''
from math import factorial
from decimal import Decimal
import numpy as np
from numpy import dtype



class SsrsteomTree(object):

    def __init__(self, initial_output_list, start_x_value, delta_x):
        initial_output_list = list(map(Decimal, initial_output_list))
        self.ssrsteomList = []
        self.coeffecientList = []
        self.deltax = delta_x
        self.highest_level = 0
        self.start_x_value = start_x_value

        self.genTree(initial_output_list)

        # gen tree must run to create these values
        self.highest_degree = self.highest_level - 1
        self.coeffecient_of_highest_degree = self.terminatingEntity / \
            (Decimal(self.deltax) ** self.highest_degree *
             factorial(self.highest_degree))
        self.initialListLength = len(self.ssrsteomList[0])

    def genTree(self, ssrsteom_tree_row):
        self.highest_level += 1
        self.ssrsteomList.append(ssrsteom_tree_row)

        # this is purely to see if there is an the term that iterates itself
        # over and over
        ssrsteom_tree_row_set = set(ssrsteom_tree_row)

        if len(ssrsteom_tree_row_set) == 0:
            raise Exception("SSRSTEOM tree row passed is of size 0")
        elif len(ssrsteom_tree_row_set) == 1:
            self.terminatingEntity = ssrsteom_tree_row_set.pop()
        else:
            next_row = []
            for i in range(0, len(ssrsteom_tree_row) - 1):
                difference_quotient = ssrsteom_tree_row[i +
                                                        1] - ssrsteom_tree_row[i]
                next_row.append(difference_quotient)
            next_row = list(map(Decimal, next_row))
            self.genTree(next_row)

    def solve(self, runningSsrsteomTree):
        # add running ssrsteomTree highest coeffecient to list
        self.coeffecientList.append(
            runningSsrsteomTree.coeffecient_of_highest_degree)
        
        monomialFunc = lambda x: runningSsrsteomTree.coeffecient_of_highest_degree * \
            Decimal(str(x))**runningSsrsteomTree.highest_degree

        output_list_of_running = np.array(runningSsrsteomTree.ssrsteomList[0])
        highest_monomial_output_list = np.array([monomialFunc(self.start_x_value + x * self.deltax)  for x  in range(self.initialListLength)], dtype=np.dtype(Decimal))
        
        successive_polynomial_list = np.subtract(output_list_of_running, highest_monomial_output_list);

        nextDegreeTree = SsrsteomTree(
            successive_polynomial_list,
            self.start_x_value,
            self.deltax)
        
        # this checks whether your degree deviation jumped more than one
        # meaning that you have 0's for coeffecients on successive degrees
        degreeDeviation = runningSsrsteomTree.highest_degree - nextDegreeTree.highest_degree
        if degreeDeviation > 1:
            for i in range(degreeDeviation - 1):
                self.coeffecientList.append(0)
        if len(runningSsrsteomTree.ssrsteomList) > 1:
            self.solve(nextDegreeTree)
