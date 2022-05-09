#Enunciado:
#Introduce el nombre de una competición y averigua su máximo goleador.

#Librerias necesarias
import requests
import json
import os

#Declaración de variables
URL_BASE="https://livescore-api.com/api-client/"
KEY=os.environ["key"]
SECRET=os.environ["secret"]
payload={'key':KEY,'secret':SECRET}

r_info_competiciones=requests.get(URL_BASE+'competitions/list.json',params=payload)
dic_info_competiciones=r_info_competiciones.json()
lista_id_competiciones=[]
lista_nombre_competiciones=[]
for info in dic_info_competiciones["data"]["competition"]:
    if info["id"] not in lista_id_competiciones:
        lista_nombre_competiciones.append(info["name"])
        lista_id_competiciones.append(info["id"])

#PROGRAMA
print()
print("Bienvenido al programa")
print()
nombre_liga=input("Introduce el nombre de una competición: ")
if nombre_liga not in lista_nombre_competiciones:
    print()
    print("No se ha encontrado ninguna competición con ese nombre")
    print()
    print("Fin del programa")
else:
    payload["competition_id"]=lista_id_competiciones[lista_nombre_competiciones.index(nombre_liga)]
    r_info_goleadores=requests.get(URL_BASE+"competitions/goalscorers.json",params=payload)
    dic_goleadores=r_info_goleadores.json()
    lista1=[]
    lista2=[]
    lista3=[]
    for info in dic_goleadores["data"]["goalscorers"]:
        lista1.append(info["team"]["name"])
        lista2.append(info["name"])
        lista3.append(info["goals"])
    if len(lista1)<1 or len(lista2)<1 or len(lista3)<1:
        print("No se encontraron datos de esta liga")
    else:
        print()
        print("MÁXIMO GOLEADOR")
        print()
        print("Club: ",lista1[0])
        print()
        print("Jugador: ",lista2[0])
        print()
        print("Goles: ",lista3[0])

print()
print("Fin del programa")