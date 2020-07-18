from selenium import webdriver
import os #Dar propiedades y listas de directorios
import time 
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# importar aptitudes
path = r"C:\Users\guill\Documents\GitHub\project\Aptitudes_cultivos\data_web.xlsx"
nom_aptitudes = pd.read_excel(path,sheet_name="3")

# importar driver
browser = webdriver.Chrome("C:/Users/guill/Downloads/chromedriver_win32/chromedriver.exe")
browser.implicitly_wait(60)

# abrir pagina
browser.get('https://sipra.upra.gov.co/')
time.sleep(30)
# Nota: cuando abra la web page, debo de cerrar estadisticas y abrir cadenas productivas predominates, además poner en departamentos

# Por cada aptitud que tengo en excel
for i in nom_aptitudes['aptitudes']:
    time.sleep(1)
    # seleccionar donde están las aptitudes
    aptitudes = browser.find_element_by_css_selector("#comboOpciones")
    aptitudes.clear()
    aptitudes.send_keys(str(i)[0:-1])
    # # la unica forma de elegir las aptitudes toca a apartir de un loop bajando por cada aptitud
    # for z in range(len(nom_aptitudes['aptitudes'])):#widget_comboOpciones > div.dijitReset.dijitInputField.dijitInputContainer"
    #     time.sleep(0.5)
    #     # tomar el valor que hay de aptitudes en el momento
    #     aptitud = browser.find_element_by_css_selector("#comboOpciones").get_attribute("value")
    #     # si es el valor que busco entonces salir de este loop
    #     if aptitud == i:
    #         print(i)
    #         break
    #     time.sleep(1)
    #     # si no es el valor entonces mirar la aptitud de abajo
    #     aptitudes.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    aptitudes.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    aptitudes.send_keys(Keys.ENTER)
    time.sleep(2)
    table = browser.find_element_by_css_selector('#gridcontainer > table')
    values = table.find_elements_by_tag_name('td')
    col1 = []
    col2 = []
    col3 = []
    col4 = []
    col5 = []
    col6 = []
    # pasar todos los datos de la tabla a un dataframe
    for y in range(len(values)):
        if y == 0:
            tit1 = values[0].text
        elif y == 1:
            tit2 = values[1].text
        elif y == 2:
            tit3 = values[2].text
        elif y == 3:
            tit4 = values[3].text
        elif y == 4:
            tit5 = values[4].text
        elif y == 5:
            tit6 = values[5].text
        else:
            if (y%6) == 0:
                col1.append(values[y].text)
            elif (y%6) == 1:
                col2.append(values[y].text)
            elif (y%6) == 2:
                col3.append(values[y].text)
            elif (y%6) == 3:
                col4.append(values[y].text)
            elif (y%6) == 4:
                col5.append(values[y].text)
            elif (y%6) == 5:
                col6.append(values[y].text)
    df = pd.DataFrame(list(zip(col1,col2,col3,col4,col5,col6)),columns =[str(tit1),str(tit2),str(tit3),str(tit4),str(tit5),str(tit6)])
    df.to_excel("C:/Users/guill/Documents/GitHub/project/Aptitudes_cultivos/datos/deptos_"+str(i)+".xlsx")
    print("se exportaron Datos",i,"primer valor col6:",col6[0])
    time.sleep(5)
