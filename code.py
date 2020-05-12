# --------------
import pandas as pd
import numpy as np
import math


#Code starts here

class complex_numbers(object):
    """The complex number class.

    Attributes:
    attr1 (x): Real part of complex number.
    attr2 (y): Imaginary part of complex number.

    """

    def __init__(self, x = 0.00, y = 0.00):
        self.real = x
        self.imag = y

    def __repr__(self):

        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))

    def __add__(self,other):
        """Overloaded '+' operator.

        Args:
        param1 (complex_numbers): Other point.

        Returns:
        complex_numbers: The evaluated complex number.
        """
        x = self.real + other.real
        y = self.imag + other.imag
        return complex_numbers(x,y)

    def __sub__(self, other):
        """Overloaded '-' operator.

        Args:
        param1 (complex_numbers): Other point.

        Returns:
        complex_numbers: The evaluated complex number.

        """
        x = self.real - other.real
        y = self.imag - other.imag
        return complex_numbers(x,y)

    def __mul__(self, other):
        """Overloaded '*' operator.

        Args:
        param1 (complex_numbers): Other point.

        Returns:
        complex_numbers: The evaluated complex number.

        """
        x = self.real * other.real - self.imag * other.imag
        y = self.real * other.imag + self.imag * other.real
        return complex_numbers(x,y)

    def __truediv__(self, other):
        """Overloaded '/' operator.

        Args:
        param1 (complex_numbers): Other point.

        Returns:
        complex_numbers: The evaluated complex number.

        """
        if other.real*other.real + other.imag*other.imag != 0:
            return complex_numbers((self.real*other.real + self.imag*other.imag) / (other.real*other.real + other.imag*other.imag), 
                             (self.imag*other.real - self.real*other.imag) / (other.real*other.real + other.imag*other.imag))
        else:
            return "Denominator is zero."	


    def absolute(self):
        """Returns Absolute value.

        Returns:
        Integer: The evaluated abs value.

        """
        return math.sqrt( self.real * self.real + self.imag * self.imag)


    def argument(self):
        """Returns arguments in degree.

        Returns:
        Float: The evaluated arg in degrees.

        """
        return math.degrees(math.atan(self.imag / self.real))

    def conjugate(self):
        """Returns conjugate of the complex number.

        Returns:
        complex_numbers: The conjugate complex number.

        """
        x = self.real
        y = self.imag * -1
        return complex_numbers(x,y)


    
comp_1 = complex_numbers(3,5)
print('Complex Number 1: ',comp_1)

comp_2 = complex_numbers(4,4)
print('Complex Number 2: ',comp_2)

comp_sum= (comp_1+comp_2)
print('Sum of Complex Number 1 & 2: ', comp_sum)

comp_diff= (comp_1-comp_2)
print('Difference of Complex Number 1 & 2: ',comp_diff)

comp_prod= (comp_1*comp_2)
print('Product of Complex Number 1 & 2: ',comp_prod)

comp_quot= (comp_1/comp_2)
print('Quotient of Complex Number 1 & 2: ',comp_quot)

comp_abs=comp_1.absolute()
print('Absolute value of Complex Number 1: ',comp_abs)

comp_conj= comp_1.conjugate()
print('Conjugate value of Complex Number 1: ',comp_conj)

comp_arg=comp_1.argument()
print('Argument value of Complex Number 1: ',comp_arg) 

#Code ends here


