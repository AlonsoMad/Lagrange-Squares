from algorithms_package.algorithms import finders
from tests_package.statistic_test import tests
def main():
    n = 100
    find = finders()
    test = tests()
    result, iterations = find.findLagSq(5652)
    print(result, iterations)

if __name__ == "__main__":
    main()