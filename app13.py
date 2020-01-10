import libreria

def pedirReparacion():
    moto=libreria.pedir_nombre("Ingrese moto/AUTO: ")
    super=libreria.pedir_super("Ingrese super del motor:")
    contenido=moto+"-"+super+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print(" Se registro el vehiculo")
def VerDatosSub():
    data=libreria.obtener_datos("info.txt")
    if(data!=""):
        print(data)
    else:
        print("Archivo sin datos")

def repacionMoto():
    opc=0
    max=3
    while (opc != max):
        print("######### MOTO #######")
        print("# 1. Pedir Modelo Moto ")
        print("# 2. Ver datos  ")
        print("# 3. Salir")
        print("######################")
        opc = libreria.pedir_numero("Ingrese opcion:",1,3)
        if (opc == 1):
            pedirReparacion()
        if (opc == 2):
            VerDatosSub()

def repacionAuto():
    opc=0
    max=3
    while (opc != max):
        print("######### AUTO #######")
        print("# 1. Pedir Modelo Auto ")
        print("# 2. Ver datos  ")
        print("# 3. Salir")
        print("######################")
        opc = libreria.pedir_numero("Ingrese opcion:",1,3)
        if (opc == 1):
            pedirReparacion()
        if (opc == 2):
            VerDatosSub()

opc=0
max=3
while (opc != max):
    print("########## MECANICA #########")
    print("# 1. MOTO")
    print("# 2. AUTO")
    print("# 3. SALIR")
    print("##########################")
    opc = libreria.pedir_numero("Ingrese Opcion:",1,3)
    if (opc == 1):
        repacionMoto()
    if (opc == 2):
        repacionAuto()
#fin_while

#fin_menu
print("*FIN DEL PROGRAMA*")
