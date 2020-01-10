import libreria
# Aplicacion para realizar una multiplicacion
def Multiplicar():
    # 1. Pedir n1 y n2 para luego realizar la multiplicacion entre ellos
    # 2. Guardar los datos en el archivo info.txt
    n1=libreria.pedir_numero("Ingrese primer numero:",0,99999)
    n2=libreria.pedir_numero("Ingrese segundo numero:",0,99999)
    contenido="El producto es:" + str(n1*n2) +"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("Multiplicacion con exito")

# Aplicacion para realizar una division
def Dividir():
    # 1. Pedir n1 y n2 para luego realizar la divison entre ellos
    # 2. Guardar los datos en el archivo info.txt
    n1=libreria.pedir_numero("ingrese primer numero:",0,99999)
    n2=libreria.pedir_numero("Ingrese segundo numero:",0,99999)
    contenido="La division es:"+str(n1/n2) +"\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Division con exito")

def verRes():
    datos = libreria.obtener_datos("info.txt")
    if ( datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")
opc=0
max=4
while opc != max :
    # 1. Impresion del menu
    print("################")
    print(" 1. Multiplicar ")
    print(" 2. Dividir     ")
    print(" 3. Ver datos   ")
    print(" 4. Salir")
    print("################")

    opc=libreria.pedir_numero("Ingresar opcion:",1,4)

    if (opc == 1):
        Multiplicar()
    if (opc == 2):
        Dividir()
    if (opc == 3):
        verRes()

#Fin del menu
print("*Fin del programa*")
