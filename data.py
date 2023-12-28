import pandas as pd

from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

df = pd.DataFrame(data)

fallecidos_df = df[df['age'] == 1]

no_fallecidos_df = df[df['age'] != 1]

promedio_edad_fallecidos = fallecidos_df['age'].mean()
print("Promedio de edades de personas fallecidas:", promedio_edad_fallecidos)

promedio_edad_no_fallecidos = no_fallecidos_df['age'].mean()
print("Promedio de edades de personas que no fallecieron:", promedio_edad_no_fallecidos)