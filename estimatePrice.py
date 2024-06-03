import json

def estimatePrice(mileage, theta0, theta1):
    estimatePrice = float(theta0) + (float(theta1) * mileage)
    return estimatePrice

def launchEstimatePrice(mileage):
    with open("values.json", "r") as myJson:
        myData = json.load(myJson)
    
    mileage = float(mileage)
    estimateCarPrice = estimatePrice(mileage, myData["Theta0"], myData["Theta1"])

    return(int(estimateCarPrice))

def main():
    with open("values.json", "r") as myJson:
        myData = json.load(myJson)
    
    mileage = "start"
    while (mileage.isdigit() == False):
        mileage = input("Insert the mileage of your car: ")

    mileage = float(mileage)
    estimateCarPrice = estimatePrice(mileage, myData["Theta0"], myData["Theta1"])

    print(int(estimateCarPrice), "$")

if __name__ == "__main__":
    main()