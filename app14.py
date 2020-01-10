import libreria

def realizarViaje():
    viaje=libreria.pedir_viaje("El viaje se realizara a: ")
    precio=libreria.pedir_numero("Ingrese el precio del viaje:",50,150)
    contenido=viaje+"-"+str(precio)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print(" Se registro el viaje")
def VerDatosSub():
    data=libreria.obtener_datos("info.txt")
    if(data!=""):
        print(data)
    else:
        print("Archivo sin datos")

def viajeTierra():
    opc=0
    max=3
    while (opc != max):
        print("############# OPCION-01 ############")
        print("# 1. Pedir tipo de viaje   ->Tierra ")
        print("# 2. Ver datos  ")
        print("# 3. Salir")
        print("######################")
        opc = libreria.pedir_numero("Ingrese opcion:",1,3)
        if (opc == 1):
            realizarViaje()
        if (opc == 2):
            VerDatosSub()

def viajeAire():
    opc=0
    max=3
    while (opc != max):
        print("############# OPCION-02 ############")
        print("# 1. Pedir tipo de viaje   ->Aire ")
        print("# 2. Ver datos  ")
        print("# 3. Salir")
        print("######################")
        opc = libreria.pedir_numero("Ingrese opcion:",1,3)
        if (opc == 1):
            realizarViaje()
        if (opc == 2):
            VerDatosSub()

def viajeAgua():
    opc=0
    max=3
    while (opc != max):
        print("############# OPCION-03 ############")
        print("# 1. Pedir tipo de viaje   ->Agua ")
        print("# 2. Ver datos  ")
        print("# 3. Salir")
        print("######################")
        opc = libreria.pedir_numero("Ingrese opcion:",1,3)
        if (opc == 1):
            realizarViaje()
        if (opc == 2):
            VerDatosSub()


opc=0
max=4
while (opc != max):
    print("########## VIAJAR #########")
    print("# 1. TIERRA")
    print("# 2. AIRE")
    print("# 3. AGUA")
    print("# 4. SALIR")
    print("##########################")
    opc = libreria.pedir_numero("Ingrese Opcion:",1,4)
    if (opc == 1):
        viajeTierra()
    if (opc == 2):
        viajeAire()
    if (opc == 3):
        viajeAgua()
#fin_while

#fin_menu
print("*FIN DEL PROGRAMA*")
