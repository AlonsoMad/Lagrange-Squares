from algorithms_package.algorithms import Finders

def main():
    find = Finders()
    c = True
    while c:
        print(find.findLagSq2(int(input("Please insert the number you want to decompose:\n"))))
        response = input("Do you want to decompose another number: [Y/n]\n")
        if response.upper() != 'Y':
            c = False

if __name__ == "__main__":
    main()
    #find = Finders()
    #find.MiniTest(646,323)


    #Buscar tesis doctorales. Quiza encuentres mas sobre el tema
    #University of Zurich