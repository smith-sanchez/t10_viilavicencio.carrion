# menu donde puedes pedir postre y menu
import libreria
def agregarMenu():
    menu=libreria.pedir_marca("ingrese plato: ")
    postre=libreria.pedir_marcas("  Elija postre( gelatina / mazamorra ): ")
    condic=libreria.pedir_marcas_condic(" desayuo / almuerzo / cena: ")
    contenido=menu+" - "+postre+" - "+condic+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print(">>>> Se guardo su pedido ")
def verMenu():
    data=libreria.obtener_datos("info.txt")
    if(data!=""):
        print(data)
opc=0
max=3

while(opc!=max):
    print(">>>>>>>>>>>>>>>  MENU   >>>>>>>>>>>>>>>")
    print(">> 1: agregar menu                   >>")
    print(">> 2: ver menu                       >>")
    print(">> 3: salir                          >>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    opc = libreria.pedir_rango(">>>>ingrese opcion: ", 1, 3)
    if (opc == 1):
        agregarMenu()
    if (opc == 2):
        verMenu()
print(">>>>lo estaremos esperando")
