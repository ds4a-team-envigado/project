import pandas as pd

# importar aptitudes y departamentos
path = r"C:\Users\guill\Documents\GitHub\project\Aptitudes_cultivos\data_web.xlsx"
nom_aptitudes = pd.read_excel(path,sheet_name="1")
nom_departamentos = pd.read_excel(path,sheet_name="2")

apts = []
depts = []
for i in nom_aptitudes['aptitudes']:
    for k in nom_departamentos['departamentos']:
        apts.append(i)
        depts.append(k)
df = pd.DataFrame(list(zip(apts, depts)),columns =['Aptitud', 'Departamento'])
df.to_excel(r"C:\Users\guill\Documents\GitHub\project\Aptitudes_cultivos\data_nombres.xlsx")