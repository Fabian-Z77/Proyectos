import pandas as pd
def sum(a,b):
    resultado = a + b
    return resultado


def validador():
    entrada = 'D:/Tercer semestre/Prueba de software/Sistema/Entity/BaseDatos.txt'
    BaseDatos_dataframe = pd.read_csv(entrada)
    BaseDatos_dataframe.rename(columns = {'123':'Rut','Carlos':'Nombre','53':'Año','100000':'Sueldo','1':'Tipo','214560':'Saldo'},inplace=True)
    BaseDatos_dataframe.iloc[0] = ['123','Carlos','53','100000','1','214560']
    saldo_lista = list(BaseDatos_dataframe[:6]['Saldo'])

    return saldo_lista