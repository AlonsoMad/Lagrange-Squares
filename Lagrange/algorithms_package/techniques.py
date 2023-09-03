import numpy as np
import math

class MathTechniques:

    def __init__(self):
        primes = []

    def get_primes(self, n):
        print('primmes')
    
    def ggcd(self, a, b):
        if(b == 0):
            a = abs(a.real) + abs(a.imag) * 1j
            if a.imag == 0j:
                a = int(a.real)
            print(a)
            return a
        else:
            x = a if abs(a) > abs(b) else b
            y = b if abs(a) > abs(b) else a
            q = x/y
            q = complex(round(np.real(q)), round(np.imag(q)))
            r = a - b*q
            self.ggcd(b, r)

    def gdrc(self, a, b):
        print(5)
