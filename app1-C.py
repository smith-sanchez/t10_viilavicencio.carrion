# menu pedir talla de un zapato
import libreria
def compraZapatilla():
    talla=libreria.pedir_rango(" Ingrese la talla: ", 30, 48)
    color=libreria.pedir_color(" color(blanco/negro): ")
    marca=libreria.pedir_marca(" Ingree la marca: ")
    contenido=str(talla) + "-" + color + "-" + marca + "\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("datos guardados")

def mostrarCompra():
    datos=libreria.obtener_datos("info.txt")
    if(datos!=""):
        print(datos)


opc=0
max=3
while(opc!=max):
    # mostrar menu de opciones
    print("==========  MENU  ==========")
    print("1: comprar zapatilla ")
    print("2: mostrar compra ")
    print("3: exit")
    print("============================")


    opc=libreria.pedir_rango("ingrese opcion: ",1,3)

    if( opc==1):
        compraZapatilla()
    if( opc==2):
        mostrarCompra()


    # fin_if
#fin_while
print("gracias por su compra.")
# fin_menu
