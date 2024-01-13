import pandas as pd
import matplotlib.pyplot as plt

try:
    archivo_csv = "heart_failure_clinical_records_dataset.csv"
    dataframe = pd.read_csv(archivo_csv)

  
    dataframe.dropna(inplace=True)


    dataframe.drop_duplicates(inplace=True)

   
    Q1 = dataframe['age'].quantile(0.25)
    Q3 = dataframe['age'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    dataframe = dataframe[(dataframe['age'] >= lower_bound) & (dataframe['age'] <= upper_bound)]

     
    men_data = dataframe[dataframe['sex'] == 1]
    women_data = dataframe[dataframe['sex'] == 0]


    categories = ['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']
    men_counts = [men_data[category].sum() for category in categories]
    women_counts = [women_data[category].sum() for category in categories]

    x = range(len(categories))

    plt.subplot(1, 2, 2)
    plt.bar(x, men_counts, color='green', width=0.4, label='Hombres', align='edge', alpha=0.6)
    plt.bar(x, women_counts, color='red', width=0.4, label='Mujeres', align='edge', alpha=0.6)
    plt.xticks(x, categories)
    plt.xlabel('Categorías')
    plt.ylabel('Cantidad')
    plt.title('Categorías por Sexo')
    plt.legend()

    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"El archivo CSV en la ubicación '{archivo_csv}' no se encontró.")
except Exception as e:
    print(f"Error inesperado: {e}")