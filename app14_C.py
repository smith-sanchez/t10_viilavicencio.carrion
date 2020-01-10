# sub menu ---->  hacer una apuesta
import libreria
def seleccionarequipo():
    # la apuesta es un numero positivo
    equipo=libreria.pedir_nombre("Ingrese equipo: ")
    num=libreria.pedir_rango("Ingrese apuesta: ",1 , 1000000000)
    nombre=libreria.pedir_nombre("Ingrese su nombre: ")
    contenido=equipo+" - "+str(num)+" - "+nombre+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print(">> Apuesta Guardada")
def galeriadeapuesta():
    datos=libreria.obtener_datos("info.txt")
    if(datos!=""):
        print(datos)


def agregarapuesta():
    opc = 0
    max = 3

    while (opc != max):
        print(">>>>>>>>>>>>>>>  AGREGAR APUESTA  >>>>>>>>>>>>>>")
        print(">> 1: Seleccionar Equipo                       >>")
        print(">> 2: ver galeria de Apuestas                 >>")
        print(">> 3: salir                                   >>")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        opc = int(input("ingrese opcion: "))
        if (opc == 1):
            seleccionarequipo()
        if (opc == 2):
            galeriadeapuesta()
        # fin_ if
opc=0
max=2

while(opc!=max):
    print(">>>>>>>>>>>>>>>  A P U E S T A   >>>>>>>>>>>>>>>")
    print(">> 1: Agregar Apuesta                         >>")
    print(">> 2: salir                                   >>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    opc=int(input("ingrese opcion: "))
    if(opc==1):
        agregarapuesta()
    # fin_ if
#fin while
print("Fin apuesta")