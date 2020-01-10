import libreria

def pedirNota():
    promedio=libreria.pedir_numero("ingrese nota:",0,20)
    contenido=str(promedio)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print(" Se ingreso la nota")
def VerDatosSub():
    data=libreria.obtener_datos("info.txt")
    if(data!=""):
        print(data)
    else:
        print("Archivo sin datos")

def nota01():
    opc=0
    max=3
    while (opc != max):
        print("######### NOTA-01 #######")
        print("# 1. Pedir nota 01")
        print("# 2. Ver datos")
        print("# 3. Salir")
        opc = libreria.pedir_numero("Ingrese opcion:",1,3)
        if (opc == 1):
            pedirNota()
        if (opc == 2):
            VerDatosSub()

def nota02():
    opc=0
    max=3
    while (opc != max):
        print("######### PROMEDIO-02 #######")
        print("# 1. Pedir nota 02")
        print("# 2. Ver datos")
        print("# 3. Salir")
        opc = libreria.pedir_numero("Ingrese opcion:",1,3)
        if (opc == 1):
            pedirNota()
        if (opc == 2):
            VerDatosSub()

opc=0
max=3
while (opc != max):
    print("###### NOTAS FINALES ######")
    print("# 1. NOTA-01")
    print("# 2. NOTA-02")
    print("# 3. SALIR")
    print("##########################")
    opc = libreria.pedir_numero("Ingrese Opcion:",1,3)
    if (opc == 1):
        nota01()
    if (opc == 2):
        nota02()
#fin_while

#fin_menu
print("*FIN DEL PROGRAMA*")
