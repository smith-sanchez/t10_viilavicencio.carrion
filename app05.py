import libreria
# Aplicacion para pedir carrera
def pedirCarrera():
    # 1. Pedir carrera que solo pertencen a la facultad de FACFyM
    # 2. Guardar los datos en el archivo info.txt
    carrera = libreria.pedir_carrera("Ingrese carrera:")
    contenido=carrera +"\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Se ingreso la carrera")

def verCarrera():
    datos = libreria.obtener_datos("info.txt")
    if ( datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")

opc=0
max=3
while(opc != max):
    # 1. Impresion del menu
    print("######### MENU ###########")
    print("1. Ingrese carrera        ")
    print("2. Ver carrera ingresada  ")
    print("3. Salir")
    print("##########################")

    opc=libreria.pedir_numero("Ingresar Opcion:", 1, 3)

    if (opc == 1):
        pedirCarrera()
    if (opc == 2):
        verCarrera()

#fin_menu
print("*Fin del programa*")
