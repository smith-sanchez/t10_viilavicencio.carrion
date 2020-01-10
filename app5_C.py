# menu donde puedes guardar tu curso favorito y profesor favorito
# y que puntaje le das en escala del 1 al 5
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

opc=0
max=3
while(opc!=max):
    print("++++++++++++++++  MENU  ++++++++++++++++++++")
    print("+ 1. Elejir curso  y profesor favorito     +")
    print("+ 2. Ver favoritos                         +")
    print("+ 3. Salir")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    opc=libreria.pedir_rango("++++ ingrese opcion: ",1,3)
    if (opc==1):
        favorito()
    if (opc==2):
        verFavorito()

print("++++ BUENA ELECCION...")