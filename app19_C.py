import libreria
def ingJuga():
    # ingresar jugador que va a entra a jugar
    nombre=libreria.pedir_marca("-- Ingrese jugador: ")
    num=libreria.pedir_rango("-- Numero de camiseta: ",1,100)
    contenido=nombre+" - "+str(num)+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("-- ingreso ",nombre,", camiseta",num)
def susJuga():
    # ingresar el jugador que va a salir
    nombre=libreria.pedir_marca("-- Ingrese jugador: ")
    num=libreria.pedir_rango("-- Numero de camiseta: ",1,100)
    contenido=nombre+" - "+str(num)+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("-- Salio ",nombre,", camiseta",num)
def verSusti():
    data=libreria.obtener_datos("info.txt")
    if(data!=""):
        print(data)


def insusti():
    opc = 0
    max = 4

    while (opc != max):
        print("------- S U S T I T U C I O N ------")
        print("1: Ingresar Jugador               --")
        print("2: Sustituir Jugador              --")
        print("3: Ver Sustitucion                --")
        print("4: Salir")
        print("------------------------------------")
        opc = libreria.pedir_rango("-- Ingrese opcion: ", 1, 4)
        if (opc == 1):
            ingJuga()
        if (opc == 2):
            susJuga()
        if (opc == 3):
            verSusti()
        # Fin_if
    # fin_while
    print("-- Fin Sustitucion")


opc=0
max=2

while(opc!=max):
    print("------- S U S T I T U C I O N ------")
    print("1: Iniciar Sustitucion            --")
    print("2: Desacer Sustitucion            --")
    print("------------------------------------")
    opc=libreria.pedir_rango("-- Ingrese opcion: ",1,4)
    if(opc==1):
        insusti()
    # Fin_if
#fin_while
print("-- Fin Sustitucion")
