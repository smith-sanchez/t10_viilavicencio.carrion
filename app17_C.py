import libreria
def favorito():
    prof=libreria.pedir_prof("ingrese un profesor(figueroa - fernando - coronado ): ")
    curso=libreria.pedir_curso("ingrese un curso( analisis - programacion + matematica): ")
    escala=libreria.pedir_rango("ingrese escala( 1 - 5 ): ",1,5)
    contenido=prof+"-"+curso+"-"+str(escala)+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print(" se guardo en favoritos ")
def verFavorito():
    datos=libreria.obtener_datos("info.txt")
    if(datos!=""):
        print(datos)


def encuesta():
    opc = 0
    max = 3
    while (opc != max):
        print("+++++++++   E N C U E S T A   ++++++++++++++")
        print("+ 1. Elejir curso  y profesor favorito     +")
        print("+ 2. Ver favoritos                         +")
        print("+ 3. Salir")
        print("++++++++++++++++++++++++++++++++++++++++++++")
        opc = libreria.pedir_rango("++++ ingrese opcion: ", 1, 3)
        if (opc == 1):
            favorito()
        if (opc == 2):
            verFavorito()


opc=0
max=2
while(opc!=max):
    print("+++++++++++   E N C U E S T A   ++++++++++++")
    print("+ 1. Comenzar Encuesta                     +")
    print("+ 2. Salir")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    opc=libreria.pedir_rango("++++ ingrese opcion: ",1,2)
    if (opc==1):
        encuesta()
    # fin_if
# fin_while

print("++++ BUENA ELECCION...")