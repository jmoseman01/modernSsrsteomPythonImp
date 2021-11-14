# SSRSTEOM - Sequential Successive Recursive Subtraction Termination Entities of Monomials
 
 This is using my horizontal algorithm which takes subtract initial output lists recursively to solve for coeffecients in polynomial.
 
 Here's documentation examples on the math behind the horizontal algorithm that's implemented here: https://drive.google.com/drive/folders/1xQZA5DM8crRrsOfFwnksZ4EK5YTWpsDV?usp=sharing
 

# How to use ssrsteomTree.py

First construct an SsrsteomTree. 
1. The first argument is a list of output values.
2. The second argument is the starting x value
3. The thrid argument is the deltax between input values which is static.

You can then assign it to a reference and run the solve method.
This will populate the coeffecient list of that object.


```python
from ssrsteom import SsrsteomTree
from decimal import Decimal
ssrsteom_tree = ssrsteomTree([Decimal('68.035'),Decimal('94.000'),Decimal('126.625'),Decimal('166.720')], Decimal('1.9'),Decimal('.3'))
ssrsteom_tree.solve(ssrsteom_tree)
ssrsteom_tree.coeffecientList # this will output the coeffecients that hit the points above 
# [Decimal('5'), Decimal('4.0'), Decimal('7.00'), Decimal('6.000')]
# This represents the polynomial 5x^3 + 4x^2 + 7x + 6 
```
