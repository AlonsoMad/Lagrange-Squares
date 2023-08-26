import numpy as np
from matplotlib import pyplot as plt

class tests:
    def __init__(self):
        self.repetitions = 100#How manny times the test will be repeated
        self.size = 100
        self.output = []

    def mean_test(self, function_to_test, *args, **kwargs ):
        print('Mean test starting, evaluating the function' + function_to_test.__name__)
        for _ in range(self.repetitions):
            print("mean")