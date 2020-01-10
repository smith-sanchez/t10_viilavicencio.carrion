import libreria
# Aplicacion para pedir una pequeña informacion de una universidad
def pedirUni():
    # 1. Pedir nombre de la universidad
    # 2. Pedir direccion de la universidad
    # 3. Pedir la cantidad de carreras que cuenta la universidad
    # 4. Guardar los datos en el archivo info.txt
    nombre = libreria.pedir_nombre("Ingrese nombre de la universidad:")
    direccion = libreria.pedir_nombre("Ingrese direccion de la universidad:")
    cantidad = libreria.pedir_numero("Ingrese la cantidad de carreras:",1,80)
    contenido=nombre+"-"+direccion+"-"+str(cantidad)+"\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Se ingreso una pequeña informacion de la universidad")

def verInf():
    datos = libreria.obtener_datos("info.txt")
    if ( datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")

opc=0
max=3
while(opc != max):
    # 1. Impresion del menu
    print("######## MENU ##########")
    print("1. Pedir Universidad    ")
    print("2. Ver informacion      ")
    print("3. Salir")
    print("########################")

    opc=libreria.pedir_numero("Ingresar Opcion:", 1, 3)

    if (opc == 1):
        pedirUni()
    if (opc == 2):
        verInf()

#fin_menu
print("*Fin del programa*")
