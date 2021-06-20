import seaborn as sns
import pandas as pd
from scipy import stats


def replace(df, old_var_arr,new_var):
    """
    Definición: La función cambia unos o más valores.
    Parametro:  df = Data Frame
                old_var_arr = array con valores a reemplazar
                new_var = valor reemplazadp
    Input: data frame, array.
    Output: string.
    """
    for i in old_var_arr:
        df_rep = df.replace(old_var_arr,new_var)
    return df_rep


def z_score(df,var):
     """
    Definición: La función genera los puntajes Z, para las variables 
    Parametro:  df = Data Frame
                var = columnas a transformar a Z score 
    Input: data frame, str.
    Output: float.
    """

     df[var+'_zscore']=stats.zscore(df[var])


def count_value(df, value):
    
    """
    Definición: La función retorna la columna en donde se encuentra un valor buscado, la cantidad de veces que se repite y el %
    Parametro:  df = Data Frame
                value = valor a sumar
    Input: data frame, string.
    Output: string.
    """
    
    columns = df.columns
    shape_value = df.shape[0]
    
    for i in columns:
        sum_value = df[i].isin([value]).sum()
        if sum_value > 0:
            print(f'Column: {i}\tTotal values: {sum_value}\tPercentage:{round((sum_value/shape_value*100),1)}%')

def filt_col_describe(df,col, under_val,over_val):
    
    """
    Definición: La función retorna los valores de 2 variables en una columna de un dataframe.
    Parametro:  df = Data Frame
                col = Columna donde se encuentran las clases
                under_val = primera clase a contabilizar
                over_val = segunda clase a contabilizar
    Input: data frame, string.
    Output: string.
    """

    sum_obj_vec = df[col].value_counts().sum()
    sum_under = df[df[col] == under_val].shape[0]
    sum_over = df[df[col] == over_val].shape[0]
    
    per_under = round(sum_under/sum_obj_vec*100,2)
    per_over = round(sum_over/sum_obj_vec*100,2)
  
    print(f'Total de registros de clase {under_val}: \t{sum_under}\t{per_under}%')
    print(f'Total de registros de la clase {over_val}:\t{sum_over}\t{per_over}%')
    print(f'Total de registros de columna {col}: \t{sum_obj_vec}\t100%')

def missing_data(df):

    """
    Definición: La función retorna los valores y porcentajes de datos nulos y NaN, según columna
    Parametro:  df = Data Frame
    Input: data frame.
    Output: lista.
    """

    columns = list(df.columns)
    isna = list(df.isna().sum())
    isnull = list(df.isnull().sum())
    percent_missing_null = df.isnull().sum() * 100 / len(df)
    percent_missing_nan = df.isnull().sum() * 100 / len(df)   

    lists = [columns, isna, percent_missing_nan  ,isnull, percent_missing_null]
    
    x = pd.DataFrame(lists).T.set_axis(['Column', 'is NaN','% is NaN','is Null','% is Null'], axis=1, inplace=False)
    return x

def nan_heatmap(x):
    sns.heatmap(x.isna(),yticklabels=False,cbar=False,cmap='viridis')

def null_heatmap(x):
    sns.heatmap(x.isnull(),yticklabels=False,cbar=False,cmap='viridis')

def count_class(df, col):
    
    """
    Definición: La función retorna la cantidad de veces que se repite una clase
    Parametro:  df = Data Frame
                col = nombre de columna objetivo
    Input: data frame, string.
    Output: string.
    """
    
    print(df[col].value_counts())
    print('\nTotal: ', df[col].value_counts().sum())