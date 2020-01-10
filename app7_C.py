# menu donde se puede ver peliculas / series / Telenovelas
import libreria
def pelicula():
    # elejir nombre de la pelicula
    peli=libreria.pedir_peli("star wars / stand de besos :")
    # que dia de la semana la voy a ver
    dia=libreria.pedir_dia("Ingrese dia: ")
    # cuantos la vamos a ver( solo se pueden ver como maximo 100 persona)
    num=libreria.pedir_rango("Numero de persona: ",1,100)
    contenido=peli+" - "+dia+" - "+str(num)+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("---- Pelicula ==>",peli)
def serie():
    # elejir nombre de la serie
    peli=libreria.pedir_peli("el barco / la casa de papel :")
    # que dia de la semana la voy a ver
    dia=libreria.pedir_dia("Ingrese dia: ")
    # cuantos la vamos a ver( solo se pueden ver como maximo 100 persona)
    num=libreria.pedir_rango("Numero de persona: ",1,100)
    contenido=peli+" - "+dia+" - "+str(num)+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("---- Serie ==>",peli)
def anime():
    # elejir nombre de Anime
    peli=libreria.pedir_peli("naruto / dragon ball :")
    # que dia de la semana la voy a ver
    dia=libreria.pedir_dia("Ingrese dia: ")
    # cuantos la vamos a ver( solo se pueden ver como maximo 100 persona)
    num=libreria.pedir_rango("Numero de persona: ",1,100)
    contenido=peli+" - "+dia+" - "+str(num)+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("---- Anime ==>",peli)
def verEstrenos():
    data=libreria.obtener_datos("info.txt")
    if(data!=""):
        print(data)
opc=0
max=5

while(opc!=max):
    print("------- E S T R E N O S  --------")
    print("- 1. Elejir Pelicula           --")
    print("- 2. Eleir Serie               --")
    print("- 3. Elejir Anime              --")
    print("- 4. Galeria De ESTRENOS       --")
    print("- 5. Salir                     --")
    print("---------------------------------")
    opc=libreria.pedir_rango("ingrese opcion: ",1,4)
    if(opc==1):
        pelicula()
    if(opc==2):
        serie()
    if(opc==3):
        anime()
    if(opc==4):
        verEstrenos()
    # fin if
# fin menu
print("--- ESTRENOS INOLVIDABLES ")