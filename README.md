# modernSsrsteomPythonImp

# How to use ssrsteomTree.py

First construct an ssrsteom_tree. 
The first argument is a list of output values.
The second argument is the starting x value
The thrid argument is the deltax between input values which is static.

You can then assign it to a reference and run the solve method.
This will populate the coeffecient list of that object.


```python
# the first argument is the 
ssrsteom_tree = ssrsteomTree([Decimal('68.035'),Decimal('94.000'),Decimal('126.625'),Decimal('166.720')], Decimal('1.9'),Decimal('.3'))
ssrsteom_tree.solve(ssrsteom_tree)
ssrsteom_tree.coeffecientList # this will output the coeffecients that hit the points above 
# [Decimal('5'), Decimal('4.0'), Decimal('7.00'), Decimal('6.000')]
# This represents the polynomial 5x^3 + 4x^2 + 7x + 6 
```
