import pandas as pd
import matplotlib.pyplot as plt

def normalize(series):
    min_val = series.min()
    max_val = series.max()
    normalized_data = (series - min_val) / (max_val - min_val)
    return normalized_data

def main():
    csv_file = 'data.csv'
    df = pd.read_csv(csv_file)
    
    normalized_data = {}
    normalized_data['price'] = normalize(df['price'])
    normalized_data['km'] = normalize(df['km'])

    df_normalized = pd.DataFrame(normalized_data)
    plt.scatter(df_normalized['km'], df_normalized['price'])
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.title('Price vs Kilometers')
    plt.show();

main()