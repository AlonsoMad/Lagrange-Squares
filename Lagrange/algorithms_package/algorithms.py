import numpy as np

class finders:
    def __init__(self):
        self.iteration = 0

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
                arr[1] = j**2
                if (j == raiz) and (np.sum(arr) != n):
                    j = 0
                    k += 1
                    arr[2] = k**2
                    if (k == raiz) and (np.sum(arr) != n):
                        k = 0
                        l += 1
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
            arr[index] = i ** 2
            result, found, self.iteration = self.findLagSq2(n, arr, index + 1)
            if found:
                return result, True, self.iteration

        return arr, False, self.iteration