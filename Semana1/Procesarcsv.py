import pandas as pd
import numpy as np

csv = "Python.csv"

def leer_csv(csv):
    try:
        df = pd.read_csv(csv, sep=';')
        print("contenido:")
        print(df)
        return df
    except FileNotFoundError:
        print (f"Error: El archivo'{csv}' no se encontró")
        return None
    
def estadisticas(df,columna):
    if columna in df.columns:
        datos = df[columna].dropna().to_numpy()
        print(f"\nEstadísticas de la columna '{columna}':")
        print(f"  Promedio: {np.mean(datos):.2f}")
        print(f"  Mediana: {np.median(datos):.2f}")
        print(f"  Desviación estándar: {np.std(datos):.2f}")
    else:
        print(f"Error: La columna '{columna}' no existe en el archivo.")

if __name__ =="__main__":
    df = leer_csv(csv)

    if id is not None:

        Edad = "Edad"
        estadisticas(df,Edad)
        
        Salario = "Salario"
        estadisticas(df,Salario)

