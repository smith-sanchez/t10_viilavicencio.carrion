#  menu donde puedas guardar la fechas de cumpleanos
import libreria
def agregarCumple():
    ano=libreria.pedir_ano("ingrese año: ")
    mes=libreria.pedir_mes("ingrese mes: ")
    dia=libreria.pedir_dia("ingrese dia: ")
    contenido=str(ano)+"-"+mes+"-"+dia+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print(">> fecha de cumpleaño guardado <<")
def galeriaCumple():
    datos=libreria.obtener_datos("info.txt")
    if(datos!=""):
        print(datos)


opc=0
max=3

while(opc!=max):
    print(">>>>>>>>>>>>>>>  MENU   >>>>>>>>>>>>>>>")
    print(">> 1: agregar cumpleaño: ")
    print(">> 2: ver galeria de cumpleaños: ")
    print(">> 3: salir ")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    opc=int(input("ingrese opcion: "))
    if(opc==1):
        agregarCumple()
    if(opc==2):
        galeriaCumple()
    # fin_ if
#fin while
print("guardaste una fecha importante")