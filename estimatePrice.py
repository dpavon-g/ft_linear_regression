import matplotlib.pyplot as plt
import numpy as np
import json

def estimatePrice(mileage, theta0, theta1):
    estimatePrice = float(theta0) + (float(theta1) * mileage)
    return estimatePrice

def drawGraphic(theta0, theta1):
    x_values = np.linspace(0, 1, 100)
    y_values = estimatePrice(x_values, theta0, theta1)
    plt.plot(x_values, y_values, color='red', label='Línea de regresión')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Regresión Lineal')
    plt.show()

def main():
    with open("values.json", "r") as myJson:
        myData = json.load(myJson)
    
    mileage = "start"
    while (mileage.isdigit() == False):
        mileage = input("Insert the mileage of your car: ")

    mileage = float(mileage)
    estimateCarPrice = estimatePrice(mileage, myData["Theta0"], myData["Theta1"])

    print(int(estimateCarPrice), "$")

    drawGraphic(myData["Theta0"], myData["Theta1"])

if __name__ == "__main__":
    main()