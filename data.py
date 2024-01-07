import pandas as pd

from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

df = pd.DataFrame(data)

fallecidos_df = df[df['is_dead'] == 1]

no_fallecidos_df = df[df['is_dead'] != 1]

promedio_edad_fallecidos = fallecidos_df['age'].mean()

promedio_edad_no_fallecidos = no_fallecidos_df['age'].mean()

tipos_de_datos = df.dtypes
print(tipos_de_datos)

Verificacion_edad=df['age',] = pd.to_numeric(df['age'], errors='coerce')
#Verificacion_anaemia=df['creatinine_phosphokinase']= pd.to_numeric(df['creatinine_phosphokinase'], errors='coerce')

Cantidad_fumadores_df = df.groupby('is_male')['is_smoker'].apply(lambda x: (x == True).sum()).reset_index().mean()

print("Promedio de edades de personas que no fallecieron:", promedio_edad_no_fallecidos)

print("Promedio de edades de personas fallecidas:", promedio_edad_fallecidos)

print("Fallecidos por edad",promedio_edad_fallecidos)

print("Verificacion de edada",Verificacion_edad)

print("Cantidad de fumadores H/M",Cantidad_fumadores_df)

