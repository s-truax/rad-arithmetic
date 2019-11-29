# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 21:00:40 2019

@author: sam
"""

class Arithmetic():
    def __init__(self, digits, adder=lambda x, y: x+y, multiplier=lambda x, y: x*y):
        self.to_digit = {}
        self.to_value = {}
        count = 0
        for char in digits:
            self.to_digit[count] = char
            self.to_value[char] = count
            count += 1
        self.adder = adder
        self.multiplier = multiplier
        self.radix = len(digits)
    
    def add(self, x, y):
        val_x = self.to_value[x]
        val_y = self.to_value[y]
        summation = self.adder(val_x, val_y)
        return self.to_radix(summation)
    
    def mul(self, x, y):
        val_x = self.to_value[x]
        val_y = self.to_value[y]
        product = self.multiplier(val_x, val_y)
        return self.to_radix(product)
    
    def to_radix(self, number):
        """Convert a base 10 NUMBER to the base (radix) of this arithmethic
        object.
        """
        if number < self.radix:
            return self.to_digit[number]
        else:
            remainder = number % self.radix
            quotient = number // self.radix
            return self.to_radix(quotient) + self.to_digit[remainder]
    # TODO:
    def to_base10(self, number_str):
        """Convert a string representing a radix number to a base 10 
        integer.
        """
        raise Exception("This method is not implemented")
        


