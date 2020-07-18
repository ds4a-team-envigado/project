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

# Export dataframe as csv
df_ini.to_csv("C:/Users/guill/Documents/GitHub/project/Aptitudes_cultivos/data_sipra.csv")
df_ini.to_excel("C:/Users/guill/Documents/GitHub/project/Aptitudes_cultivos/data_sipra.xlsx")
