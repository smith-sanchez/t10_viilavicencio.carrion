import libreria

def opcionA():
    # 1. Pedir el modelo de la moto que se desea comprar
    # 2. Pedir precio de la moto
    # 3. Pedir cantidad
    # 4. Guardar los datos en el archivo info.txt
    moto=libreria.pedir_nombre("Ingrese modelo de moto: ")
    precio=libreria.pedir_numero("Ingrese precio:",2000,8000)
    cantidad=libreria.pedir_numero("Ingrese cantidad: ",1,10)
    contenido=moto+"-"+str(precio)+"-"+str(cantidad)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print(" Se registro la compra")
def opcionB():
    data=libreria.obtener_datos("info.txt")
    if(data!=""):
        print(data)


# Menu Generico
opc=0
max=3
while( opc != max):
    #1. Impresion del menu
    print("########### MENU ##########")
    print("1. Eligir modelo de la moto")
    print("2. Ver la compra realizada ")
    print("3. Salir")
    print("###########################")

    #2. Eleccion del opcion del menu
    opc=libreria.pedir_numero("Ingrese Opcion:",1,3)

    #3. Mapeo de las opciones
    if ( opc == 1 ):
        opcionA()
    if ( opc == 2 ):
        opcionB()

#fin_while

print(" *Fin del menu* ")
