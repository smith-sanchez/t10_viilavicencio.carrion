import libreria
# Aplicacion para realizar una operacion matematica
def Operacion():
    # 1. Pedir n1,n2,n3 y n4 para luego realizar la operacion daentre ellos
    # 2. Guardar los datos en el archivo info.txt
    n1=libreria.pedir_numero("Ingrese primer numero:",0,999999)
    n2=libreria.pedir_numero("Ingrese segundo numero:",0,999999)
    n3=libreria.pedir_numero("ingrese tercer numero:",0,20)
    n4=libreria.pedir_numero("Ingrese cuarto numero:",0,4)
    contenido="El resultado es:" + str((n1*n2)+(n3**n4)) +"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("Operacion con exito")

def verRes():
    datos = libreria.obtener_datos("info.txt")
    if ( datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")
opc=0
max=3
while opc != max :
    # 1. Impresion del menu
    print("#######################")
    print(" 1. Realizar operacion ")
    print(" 2. Ver datos          ")
    print(" 3. Salir")
    print("################")

    opc=libreria.pedir_numero("Ingresar opcion:",1,3)

    if (opc == 1):
        Operacion()
    if (opc == 2):
        verRes()

#Fin del menu
print("*Fin del programa*")
