import libreria
def arpersonal():
    # se registrara nombre - escuela - edad
    # la escuela tiene que ser solo FACFyM --> ing. electronica
    nombre=libreria.pedir_nombre("== Ingrese Nombre: ")
    escuela=libreria.pedir_escuela("== Ingrese Escuela: ")
    edad=libreria.pedir_edad("== Ingrese edad: ",0,120)
    contenido=nombre+" - "+escuela+" - "+str(edad)+" - "+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("== Registro universitario guardado ")
def arnacional():
    # se registrara con telefono - nombre - edad - dni
    # el telefono tiene que ser peruano --> 925780779
    # el  dni tiene que tener la forma --> 74286646
    telefono = libreria.pedir_telefono("== Ingrese telefono: ")
    nombre = libreria.pedir_nombre("== Ingrese nombre: ")
    edad = libreria.pedir_edad("== Ingrese edad: ", 0, 120)
    dni = libreria.pedir_dni("== Ingrese DNI: ")
    contenido = str(telefono) + " - " + nombre + " - " + str(edad) + " - " + str(dni) + "\n"
    libreria.guardar_d("info.txt", contenido, "a")
    print("== Registro personal guardado ")

def verregistro():

    data=libreria.obtener_datos("info.txt")
    if(data!=""):
        print(data)
def registroInt():
    opc = 0
    max = 3
    while (opc != max):
        print("======== MENU DE REGISTRO =========")
        print("== 1. Agregar Registro Personal  ==")
        print("== 2. Ver Registro Personal      ==")
        print("== 3. Salir                      ==")
        print("===================================")
        opc = libreria.pedir_rango("ingrese opcion: ", 1, 3)
        if (opc == 1):
            arpersonal()
        if (opc == 2):
            verregistro()

def registroNacional():
    opc = 0
    max = 3
    while (opc != max):
        print("======== MENU DE REGISTRO =========")
        print("== 1. Agregar Registro Nacional  ==")
        print("== 2. Ver Registro Nacional      ==")
        print("== 3. Salir                      ==")
        print("===================================")
        opc = libreria.pedir_rango("ingrese opcion: ", 1, 3)
        if (opc == 1):
            arnacional()
        if (opc == 2):
            verregistro()




opc=0
max=4
while(opc!=max):
    print("======== MENU DE REGISTRO =========")
    print("== 1. Registro Personal          ==")
    print("== 2. Registro Universitario     ==")
    print("== 3. Ver Registro               ==")
    print("== 4. Salir                      ==")
    print("===================================")
    opc=libreria.pedir_rango("ingrese opcion: ",1,4)
    if (opc==1):
        registroInt()
    if (opc==2):
        registroNacional()
    if(opc==3):
        verRegistro()
    # fin if
#fin while
print("== Fin del registro")
