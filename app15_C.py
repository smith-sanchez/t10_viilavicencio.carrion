# sub menu ----> hacer compra de sapatillas o polo
import libreria

def elejirZapatilla():
    talla = libreria.pedir_rango(" Ingrese la talla: ", 10, 50)
    color = libreria.pedir_color(" color(blanco/negro): ")
    marca = libreria.pedir_marca(" Ingrese la marca: ")
    contenido = str(talla) + "-" + color + "-" + marca + "\n"
    libreria.guardar_d("info.txt", contenido, "a")
    print("datos guardados")


def mostraCompra():
    datos=libreria.obtener_datos("info.txt")
    if(datos!=""):
        print(datos)

def elejirPolo():
    talla = libreria.pedir_rango(" Ingrese la talla: ", 10, 48)
    color = libreria.pedir_color(" color(blanco/negro): ")
    marca = libreria.pedir_marca(" Ingrese la marca: ")
    contenido = str(talla) + "-" + color + "-" + marca + "\n"
    libreria.guardar_d("info.txt", contenido, "a")
    print("datos guardados")



def compraZapatilla():
    opc = 0
    max = 3
    while (opc != max):
        # mostrar menu de opciones
        print("========== ZAPATILLAS  ==========")
        print("1: Elejir Zapatilla            ==")
        print("2: Ver Compra                  ==")
        print("3: exit                        ==")
        print("=================================")

        opc = libreria.pedir_rango("ingrese opcion: ", 1, 3)

        if (opc == 1):
            elejirZapatilla()
        if (opc == 2):
            mostraCompra()


def compraPolo():
    opc = 0
    max = 3
    while (opc != max):
        # mostrar menu de opciones
        print("==========  POLO  ==========")
        print("1: Elejir Polo            ==")
        print("2: Mostrar Compra           ==")
        print("3: exit                   ==")
        print("============================")

        opc = libreria.pedir_rango("ingrese opcion: ", 1, 3)

        if (opc == 1):
            elejirPolo()
        if (opc == 2):
            mostrarCompra()


opc=0
max=3
while(opc!=max):
    # mostrar menu de opciones
    print("==========  MENU  ==========")
    print("1: comprar zapatilla      ==")
    print("2: Comprar polo           ==")
    print("3: exit                   ==")
    print("============================")


    opc=libreria.pedir_rango("ingrese opcion: ",1,3)

    if( opc==1):
        compraZapatilla()
    if( opc==2):
        compraPolo()


    # fin_if
#fin_while
print("gracias por su compra.")
# fin_menu
