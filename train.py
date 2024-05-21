import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Usa el backend "Agg" para entornos no interactivos
import matplotlib.pyplot as plt

def normalize(df, min, max):
    data = [];
    for value in df:
        data.append((value - min) / (max - min))
    return data



# print(df['km'].min())
# print(df['price'].min())

# for (columnName, columnData) in df.iteritems():
#     print(columnName)
#     print(columnData)

def main():
    csv_file = 'data.csv'
    df = pd.read_csv(csv_file)
    
    normalized_data = {}
    normalized_data['price'] = normalize(df['price'], df['price'].min(), df['price'].max())
    normalized_data['km'] = normalize(df['km'], df['km'].min(), df['km'].max())

    # print(normalized_data['price'])
    # print(normalized_data['km'])
    
    df_normalized = pd.DataFrame(normalized_data)
    plt.scatter(df_normalized['km'], df_normalized['price'])
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.title('Price vs Kilometers')
    plt.show();

main()