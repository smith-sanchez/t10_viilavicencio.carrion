import libreria

def opcionA():
    # 1. Pedir fruta
    # 2. Pedir el numero de frutas que se desea
    # 3. Guardar los datos en el archivo info.txt
    fruta=libreria.pedir_nombre("ingrese fruta: ")
    numero=libreria.pedir_numero("ingrese cantidad: ",1,100)
    contenido=fruta+"-"+str(numero)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print(" Se registro la fruta")
def opcionB():
    data=libreria.obtener_datos("info.txt")
    if(data!=""):
        print(data)
    else:
        print("Archivo sin datos")

# Menu Generico
opc=0
max=3
while( opc != max):
    #1. Impresion del menu
    print("########### MENU ##########")
    print("1. Regristrar frutas ")
    print("2. Ver registro de frutas ")
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

