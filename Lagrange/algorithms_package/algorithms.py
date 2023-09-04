import numpy as np
from .techniques import MathTechniques

class Finders:
    def __init__(self):
        self.iteration = 0
        self.mymath = MathTechniques()

    def clearIteration(self):
        self.iteration = 0
    
    def findLagSq(self, n):
        arr = [0, 0, 0, 0]
        raiz = int(np.floor(np.sqrt(n)))
        i = j = k = l = 0
        while np.sum(arr) != n:
            i += 1
            arr[0] = i**2
            if (i == raiz) and (np.sum(arr) != n):
                i = 0
                j += 1
                arr[0] = i**2
                arr[1] = j**2
                if (j == raiz) and (np.sum(arr) != n):
                    j = 0
                    k += 1
                    arr[1] = j**2
                    arr[2] = k**2
                    if (k == raiz) and (np.sum(arr) != n):
                        k = 0
                        l += 1
                        arr[2] = k**2
                        arr[3] = l**2
            self.iteration += 1
        return arr, self.iteration

    def findLagSq2(self, n, arr=None, index=0):
        if arr is None:
            arr = [0, 0, 0, 0]

        if index == len(arr):
            if np.sum(arr) == n:
                return arr, True, self.iteration
            return arr, False, self.iteration

        raiz = int(np.floor(np.sqrt(n)))
        for i in range(raiz + 1):
            self.iteration += 1
            arr[index] = i ** 2
            result, found, self.iteration = self.findLagSq2(n, arr, index + 1)
            if found:
                return result, True, self.iteration

        return arr, False, self.iteration
    
    def ehrFind(self, n):
        #Precomputation step
        limit = int(np.floor(np.log(n))) 
        primes = self.mymath.get_primes(limit)
        M = np.prod(primes)           
        #Random trials
        s, p = self.genRandomMod(n, M)
        while not self.mymath.is_congruent(s**2, -1, p):
            s, p = self.genRandomMod(n, M)
        #Denouement
        z = self.mymath.ggcd((s + 1j), p)
        #I need gcrd here
        return M

    def genRandomMod(self, n, M):
        k = np.random.randint(1, n**5 + 1)
        while k%2 == 0:
            k = np.random.randint(1, n**5 + 1)
        p = M*n*k - 1
        u = np.random.randint(1, p)
        s = (u**((p-1)/4)%p)
        return s,p


    def MiniTest(self, a,b):
        print(self.ehrFind(100000))
        self.mymath.ggcd(a,b)
        print(self.mymath.is_congruent(0, -1, None))