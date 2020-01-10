import libreria

def pedirProm():
    promedio=libreria.pedir_numero("ingrese promedio:",0,20)
    contenido=str(promedio)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print(" Se ingreso el promedio")
def VerDatosSub():
    data=libreria.obtener_datos("info.txt")
    if(data!=""):
        print(data)
    else:
        print("Archivo sin datos")

def prom01():
    opc=0
    max=3
    while (opc != max):
        print("######### PROMEDIO-01 #######")
        print("# 1. Pedir promedio 01")
        print("# 2. Ver datos")
        print("# 3. Salir")
        opc = libreria.pedir_numero("Ingrese opcion:",1,3)
        if (opc == 1):
            pedirProm()
        if (opc == 2):
            VerDatosSub()

def prom02():
    opc=0
    max=3
    while (opc != max):
        print("######### PROMEDIO-02 #######")
        print("# 1. Pedir promedio 02")
        print("# 2. Ver datos")
        print("# 3. Salir")
        opc = libreria.pedir_numero("Ingrese opcion:",1,3)
        if (opc == 1):
            pedirProm()
        if (opc == 2):
            VerDatosSub()

opc=0
max=3
while (opc != max):
    print("###### NOTAS FINALES ######")
    print("# 1. PROMEDIO-01")
    print("# 2. PROMEDIO-02")
    print("# 3. SALIR")
    print("##########################")
    opc = libreria.pedir_numero("Ingrese Opcion:",1,3)
    if (opc == 1):
        prom01()
    if (opc == 2):
        prom02()
#fin_while

#fin_menu
print("*FIN DEL PROGRAMA*")
