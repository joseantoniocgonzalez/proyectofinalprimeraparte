#Con este programa en python podremos ver  la sala, el lugar y los artistas que tendran proximamente un concierto  en España con las fechas indicadas. 

#Para ello necesitamos  autentificarnos con la API key.
# Esta API utiliza la respuesta json.



#Vamos a usar variables de entorno para guardar nuestra key.
# Deremos exportar la clave de nuestra cuenta en una variable de entorno en  la terminal:

#Para ello necesitas autentificarte con la API key.
# Esta API utiliza la respuesta json.

#Vamos a usar variables de entorno para guardar nuestra key.
# Deremos exportar la clave de nuestra cuenta en una variable de entorno desde la terminal:
# exportkey ="**************************"



#importamos  la librería requests
import requests
#Importamos la libreria json
import json
#Importar la librería os que va leer nuestra variable de entorno
import os




#Importar las fechas
from datetime import datetime



#Guardamos la url base
url_base="https://app.ticketmaster.com/discovery/v2/"

#En la variable key, guardamos por el diccionario os.environ nuestra key
key=os.environ["exportkey"]

payload={'apikey':key,'countryCode':'ES','size':20,'sort':'date,desc'}
r=requests.get(url_base+'events.json',params=payload)


#en estavariable el código del país, en esta caso como queremos poner los eventos de españa pondremos 'ES'
code='ES'
#creamos un diccionario que guarde nuestros parámetros
payload = {'apikey':key,'countryCode':code}



#Aqui  en ests variable la peticion, y añadimos los parametros tambien.
r=requests.get(url_base+'venues.json',params=payload)

# con función que recibe un identificador del lugar y devuelve el nombre del evento y la fecha en la que está previsto.



def mostrar_artista_fecha (id_lugar):
    parametros = {'apikey':key,'venueId':id_lugar}
    peticion=requests.get(url_base+'events',params=parametros)
    nombres=[]
    fechas=[]
    if peticion.status_code == 200:
        contenido = peticion.json()
        for elem in contenido["_embedded"]["events"]:
            nombres.append(elem["name"])
            fechas.append(elem["dates"]["start"]["localDate"])
        filtro=[nombres,fechas]
        return filtro

#Consulmtamos el estado de la peticion para comprobar que no hay errores.
#Iniciamos las listas necesarias.
salas=[]
lugares=[]
identificadores=[]
if r.status_code == 200:
    doc = r.json()
    for lugar in doc["_embedded"]["venues"]:
        salas.append(lugar["name"])
        lugares.append(lugar["state"]["name"])
        identificadores.append(lugar["id"])
    filtro=[salas,lugares,identificadores]

    
    #Mostramos la sala y el lugar donde se encuentra. Segun el identificador del lugar muestra el nombre del artista y la fecha en la que actúa.
    for sala,lugar,ident in zip(filtro[0],filtro[1],filtro[2]):
        if mostrar_artista_fecha(ident):
            print()
            print("\nLUGAR: ",lugar,"\nSALA:",sala)
            print("\nArtistas que van a tocar en la sala proximamente:")
            for nom,fecha in zip((mostrar_artista_fecha(ident)[0]),(mostrar_artista_fecha(ident)[1])):
                fecha_cambiada = datetime.strptime(fecha, '%Y-%m-%d')
                fecha_str = datetime.strftime(fecha_cambiada, '%d/%m/%Y')
                print("- ",nom,"Fecha: ",fecha_str) 
