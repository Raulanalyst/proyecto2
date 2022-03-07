# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 01:15:09 2022

@author: Familia
"""
import pandas as pd 


datos=pd.read_csv('C:/Users/bruni/Documents/Raul/Emtech/synergy_logistics_database.csv') #Importación de datos
"Punto 1: Conteo y suma de de las diferentes rutas" 
con_rutas=datos.groupby(['origin','destination']).count().sort_values('year',ascending=False)
sum_pdr=datos.groupby(['origin','destination']).sum().sort_values('total_value',ascending=False)
conrut_pd=con_rutas.index.tolist()[0:10] #Lista de las primeras 10 rutas
total=datos['total_value'].sum() #Total global de todos los datos
"Cíclo para sumar la aportación de las 10 primeras rutas e imprimirlas"
suma=0
print('Las 10 rutas más transitadas son:')
for i in conrut_pd:
    suma+=sum_pdr.iloc[sum_pdr.index.get_loc(i),2]
    print(i)
porcentaje=round((suma*100)/total,2) #Porcentaje de aportación de las 10 primeras rutas
print(f"Dichas rutas aportan un {porcentaje}% del total de las ganancias\n")

"Punto dos: Suma de las aportaciones de los diferentes transportes"
sum_tran=datos.groupby(['transport_mode']).sum().sort_values('total_value',ascending=False) #Suma de los modos de transporte
sumtra_pt=sum_tran.index.tolist()[0:3] #Lista de los primeros 3 transportes 
suma_tran=0
print('Los 3 transportes con mayor aportación son:')
"Cíclo para la impresión y suma de los tres primeros valores"
for i in sumtra_pt:
    suma_tran+=sum_tran.iloc[sum_tran.index.get_loc(i),2]
    print(i)
porcentaje_tran=round((suma_tran*100)/total,2) #Porcentaje de aportación de los 3 primeros medios de transporte 
print(f"Los primeros 3 medios de transporte aportan un {porcentaje_tran}% del total de las ganancias\n")

"Punto tres:Países"
sum_pais=datos.groupby(['origin']).sum().sort_values('total_value',ascending=False) #Suma de los países 
ochenta=total*.8 #Cálculo del 80 porciento del total de las ganaicas 
paises=sum_pais.index.tolist() #Lista de todos los países 
suma_pais=0
cont=-1
"Cíclo while para saber cuales son los países que aportan el 80%"
while suma_pais<ochenta:
    cont+=1
    suma_pais+=sum_pais.iloc[sum_pais.index.get_loc(paises[cont]),2]
print('Los pasíses que aportan el 80% de las ganancias son:')
"Cíclo for para la impresión de los países que aportan el 80%"
for i in range(cont+1):
    print(paises[i])
porcentaje_pais=round(suma_pais*100/total,2)
print(f"Estos países generan un {porcentaje_pais}% del total de las ganancias\n")
"Comparación final"
print('Información adicional\n')
con_modtra=datos.groupby(['transport_mode']).count().sort_values('year',ascending=False).index.tolist()
"Cíclo para imprimir los medios de transporte en orden de uso"
print('Los medios de transporte ordenados por uso:')
for i in con_modtra:
    print(i)
print('Los medios de transporte más usados por los países que generan el 80% de las ganancias son:')
con_paistran=datos.groupby(['origin','transport_mode']).count().sort_values('year',ascending=False).index.tolist()
contador=0
"Cíclo para imprimir solamente el medio de transporte más utilizado"
while contador<=8:
    for i in con_paistran:
        if i[0]==paises[contador]:
            print(i)
            contador+=1
            break
            
