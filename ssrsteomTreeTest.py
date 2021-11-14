'''
Created on Nov 13, 2021

@author: jmose
'''
import unittest
from ssrsteomTree import ssrsteomTree
from decimal import Decimal


class Test(unittest.TestCase):


    def testSsrstoemTreeConstructionAlternatDeltax(self):
        ssrsteom_tree = ssrsteomTree([Decimal('68.035'),Decimal('94.000'),Decimal('126.625'),Decimal('166.720')], Decimal('1.9'),Decimal('.3'))
        assert ssrsteom_tree.terminatingEntity == Decimal('.810')
        
    def testSrrsteomTreeSolveCoeffecients(self):
        ssrsteom_tree = ssrsteomTree([Decimal('68.035'),Decimal('94.000'),Decimal('126.625'),Decimal('166.720')], Decimal('1.9'),Decimal('.3'))
        ssrsteom_tree.solve(ssrsteom_tree)
        assert ssrsteom_tree.terminatingEntity == Decimal('.810')
        assert ssrsteom_tree.coeffecientList == [Decimal('5'), Decimal('4.0'), Decimal('7.00'), Decimal('6.000')]


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()