import sys
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from estimatePrice import estimatePrice

verbosed = False
drawGraphic = False
drawTrain = False

def normalize(series):
    min_val = series.min()
    max_val = series.max()
    normalized_data = (series - min_val) / (max_val - min_val)
    return normalized_data

def denormalize(df, t0, t1):
    
    minPrice_val = df['price'].min()
    maxPrice_val = df['price'].max()
    minKm_val = df['km'].min()
    maxKm_val = df['km'].max()
    
    t0_desnormalizado = 0;
    t1_desnormalizado = 0;
    
    t0_desnormalizado = t0 * (maxPrice_val - minPrice_val) + minPrice_val +\
    (t1 * minKm_val * (minPrice_val - maxPrice_val)) / (maxKm_val - minKm_val)
    t1_desnormalizado = t1 * (maxPrice_val - minPrice_val) / (maxKm_val - minKm_val)
    
    return t0_desnormalizado, t1_desnormalizado

def trainThetas(df, t0, t1):
    learningRate = 0.1
    sumErrorT0 = 0
    sumErrorT1 = 0
    
    for index, car in df.iterrows():
        price = car['price']
        km = car['km']
        prediction = estimatePrice(km, t0, t1)
        error = prediction - price
        sumErrorT0 += error
        sumErrorT1 += error * km
        
    t0 -= learningRate * 1 / len(df) * sumErrorT0
    t1 -= learningRate * 1 / len(df) * sumErrorT1
    
    return (t0, t1)

def writeThetas(jsonFile, t0, t1):
    with open(jsonFile, 'w') as myJson:
        json.dump({"Theta0": t0, "Theta1": t1}, myJson)

def fillGraphic(df_normalized):
    plt.scatter(df_normalized['km'], df_normalized['price'])
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.title('Price vs Kilometers')

def writeThetasLine(t0, t1): 
    price0 = estimatePrice(0, t0, t1)
    price1 = estimatePrice(1, t0, t1)
    plt.plot([0, 1], [price0, price1], color='red')

def launchTrain(csv_file, flags):
    df = pd.read_csv(csv_file)
    t0, t1 = 0, 0

    normalized_data = {}
    normalized_data['price'] = normalize(df['price'])
    normalized_data['km'] = normalize(df['km'])

    df_normalized = pd.DataFrame(normalized_data)
    fillGraphic(df_normalized)

    while (True):
        oldT0 = t0
        oldT1 = t1
        t0, t1 = trainThetas(df_normalized, t0, t1)
        if (flags["verbose"] == True):
            print("Theta0: ", t0)
            print("Theta1: ", t1)
        
        if (t0 == oldT0 and t1 == oldT1):
            break
        if (flags["graphicTrain"] == True):
            plt.clf()
            fillGraphic(df_normalized)
            writeThetasLine(t0, t1)
            plt.pause(0.01)


    writeThetasLine(t0, t1)
    
    t0, t1 = denormalize(df, t0, t1)
    writeThetas('values.json', t0, t1)

    if (flags["graphicFinish"] == True):
        plt.show()

def main():
    csv_file = 'data.csv'
    df = pd.read_csv(csv_file)
    t0, t1 = 0, 0
    
    normalized_data = {}
    normalized_data['price'] = normalize(df['price'])
    normalized_data['km'] = normalize(df['km'])

    df_normalized = pd.DataFrame(normalized_data)
    plt.scatter(df_normalized['km'], df_normalized['price'])
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.title('Price vs Kilometers')

    while (True):
        oldT0 = t0
        oldT1 = t1
        t0, t1 = trainThetas(df_normalized, t0, t1)
        print("Theta0: ", t0)
        print("Theta1: ", t1)
        if (t0 == oldT0 and t1 == oldT1):
            break
        
    price0 = estimatePrice(0, t0, t1)
    price1 = estimatePrice(1, t0, t1)

    plt.plot([0,1], [price0,price1], color='red')
    
    t0, t1 = denormalize(df, t0, t1)
    
    writeThetas('values.json', t0, t1)
    
    plt.show()


if __name__ == "__main__":
    main()