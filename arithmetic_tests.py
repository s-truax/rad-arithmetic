# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 21:12:14 2019

@author: sam
"""

from arithmetic import Arithmetic

dodecimal = ['0',
             '1',
             '2',
             '3',
             '4',
             '5',
             '6',
             '7',
             '8',
             '9',
             'X',
             'Y']

twelves = Arithmetic(dodecimal)
print(twelves.to_radix(24))
print(twelves.add('1', '9'))
print(twelves.to_base10('11'))