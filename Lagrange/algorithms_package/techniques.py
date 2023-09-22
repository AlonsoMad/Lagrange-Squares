import numpy as np
import math

class MathTechniques:

    def __init__(self):
        primes = []

    def get_primes(self, n): #Eventually change into Atkin's sieve, now is Erathostenes'
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        p = 2
        while p**2 <= n:
            if is_prime[p]:
                for i in range(p**2, n + 1, p):
                    is_prime[i] = False
            p += 1

        primes = [i for i, prime in enumerate(is_prime) if prime]

        return primes
    
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
            r = a - b*q
            self.ggcd(b, r)

    def gdrc(self, a, b):
        print(5)
