# sub menu --> puedes elejir segun la hora que estes( desayuno / almuerzo / cena )
import libreria
def ingresarplato():
    menu = libreria.pedir_marca("ingrese plato: ")
    postre = libreria.pedir_marcas("  Elija postre( gelatina / mazamorra ): ")
    cantidad = libreria.pedir_rango("ingrese cantidad: ",1,40)
    contenido = menu + " - " + postre + " - " +str(cantidad)+"\n"
    libreria.guardar_d("info.txt", contenido, "a")
    print(">>>> Se guardo su pedido ")
def verplato():
    data=libreria.obtener_datos("info.txt")
    if(data!=""):
        print(data)


def desayuno():
    opc = 0
    max = 3

    while (opc != max):
        print(">>>>>>>>>>>>>>> DESAYUNO  >>>>>>>>>>>>>>")
        print(">> 1: Ingresar plato                  >>")
        print(">> 2: Ver Desayuno                    >>")
        print(">> 3: salir                           >>")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        opc = libreria.pedir_rango(">>>>ingrese opcion: ", 1, 3)
        if (opc == 1):
            ingresarplato()
        if (opc == 2):
            verplato()


def almuerzo():
    opc = 0
    max = 3

    while (opc != max):
        print(">>>>>>>>>>>>>>> ALMUERZO  >>>>>>>>>>>>>>")
        print(">> 1: Ingresar plato                  >>")
        print(">> 2: Ver Desayuno                    >>")
        print(">> 3: salir                           >>")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        opc = libreria.pedir_rango(">>>>ingrese opcion: ", 1, 3)
        if (opc == 1):
            ingresarplato()
        if (opc == 2):
            verplato()


def cena():
    opc = 0
    max = 3

    while (opc != max):
        print(">>>>>>>>>>>>>>>   CENA    >>>>>>>>>>>>>>")
        print(">> 1: Ingresar plato                  >>")
        print(">> 2: Ver Desayuno                    >>")
        print(">> 3: salir                           >>")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        opc = libreria.pedir_rango(">>>>ingrese opcion: ", 1, 3)
        if (opc == 1):
            ingresarplato()
        if (opc == 2):
            verplato()


opc=0
max=4

while(opc!=max):
    print(">>>>>>>>>>>>>>>  MENU   >>>>>>>>>>>>>>>")
    print(">> 1: Desayuno                       >>")
    print(">> 2: Almuerzo                       >>")
    print(">> 3: Cena                           >>")
    print(">> 4: salir                          >>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    opc = libreria.pedir_rango(">>>>ingrese opcion: ", 1, 4)
    if (opc == 1):
        desayuno()
    if (opc == 2):
        almuerzo()
    if (opc == 3):
        cena()
print(">>>>lo estaremos esperando")
