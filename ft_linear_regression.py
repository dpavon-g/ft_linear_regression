from estimatePrice import launchEstimatePrice
from train import launchTrain
import os

introduction = """

            Welcome to the launcher of the \033[34mft_linear_regression\033[0m. 
                        Made with \033[31m<3\033[0m by dpavon-g


In this project you will train a linear regresion model to predict the price 
of a car based on its mileage.

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
 ╚═╝░░╚═╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝ 

 -------------------------------------------------------------------------------"""

menu = """

                With this launcher you can:

                    1. Train the linear regression model.
                    2. Predict a price using the trained model.
                    3. Know more about the project.
                    4. Exit

-------------------------------------------------------------------------------
"""

estimatePriceMenu = """

You are about to estimate the price of a car based on its mileage.

"""

moreInformation = """

This project is the first from the \033[34mArtificial Intelligence branch of the 42 
Network's outer core\033[0m. Here, you will train a linear regression model to predict
the price of a car based on its mileage.

The original project have its own .csv file with all the mileage and price of
the cars, but you can also import your own if it has \033[32mprice\033[0m and \033[32mkm\033[0m columns.

If you want to know more about the project dont hesitate to ask me or to
look the documentation on my GitHub: 

\033[35mhttps://github.com/dpavon-g/ft_linear_regression\033[0m

                                                        Made with \033[31m<3\033[0m by dpavon-g

"""

def printTitle():
    os.system('clear')
    print(title)

def validInput(value):
    if (int(value) < 1 or int(value) > 4):
        return False
    
    return True

def askNumber(selectionMenu):
    value = input("What do you want to do? (Number): ")
    while (value.isdigit() == False or validInput(value) == False):
        printTitle()
        print(selectionMenu)
        print("Invalid parameter...")
        value = input("What do you want to do? (Number): ")
    
    return value

def calculatePrice():
    printTitle()
    print(estimatePriceMenu)
    mileage = input("Insert the mileage of your car: ")
    while (mileage.isdigit() == False):
        printTitle()
        print(estimatePriceMenu)
        print("Invalid parameter...")
        mileage = input("Insert the mileage of your car: ")
    
    price = launchEstimatePrice(mileage)

    printTitle()
    print("\n\nThe price of a car with " + str(mileage) + "km is " + str(price) + " $\n")

    input("Press enter to continue...")
    printStart()

def showInfo():
    printTitle()
    print(moreInformation)
    input("Press enter to continue...")
    printStart()

def trainModel(error = False):
    printTitle()
    print("\nYou are now in the train model menu.")
    print("Write 'Q' to exit.\n")

    if error == True:
        print("Invalid parameter...")
    inputFile = input("Insert the .csv path: ")

    if inputFile == "Q":
        return -1

    flags = {
        'verbose': False,
        'graphicTrain': False,
        'graphicFinish': False
    }

    if os.path.exists(inputFile):
        printTitle()
        print("\nYou are now in the train model menu.")
        print("Write 'Q' to exit.\n")
        myInput = input("\nTrain the model in Verbosed mode? (N/y): ")
        if myInput == "y":
            flags["verbose"] = True
        elif myInput == "Q":
            return -1
        printTitle()
        print("\nYou are now in the train model menu.")
        print("Write 'Q' to exit.\n")
        myInput = input("\nShow the train in graphic mode? (N/y): ")
        if myInput == "y":
            flags["graphicTrain"] = True
        elif myInput == "Q":
            return -1
        printTitle()
        print("\nYou are now in the train model menu.")
        print("Write 'Q' to exit.\n")
        myInput = input("\nKeep the final linear regresion graphic? (N/y): ") 
        if myInput == "y":
            flags["graphicFinish"] = True
        elif myInput == "Q":
            return -1
        launchTrain(inputFile, flags)

        printTitle()
        print("\nTrain finished succesfully :)\n")
        input("Press enter to continue...)")

        return (-1)
    else:
        trainModel(True)

def printStart():
    printTitle()
    print(menu)
    option = askNumber(menu)

    if option == "1":
        if trainModel() == -1:
            printStart()
    elif option == "2":
        calculatePrice()
    elif option == "3":
        showInfo()
    elif option == "4":
        exit


def main():
    os.system('clear')
    print(introduction)
    input("Press enter to continue...")

    printStart()

main()