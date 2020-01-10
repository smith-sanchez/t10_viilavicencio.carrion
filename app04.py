import libreria
# Aplicacion para pedir nombre completo de una persona
def pedirNombre():
    # 1. Pedir solo nombres
    # 2. Pedir apellidos
    # 3. Guardar los datos en el archivo info.txt
    nombres = libreria.pedir_nombre("Ingrese nombre:")
    apellidos = libreria.pedir_nombre("Ingrese los apellidos:")
    contenido=nombres+"-"+apellidos +"\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Se ingreso el nombre completo con exito")

def verNombre():
    datos = libreria.obtener_datos("info.txt")
    if ( datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")

opc=0
max=3
while(opc != max):
    print("######### MENU ###########")
    print("1. Ingresar nombre        ")
    print("2. Ver el nombre ingresado")
    print("3. Salir")
    print("##########################")

    opc=libreria.pedir_numero("Ingresar Opcion:", 1, 3)

    if (opc == 1):
        pedirNombre()
    if (opc == 2):
        verNombre()

#fin_menu
print("*Fin del programa*")
