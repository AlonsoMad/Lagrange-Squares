from algorithms_package.algorithms import finders
from tests_package.statistic_test import tests
def main():
    n = 100
    find = finders()
    test = tests()
    result, potato ,iterations = find.findLagSq2(2023)
    print(result, iterations, potato)

if __name__ == "__main__":
    main()