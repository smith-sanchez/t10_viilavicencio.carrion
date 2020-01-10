import libreria

def pedirAliSub():
    alimento=libreria.pedir_nombre("ingrese fruta/verdura: ")
    numero=libreria.pedir_numero("ingrese cantidad: ",1,100)
    contenido=alimento+"-"+str(numero)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print(" Se registro el alimento")
def VerDatosSub():
    data=libreria.obtener_datos("info.txt")
    if(data!=""):
        print(data)
    else:
        print("Archivo sin datos")

def fruta():
    opc=0
    max=3
    while (opc != max):
        print("######### FRUTA #######")
        print("# 1. Pedir fruta")
        print("# 2. Ver datos")
        print("# 3. Salir")
        opc = libreria.pedir_numero("Ingrese opcion:",1,3)
        if (opc == 1):
            pedirAliSub()
        if (opc == 2):
            VerDatosSub()

def verdura():
    opc=0
    max=3
    while (opc != max):
        print("######### VERDURA #######")
        print("# 1. Pedir verdura")
        print("# 2. Ver datos")
        print("# 3. Salir")
        opc = libreria.pedir_numero("Ingrese opcion:",1,3)
        if (opc == 1):
            pedirAliSub()
        if (opc == 2):
            VerDatosSub()

opc=0
max=3
while (opc != max):
    print("########## SALUD #########")
    print("# 1. FRUTAS")
    print("# 2. VERDURAS")
    print("# 3. SALIR")
    print("##########################")
    opc = libreria.pedir_numero("Ingrese Opcion:",1,3)
    if (opc == 1):
        fruta()
    if (opc == 2):
        verdura()
#fin_while

#fin_menu
print("*FIN DEL PROGRAMA*")
