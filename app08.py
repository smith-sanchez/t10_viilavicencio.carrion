import libreria
# Aplicacion para pedir el nombre de los cinco primeros planetas
def pedirPlaneta():
    # 1. Pedir nombre del planeta      Mercurio-Venus-Tierra-Marte-Jupiter
    # 2. Guardar los datos en el archivo info.txt
    planeta = libreria.pedir_planeta("Ingrese nombre del paneta:")
    contenido=planeta+"\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Se registro el nombre del planeta")

# Aplicacion para pedir el unico satelite de la tierra
def pedirSatelite():
    # 1. Pedir nombre del unico satelite que tiene la tierra  ->   Luna
    # 2. Guardar los datos en el archivo info.txt
    satelite = libreria.pedir_satelite("Ingrese nombre del satelite:")
    contenido=satelite+"\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Se registro en nombre del satelite")

def verRegistro():
    datos = libreria.obtener_datos("info.txt")
    if ( datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")

opc=0
max=4
while(opc != max):
    # 1. Impresion del menu
    print("########## MENU ###########")
    print("1. Pedir nombre de paneta  ")
    print("2. Pedir nombre del satelite ")
    print("3. Ver datos registrados")
    print("4. Salir")
    print("###########################")

    opc=libreria.pedir_numero("Ingresar Opcion:", 1, 4)

    if (opc == 1):
        pedirPlaneta()
    if (opc == 2):
        pedirSatelite()
    if (opc == 3):
        verRegistro()

#fin_menu
print("*Fin del programa*")
