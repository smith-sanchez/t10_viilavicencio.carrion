# menu donde puedes hacer operaciones con dos numeros
import libreria

def multiplicarP():
    num1=libreria.pedir_rango("== Ingrese 1° Numero: ",0,10000000000)
    num2=libreria.pedir_rango("== Ingrese 1° Numero: ",0,100000000000)
    multip=num1*num2
    contenido=str(num1)+" - "+str(num2)+" - "+str(multip)+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("== Se guardo la operacion")
def dividirP():
    num1=libreria.pedir_rango("== Ingrese 1° Numero: ",0,1000000000000)
    num2=libreria.pedir_rango("== Ingrese 1° Numero: ",0,10000000000)
    div=num1/num2
    contenido=str(num1)+" - "+str(num2)+" - "+str(div)+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("== Se guardo la operacion")
def potenciaP():
    num1=libreria.pedir_rango("== Ingrese 1° Numero: ",0,1000000000000000)
    num2=libreria.pedir_rango("== Ingrese 1° Numero: ",0,1000000000000000)
    pot=num1**num2
    contenido=str(num1)+" - "+str(num2)+" - "+str(pot)+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("== Se guardo la operacion")
def sumarP():
    num1=libreria.pedir_rango("== Ingrese 1° Numero: ",0,1000000000000000000)
    num2=libreria.pedir_rango("== Ingrese 1° Numero: ",0,100000000000)
    sumar=num1+num2
    contenido=str(num1)+" - "+str(num2)+" - "+str(sumar)+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("== Se guardo la operacion")
def restarP():

    num1=libreria.pedir_rango("== Ingrese 1° Numero: ",0,100000000000000)
    num2=libreria.pedir_rango("== Ingrese 1° Numero: ",0,100000000000000)
    res=num1-num2
    contenido=str(num1)+" - "+str(num2)+" - "+str(res)+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("== Se guardo la operacion")
def verMenu():
    data=libreria.obtener_datos("info.txt")
    if(data!=""):
        print(data)
opc=0
max=7
while(opc!=max):
    # mostrar menu de opciones
    print("==========  MENU  ==========")
    print("1: Multiplicar            ==")
    print("2: Dividir                ==")
    print("3: Potencia               ==")
    print("4: Sumar                  ==")
    print("5: Restar                 ==")
    print("6: Mostrar Menu           ==")
    print("7: Salir                  ==")
    print("============================")


    opc=libreria.pedir_rango("ingrese opcion: ",1,7)

    if( opc==1):
        multiplicarP()
    if( opc==2):
        dividirP()
    if (opc == 3):
        potenciaP()
    if (opc == 4):
        sumarP()
    if (opc == 5):
        restarP()
    if (opc == 6):
        verMenuP()
    # fin_if
#fin_while
print("== Fin Operacion")
# fin_menu
