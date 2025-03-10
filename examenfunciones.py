import pandas as pd
import numpy as np

#Función_1. Carga los archivos con extensiones .csv y .xlsx y los convierte a dataframe, si es un  archivo con cualquier 
#otra extensión, emitirá el raise (“Este formato no esta soportado para esta función: .formato”)
def cargar_archivo(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"Este formato no está soportado para esta función: {file_path.split('.')[-1]}")


 #se limpian de nulos .Función_2. Sustituye los valores nulos de las variables pares numéricas con el método “mean” 
 #y de las impares numéricas con la constante “99”. Las columnas que no sean de tipo numérico se sustituirán con el string “Este_es_un_valor_nulo”
def reemplazar_nulos(df):
    """Sustituye valores nulos según la especificación"""
    for col in df.columns:
        if df[col].dtype == 'float64' or df[col].dtype == 'int64':
            if df.columns.get_loc(col) % 2 == 0:
                df[col].fillna(df[col].mean(), inplace=True)
            else:
                df[col].fillna(99, inplace=True)
        else:
            df[col].fillna("Este_es_un_valor_nulo", inplace=True)
    return df


#Función_3. Identifica los valores nulos “por columna” y “por dataframe”
def detectar_nulos(df):
    """Identifica valores nulos por columna y por DataFrame"""
    nulos_por_columna = df.isnull().sum()
    total_nulos = df.isnull().sum().sum()
    return nulos_por_columna, total_nulos


#Función_4. Sustituye  los valores atípicos de las columnas numéricas con el método de “Rango intercuartílico”. 
def reemplazar_atipicos(df):
    """Reemplaza valores atípicos en columnas numéricas usando el Rango Intercuartílico"""
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        df[col] = np.where((df[col] < limite_inferior) | (df[col] > limite_superior), df[col].median(), df[col])
    return df
