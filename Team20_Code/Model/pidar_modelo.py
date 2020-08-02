# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from typing import Tuple
from sklearn.cluster import AgglomerativeClustering
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import pathlib
import pandas as pd
import numpy as np
import csv
import sqlalchemy
import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text
n_clusters = 4

# %% [markdown]
# **Bases de datos**
# 
# 1. EVA 
# 2. PROYECTOS_HISTORICO (Hisotrico de proyectos completo.csv)
# %% [markdown]
# **Registro de usuario**
# 
# 1. Cadena productiva CP
# 2. Departamento DP
# 3. Total de beneficiarios BN
# 4. Valor cofinanciación VC
# %% [markdown]
# # Funciones

# %%
# #Traer de la base de datos DIFICIL
# PATH = pathlib.Path('./data').parent
# DATA_PATH = PATH.joinpath("data").resolve()
# EVA = pd.read_csv(DATA_PATH.joinpath('EVA_cultivos_modificado.csv'))
# PROYECTOS_HISTORICO= pd.read_csv('Hisotrico de proyectos completo.csv')


# %%
# %reload_ext sql
# engine1 = create_engine(f'postgresql://adr_user:1234@ds4a-demo-instance.cct4rseci702.eu-west-1.rds.amazonaws.com/adr_db', max_overflow=20)
# EVA = pd.read_sql('SELECT * FROM eva_cultivos',engine1)
# PROYECTOS_HISTORICO= pd.read_sql('SELECT * FROM hist_proyectos',engine1)


# %%
#Cargar los datos
def get_EVA():
    
    engine1 = create_engine(f'postgresql://adr_user:1234@ds4a-demo-instance.cct4rseci702.eu-west-1.rds.amazonaws.com/adr_db', max_overflow=20)
    EVA = pd.read_sql('''SELECT departamento,CADENA_PRODUCTIVA_ADR,CICLO_CULTIVO, avg(RENDIMIENTO) as RENDIMIENTO, avg(area_cosech/area_sembr) as PRODUCTIVIDAD 
    FROM eva_cultivos 
    WHERE area_sembr != 0
    GROUP BY departamento,CADENA_PRODUCTIVA_ADR,CICLO_CULTIVO''',engine1)
    
    return EVA


# %%
H = get_EVA()
H.head()


# %%
#Cargar los datos
def get_history():
    
    engine1 = create_engine(f'postgresql://adr_user:1234@ds4a-demo-instance.cct4rseci702.eu-west-1.rds.amazonaws.com/adr_db', max_overflow=20)
    PROYECTOS_HISTORICO= pd.read_sql('SELECT * FROM hist_proyectos',engine1)
    
    return PROYECTOS_HISTORICO


# %%
#Transformar data historica y EVA
def transform_hist(X1):
    
    scaler = StandardScaler()
    dff= X1.drop(columns = ['departamento', 'municipio', 'year', 'cp','ciclo_cultivo']).copy()
    scaler.fit(dff)
    X2 = scaler.transform(dff)
    X3 =pd.DataFrame(X2, columns = dff.columns)
    X4 = pd.merge(X3,X1[['cp','ciclo_cultivo']],right_index=True,left_index=True)
    
    #Creating dummy variables
    cc_dummy = pd.get_dummies(X4['ciclo_cultivo'])
    cp_dummy = pd.get_dummies(X4['cp'])
    #Concatenating the dummy variables to the original dataset 
    cluster_dummy_set=pd.concat([X4,cc_dummy,cp_dummy],axis=1)
    #Deleting categorical variable from the dummy set
    del cluster_dummy_set['ciclo_cultivo']
    del cluster_dummy_set['cp']
    
    MCU = cluster_dummy_set.sample(frac = 0.5,random_state=42)
    MCL= cluster_dummy_set[~cluster_dummy_set.index.isin(MCU.index)]
    
    MCU=MCU.dropna()
    MCL=MCL.dropna()
    return MCU,MCL


# %%
#Obtener los cluster
def get_clusters(X_train: pd.DataFrame, X_test: pd.DataFrame, n_clusters: int) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    applies k-means clustering to training data to find clusters and predicts them for the test set
    """
    clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage=
                                     'ward').fit(X_train)
    # apply the labels
    train_labels = clustering.labels_
    X_train_clstrs = X_train.copy()
    X_train_clstrs['clusters'] = train_labels
    
    # predict labels on the test set
    test_labels = clustering.fit_predict(X_test)
    X_test_clstrs = X_test.copy()
    X_test_clstrs['clusters'] = test_labels
    return X_train_clstrs, X_test_clstrs





# %%
# Crear la calificacion para cada cluster
def calificar(X_train_clstrs, X1):
    PESOS = [[0.3],[0.1],[0.2],[0.4]]
    #Anexando el cluster a los valores en la escala real
    idx = X_train_clstrs.index
    X5 = X1.iloc[idx].copy()
    X5['key'] = idx
    X_train_clstrs['key']=  idx
    MCU_cl = pd.merge(X5, X_train_clstrs[['clusters','key']],on = 'key', how='left')
    
    #Claificacion de cada cluster
    cols = ['total_beneficiarios','valor_cofinanciaci¢n','rendimiento', 'productividad']
    CALIF = pd.DataFrame()
    for i in cols:
        y = MCU_cl.groupby(['clusters'])[[i]].mean().sort_values(by = i, ascending = False).reset_index()
        y['cal'] = [4,3,2,1]
        y.columns = ['cluster',i,'cal_'+ str(i)]
        temp = y[['cluster','cal_'+ str(i)]]
        if len(CALIF) == 0:
            CALIF = temp
        else:
            CALIF = pd.merge(CALIF,temp,on='cluster',how ='inner')
            
    PROBABILIDADES = CALIF.iloc[:,[1,2,3,4]].dot(PESOS)/4
    calificaciones = pd.merge(CALIF['cluster'],PROBABILIDADES,right_index=True,left_index=True)
    
    return calificaciones




# %%
# Transformar datos usuario - El output es un dicccionario solo con los datos del usuario
def transform_input(registro,X1,EVA):
    #Diccionario del tipo de proyecto
    tipo_proy = {'TERRITORIALES':548743100,'ASOCIATIVOS':392075000,'NACIONALES':634850500}
    info_adicional = EVA
    scaler = StandardScaler()
    dff= X1.drop(columns = ['departamento', 'municipio', 'year', 'cp','ciclo_cultivo']).copy()
    scaler.fit(dff)

    valor = tipo_proy[registro['tipo_proyecto']]
    cp = registro['CP']

    registro.update({'Valor cofinanciación':valor})
    registro.update({cp:1})

    inf = info_adicional[(info_adicional['departamento']==registro['DEPARTAMENTO'])&(info_adicional['cadena_productiva_adr']==cp)][['ciclo_cultivo','rendimiento','productividad']]
    registro.update(inf.to_dict('list'))
       
    registro.update({registro['ciclo_cultivo'][0]:1})
    registro.update({'Valor Contrapartida':registro['Valor cofinanciación']*0.1})
    registro_df = pd.DataFrame(registro)
    
    R1 = registro_df[['Total beneficiarios','Valor cofinanciación','Valor Contrapartida','rendimiento','productividad']]
    R2 = scaler.transform(R1)
    
    R3 = R2.tolist()
    registro.update(zip(['Total beneficiarios','Valor cofinanciación','Valor Contrapartida','rendimiento','productividad'],R3[0]))
    
    return registro


# %%
#CRear df con datos usuario - El output es un df con los datos que salen de transform_input m{as las columnas dummies para ciclo de cultivo y cadena
def create_DU(registro_final):
    
    datos = ['Total beneficiarios','Valor cofinanciación','Valor Contrapartida','rendimiento','productividad']
    ciclo = ['ANUAL', 'PERMANENTE', 'TRANSITORIO']
    cadenas = ['AGUACATE', 'AHUYAMA', 'AJI', 'ALGODON', 'ARAZA', 'ARRACACHA', 'ARROZ',
       'ARVEJA', 'ASAI', 'BADEA', 'BANANO', 'BOROJO', 'BREVO', 'BROCOLI',
       'CACAO', 'CAFE', 'CAUCHO', 'CAÑA AZUCARERA', 'CAÑA PANELERA',
       'CEBOLLA DE BULBO', 'CEBOLLA DE RAMA', 'CHONTADURO', 'CILANTRO',
       'CIMARRON', 'COCO', 'COLIFLOR', 'CURUBA', 'FIQUE', 'FRESA', 'FRIJOL',
       'GRANADILLA', 'GUANABANA', 'GUAYABA', 'HABA', 'HORTALIZAS VARIAS',
       'LECHUGA', 'LIMON', 'LULO', 'MAIZ', 'MAIZ FORRAJERO', 'MALANGA',
       'MAMEY', 'MANDARINA', 'MANGO', 'MANGOSTINO', 'MARACUYA', 'MELON',
       'MORA', 'NARANJA', 'PALMA DE ACEITE', 'PAPA', 'PAPAYA', 'PATILLA',
       'PEPINO COHOMBRO', 'PIMENTON', 'PITAHAYA', 'PIÑA', 'PLATANO',
       'REMOLACHA', 'REPOLLO', 'TANGELO', 'TOMATE', 'TOMATE DE ARBOL', 'TRIGO',
       'UCHUVA', 'ULLUCO', 'UVA', 'YACON', 'YUCA', 'ZANAHORIA', 'ÑAME']
    
        
    ciclo_val = []
    for j in ciclo:
        if j in registro_final:
            ciclo_val.append(1)
        else:
            ciclo_val.append(0)
            
    cadenas_val = []
    for j in cadenas:
        if j in registro_final:
            cadenas_val.append(1)
        else:
            cadenas_val.append(0)
    
    data = []
    for i in datos:
        data.append(registro_final[i])
    
    du = data+ciclo_val+cadenas_val
    cols= datos+ciclo+cadenas
            
    DU = pd.DataFrame(columns = cols)
    DU.loc[0] = du
    
    return DU


# %%
#Corre todas las fucniones anteriores, clasifica y entrega probabilidad
def run_model(n_clusters, registro):
    PESOS = [[0.3],[0.1],[0.2],[0.4]]
    EVA = get_EVA()
    X1 = get_history()
    
    MCU, MCL= transform_hist(X1)
    X_train_clstrs, X_test_clstrs = get_clusters(MCU, MCL, n_clusters)
    CALIFICACION = calificar(X_train_clstrs, X1)
    registro_final = transform_input(registro,X1,EVA)
    DU = create_DU(registro_final)
    
    X = X_test_clstrs.drop(columns = ['clusters'])
    y = X_test_clstrs['clusters']
    rf = RandomForestClassifier(n_estimators=10)
    rf.fit(X, y)
    y_pred = rf.predict(DU)
    y_prob = rf.predict_proba(DU)
    
    APROBADO = CALIFICACION[0]
    PROBABILIDAD_APROBADO = y_prob[0]*APROBADO.T
    
    return PROBABILIDAD_APROBADO.max()*100


# %%

def run_model_pidar():
    print("run_model_pidar")

    ###################EJEMPLO DE CORRIDA#################
    ##Variables definidas por el usuario
    registro = {'CP':'COCO', 'DEPARTAMENTO':'SUCRE','Total beneficiarios':100e6,'tipo_proyecto':'ASOCIATIVOS'}
    print(registro)
    pesos_r = [[0.3],[0.1],[0.2],[0.4]]
    print(pesos_r)
    # Beneficiarios, $, Rendimiento, Productividad
    ##Función principal
    return run_model(4, registro)
    

   # print("La probabilidad de que aprueben su proyecto es {}%.".format(prob))


# %%



# %%



