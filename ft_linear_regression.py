import os
from estimatePrice import launchEstimatePrice

introduction = """

            Welcome to the launcher of the \033[34mft_linear_regression\033[0m. 
                        Made with \033[31m<3\033[0m by dpavon-g


In this project you will train a linear regresion model to predict the price 
of a car due to its mileage.

If you want to know more about the project dont hesitate to ask me or to
look the documentation on my GitHub: 

\033[35mhttps://github.com/dpavon-g/ft_linear_regression\033[0m


"""

title = """
 ██╗░░░░░██╗███╗░░██╗███████╗░█████╗░██████╗░
 ██║░░░░░██║████╗░██║██╔════╝██╔══██╗██╔══██╗
 ██║░░░░░██║██╔██╗██║█████╗░░███████║██████╔╝
 ██║░░░░░██║██║╚████║██╔══╝░░██╔══██║██╔══██╗
 ███████╗██║██║░╚███║███████╗██║░░██║██║░░██║
 ╚══════╝╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝

 ██████╗░███████╗░██████╗░██████╗░███████╗░██████╗░██████╗██╗░█████╗░███╗░░██╗
 ██╔══██╗██╔════╝██╔════╝░██╔══██╗██╔════╝██╔════╝██╔════╝██║██╔══██╗████╗░██║
 ██████╔╝█████╗░░██║░░██╗░██████╔╝█████╗░░╚█████╗░╚█████╗░██║██║░░██║██╔██╗██║
 ██╔══██╗██╔══╝░░██║░░╚██╗██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗██║██║░░██║██║╚████║
 ██║░░██║███████╗╚██████╔╝██║░░██║███████╗██████╔╝██████╔╝██║╚█████╔╝██║░╚███║
 ╚═╝░░╚═╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝ """

menu = """

-------------------------------------------------------------------------------

                With this launcher you can:

                    1. Train the linear regression model.
                    2. Predict a price using the trained model.
                    3. Know more about the project.
                    4. Exit

-------------------------------------------------------------------------------
"""

estimatePriceMenu = """

-------------------------------------------------------------------------------

You are about to estimate the price of a car due its mileage.

"""

def validInput(value):
    if (int(value) < 1 or int(value) > 4):
        return False
    
    return True

def askNumber(selectionMenu):
    value = input("What do you want to do? (Number): ")
    while (value.isdigit() == False or validInput(value) == False):
        os.system('clear')
        print (title)
        print (selectionMenu)
        print ("Invalid parameter...")
        value = input("What do you want to do? (Number): ")
    
    return value

def calculatePrice():
    os.system('clear')
    print (title)
    print (estimatePriceMenu)
    mileage = input("Insert the mileage of your car: ")
    while (mileage.isdigit() == False):
        os.system('clear')
        print (title)
        print (estimatePriceMenu)
        print ("Invalid parameter...")
        mileage = input("Insert the mileage of your car: ")
    
    price = launchEstimatePrice(mileage)

    os.system('clear')
    print (title)
    print ("\n\nThe price of a car with " + str(mileage) + "km is " + str(price) + " $")

    input("Press enter to continue...")
    printStart()

def printStart():
    os.system('clear')

    print(title)
    print(menu)
    option = askNumber(menu)

    if option == "1":
        printStart()
    elif option == "2":
        printStart()
    elif option == "3":
        calculatePrice()
    elif option == "4":
        exit


def main():
    os.system('clear')
    print(introduction)
    input("Press enter to continue...")

    printStart()

main()