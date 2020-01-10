import libreria
def colorfavorita():
    color1 = libreria.pedir_colores("ingrese su 1° color(blanco/negro/amarillo): ")
    color2 = libreria.pedir_colores("ingrese su 2° color(rojo/rosado/dorado): ")
    color3 = libreria.pedir_colores("ingrese su 3° color(verde/celeste/azul): ")
    contenido = color1 + "=" + color2 + "=" + color3 + "\n"
    libreria.guardar_d("info.txt", contenido, "a")
    print("se guardaron tus colres favoritas ")
def vercolores():
    data = libreria.obtener_datos("info.txt")
    if (data != ""):
        print(data)

def cartuchera():
    opc = 0
    max = 3

    while (opc != max):
        print(">>>>>>>>>>>>>>>  CARTUCHERA   >>>>>>>>>>>>>>>")
        print(">> 1: agregar colores favoritos:     >>")
        print(">> 2: ver galeria de colores:        >>")
        print(">> 3: salir                          >>")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        opc = libreria.pedir_rango(">>>>ingrese opcion: ", 1, 3)
        if (opc == 1):
            colorfavorita()
        if (opc == 2):
            vercolores()


opc=0
max=2

while(opc!=max):
    print(">>>>>>>>>>>>>>>  MENU   >>>>>>>>>>>>>>>")
    print(">> 1: Ver cartuchera de colores      >>")
    print(">> 2: salir                          >>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    opc=libreria.pedir_rango(">>>>ingrese opcion: ",1,3)
    if(opc==1):
        cartuchera()

print(">>>>elige nuevas colores...")