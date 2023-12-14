import numpy as np
import math


class MathTechniques:
    
    def is_congruent(self, a, b, mod):
        res = True if ((a-b)%mod == 0) else False
        return res


    def ggcd(self, a, b):
        if(b == 0):
            a = abs(a.real) + abs(a.imag) * 1j
            if a.imag == 0j:
                a = int(a.real)
            return a
        else:
            x = a if abs(a) > abs(b) else b
            y = b if abs(a) > abs(b) else a
            q = x/y
            q = complex(round(np.real(q)), round(np.imag(q))) #Rounds to next int from .5
            r = x - y*q
            self.ggcd(b, r)

    def gdrc(self, a, b):
        print(5)
