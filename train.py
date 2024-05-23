import pandas as pd
import matplotlib.pyplot as plt
from estimatePrice import estimatePrice

def normalize(series):
    min_val = series.min()
    max_val = series.max()
    normalized_data = (series - min_val) / (max_val - min_val)
    return normalized_data

def trainTheta0(df):
    learningRate = 0.1
    t0 = learningRate * (1/len(df))
    t1 = learningRate * (1/len(df))
    for index, car in df.iterrows():
        t0 = t0 + estimatePrice(car['km'], t0, t1) - car['price']
        t1 = t1 + (estimatePrice(car['km'] - car['price'], t0, t1) * car['km'])
    print("Theta0: ", t0)
    print("Theta1: ", t1)

def main():
    csv_file = 'data.csv'
    thetaJson = 'values.json'
    df = pd.read_csv(csv_file)
    
    normalized_data = {}
    normalized_data['price'] = normalize(df['price'])
    normalized_data['km'] = normalize(df['km'])

    df_normalized = pd.DataFrame(normalized_data)
    plt.scatter(df_normalized['km'], df_normalized['price'])
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.title('Price vs Kilometers')

    trainTheta0(df_normalized)
    plt.show()



main()