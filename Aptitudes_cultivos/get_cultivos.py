from selenium import webdriver
import os #Dar propiedades y listas de directorios
import time 
import pandas as pd
import urllib.request
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# importar aptitudes y departamentos
path = r"C:\Users\guill\Documents\GitHub\project\Aptitudes_cultivos\data_web.xlsx"
nom_aptitudes = pd.read_excel(path,sheet_name="1")
nom_departamentos = pd.read_excel(path,sheet_name="2")

# importar driver
browser = webdriver.Chrome("C:/Users/guill/Downloads/chromedriver_win32/chromedriver.exe")
browser.implicitly_wait(30)

# abrir pagina
browser.get('https://sipra.upra.gov.co/')
time.sleep(30)

# encontrar pestaña de estadisticas
#print("se termino la espera entrando a estadsiticas")
# estadisticas = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[18]")
# estadisticas.click()
# time.sleep(15)
datos_apt = []
datos_dep = []
datos_tab = []

for i in nom_aptitudes['aptitudes']:
    try:
        aptitudes = browser.find_element_by_css_selector("#cbLayer_sub")
        for z in range(len(nom_aptitudes['aptitudes'])):
            time.sleep(0.5)
            aptitud = browser.find_element_by_css_selector("#widget_cbLayer_sub > div.dijitReset.dijitInputField.dijitInputContainer > input[type=hidden]:nth-child(2)").get_attribute("value")
            if aptitud == i:
                print(i)
                break
            time.sleep(1)
            aptitudes.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        aptitudes.send_keys(Keys.ENTER)
        # browser.find_element_by_css_selector("#table").click()
        time.sleep(2)
        for k in nom_departamentos['departamentos']:
            departamentos = browser.find_element_by_css_selector("#cbDepartamento_sub")
            for x in range(len(nom_departamentos['departamentos'])):
                departamento = browser.find_element_by_css_selector("#widget_cbDepartamento_sub > div.dijitReset.dijitInputField.dijitInputContainer > input[type=hidden]:nth-child(2)").get_attribute("value")
                time.sleep(0.5)
                if departamento == k:
                    print(k)
                    break
                time.sleep(1)
                departamentos.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
            departamentos.send_keys(Keys.ENTER)
            time.sleep(2)
            # browser.find_element_by_css_selector("#table").click()
            table = browser.find_element_by_css_selector('#table')
            values = table.find_elements_by_tag_name('td')
            col1 = []
            col2 = []
            col3 = []
            for y in range(len(values)):
                if y == 0:
                    tit1 = values[0].text
                elif y == 1:
                    tit2 = values[1].text
                elif y == 2:
                    tit3 = values[2].text
                else:
                    if (y%3) == 0:
                        col1.append(values[y].text)
                    elif (y%3) == 1:
                        col2.append(values[y].text)
                    elif (y%3) == 2:
                        col3.append(values[y].text)
            df = pd.DataFrame(list(zip(col1,col2,col3,)),columns =[str(tit1),str(tit2),str(tit3)])
            df.to_excel("C:/Users/guill/Documents/GitHub/project/Aptitudes_cultivos/datos/"+str(i)+"_"+str(k)+".xlsx")
            # try: 
            exportar = browser.find_element_by_xpath('//*[@id="Exportdata"]/span')
            #exportar = browser.find_element_by_class_name("dijitReset dijitStretch dijitButtonContents")
            # except:
                # try:
                #     exportar = browser.find_element_by_css_selector("#dijit_form_Button_2")
                # except:
                #     exportar = browser.find_element_by_css_selector("#dijit_form_Button_3")
            exportar.click()
            datos_apt.append(i)
            datos_dep.append(k)
            print("se exportó Datos",i,",",k,"primer valor col3:",col3[0])
            time.sleep(5)
    except:
        df = pd.DataFrame(list(zip(datos_apt, datos_dep)),columns =['Aptitud', 'Departamento'])
        df.to_excel(r"C:\Users\guill\Documents\GitHub\project\Aptitudes_cultivos\data_descargado.xlsx")
df = pd.DataFrame(list(zip(datos_apt, datos_dep)),columns =['Aptitud', 'Departamento'])
df.to_excel(r"C:\Users\guill\Documents\GitHub\project\Aptitudes_cultivos\data_descargado.xlsx")


