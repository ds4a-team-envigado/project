import pandas as pd
import os
import glob

# get names of files
path = "C:/Users/guill/Documents/GitHub/project/Aptitudes_cultivos/datos/"
files = []
for file in os.listdir(path):
    if file.endswith(".xlsx"):
        files.append(file)

# for each file, create a dataframe and a column with the name of cultivo, lastly add this dataframe to a zero dataframe
for i in range(len(files)):
    if i == 0:
        df_ini = pd.read_excel(path+str(files[0]))
        df_ini['Cultivo'] = str(files[0])[7:-5]
    else:
        df = pd.read_excel(path+str(files[i]))
        df['Cultivo'] = str(files[i])[7:-5]
        df_ini = df_ini.append(df)

# procesamiento del dataframe
#poner cultivo como primera columna
first_col = df_ini.pop("Cultivo")
df_ini.insert(0, "Cultivo", first_col)
#borrar columna
df_ini.pop('Unnamed: 0')
# poner muy baja como quinta columna
fift_col = df_ini.pop("Muy baja [ha]")
df_ini.insert(5, "Muy baja [ha]", fift_col)
df_ini['Muy baja [ha]'] = df_ini['Muy baja [ha]'].fillna(0)
# eliminar los de semestre 2
df_ini = df_ini[~df_ini['Cultivo'].str.contains("semestre II")]

# quitar nombres cientificos
cultivos = []
for cultivo in df_ini['Cultivo']:
    if cultivo == "Papa (Solanum tuberosum L.) Diacol Capiro semestre I":
        cultivo = "Papa capira"
    words = cultivo.split('(')
    cultivos.append(words[0])

df_ini['Cultivo']=cultivos

# Organizar nombres de departamentos
df_norm = df_ini

# Coger los nombres de departamentos del Json
import json
with open(path+'departamentos.json') as f:
    counties = json.load(f)

Departamentos = []
geocol = counties.copy()
#Sacar una lista de los departamentos llamada "Departamentos"
for man in geocol['features']:
    Departamentos.append(man['properties']['NOMBRE_DPT'])
    man['id']=man['properties']['NOMBRE_DPT']

# Por cada departamento del Json
for depto in Departamentos:
    # si está ya en el data set, no hacer nada, si no está hacer lo siguiente
    if df_norm['Departamento'].str.contains(depto).any() == False:
        # Revisar cantidad de palabras
        words = depto.split()
        # Si hay una sola palabra, coger el 60 % de esa palabra y buscarlo
        if len(words) == 1:
            df_norm.loc[df_norm.Departamento.str.find(depto[:int(len(depto)*0.6)])>=0, 'Departamento'] = depto
        # Si hay entre 2 o 3 palabras por lo general se encuentra casi la misma palabra (80%)
        elif len(words) > 1 and len(words) <= 3:
            df_norm.loc[df_norm.Departamento.str.find(depto[:int(len(depto)*0.8)])>=0, 'Departamento'] = depto
        # si hay mas de 4 palabras, el unico registro es san andres
        elif len(words) > 4:
            df_norm.loc[df_norm.Departamento.str.find("SAN ANDRES")>=0, 'Departamento'] = depto

# Export dataframe as csv
df_ini.to_csv("C:/Users/guill/Documents/GitHub/project/Aptitudes_cultivos/data_sipra.csv")
df_ini.to_excel("C:/Users/guill/Documents/GitHub/project/Aptitudes_cultivos/data_sipra.xlsx")

df_norm.to_csv("C:/Users/guill/Documents/GitHub/project/Aptitudes_cultivos/data_sipra_normalizado.csv")
df_norm.to_excel("C:/Users/guill/Documents/GitHub/project/Aptitudes_cultivos/data_sipra_normalizado.xlsx")