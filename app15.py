import libreria

def eligirHab():
    habitacion=libreria.pedir_habitacion("Ingresar tipo de habitacion: ")
    precio=libreria.pedir_numero("Ingrese el precio de esta habitacion:",50,200)  #SE pedira el precio por hora
    contenido=habitacion+"-"+str(precio)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print(" Se registro los datos")
def VerDatosSub():
    data=libreria.obtener_datos("info.txt")
    if(data!=""):
        print(data)
    else:
        print("Archivo sin datos")

def hotCielo():
    opc=0
    max=3
    while (opc != max):
        print("############ Hotel Cielo ###########")
        print("# 1. Pedir tipo de habitacion   ")
        print("# 2. Ver datos  ")
        print("# 3. Salir")
        print("######################")
        opc = libreria.pedir_numero("Ingrese opcion:",1,3)
        if (opc == 1):
            eligirHab()
        if (opc == 2):
            VerDatosSub()

def hotEstrellas():
    opc=0
    max=3
    while (opc != max):
        print("######## Hotel Estrellas #########")
        print("# 1. Pedir tipo de habitacion ")
        print("# 2. Ver datos  ")
        print("# 3. Salir")
        print("######################")
        opc = libreria.pedir_numero("Ingrese opcion:",1,3)
        if (opc == 1):
            eligirHab()
        if (opc == 2):
            VerDatosSub()


opc=0
max=3
while (opc != max):
    print("######## HOSPEDAJE ########")
    print("# 1. HOTEL CIELO")
    print("# 2. HOTEL ESTRELLAS")
    print("# 3. SALIR")
    print("##########################")
    opc = libreria.pedir_numero("Ingrese Opcion:",1,3)
    if (opc == 1):
        hotCielo()
    if (opc == 2):
        hotEstrellas()
#fin_while

#fin_menu
print("*FIN DEL PROGRAMA*")
