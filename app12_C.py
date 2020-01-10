# sub menu ----> formulas segun curso
import libreria
def multiplicacion():
    # pide numeros  enteros positivos
    num1=libreria.pedir_rango("== Ingrese 1° Numero: ",0,10000000000)
    num2=libreria.pedir_rango("== Ingrese 2° Numero: ",0,100000000000)
    multip=num1*num2
    contenido=str(num1)+" - "+str(num2)+" - "+str(multip)+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("== Se guardo la operacion")
def division():
    # pide numeros enteros positivos
    num1=libreria.pedir_rango("== Ingrese 1° Numero: ",0,1000000000000)
    num2=libreria.pedir_rango("== Ingrese 2° Numero: ",0,10000000000)
    div=num1/num2
    contenido=str(num1)+" - "+str(num2)+" - "+str(div)+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("== Se guardo la operacion")
def distancia():
    # pide numeros enteros positivos
    num1=libreria.pedir_rango("== Ingrese Velocidad: ",0,1000000000000)
    num2=libreria.pedir_rango("== Ingrese Tiempo: ",0,10000000000)
    div=num1/num2
    contenido=str(num1)+" - "+str(num2)+" - "+str(div)+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("== Se guardo la operacion")
def fuerza():
    # pide numeros enteros positivos
    num1=libreria.pedir_rango("== Ingrese Acceleracion: ",0,1000000000000)
    num2=libreria.pedir_rango("== Ingrese Masa: ",0,10000000000)
    div=num1*num2
    contenido=str(num1)+" - "+str(num2)+" - "+str(div)+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("== Se guardo la operacion")

def submenu():
    data=libreria.obtener_datos("info.txt")
    if(data!=""):
        print(data)
def mateF():
    # tiene formulas de algebra lineal
    opc = 0
    max = 4
    while (opc != max):
        print("---------M A T E M A T I C A ---------")
        print("1: Multiplicacion                   --")
        print("2: Division                         --")
        print("3: Ver menu                         --")
        print("4: salir                            --")
        print("--------------------------------------")

        opc = libreria.pedir_rango("ingrese opcion: ", 1, 4)
        if (opc == 1):
            multiplicacion()
        if (opc == 2):
            division()
        if (opc==3):
            submenu()
        # fin_ if
    print("Fin  del formulario --> Matematica")
def fisicaF():
    # tiene formulas de velocidad de un movil
        # tiene formulas de algebra lineal
    opc = 0
    max = 4
    while (opc != max):
        print("---------   F I S I C A      ---------")
        print("1: Distancia                        --")
        print("2: fuerza                           --")
        print("3: Ver menu                         --")
        print("4: salir                            --")
        print("--------------------------------------")

        opc = libreria.pedir_rango("ingrese opcion: ", 1, 4)
        if (opc == 1):
            distancia()
        if (opc == 2):
            fuerza()
        if (opc == 3):
            submenu()
        # fin_ if
    print("Fin  del formulario --> fisica")
opc=0
max=3
while(opc!=max):
    print("---------F O R M U L A S ---------")
    print("1: Matematica                   --")
    print("2: Fisica                       --")
    print("3: salir                        --")
    print("----------------------------------")

    opc = libreria.pedir_rango("ingrese opcion: ", 1, 3)
    if (opc == 1):
        mateF()
    if (opc == 2):
        fisicaF()

    # fin_ if
print("Fin  del formulario")