import libreria
# Aplicacion para pedir el nombre de un dia
def pedirDia():
    # 1. Pedir nombre del dia
    # 2. Guardar los datos en el archivo info.txt
    dia = libreria.pedir_dia("Ingrese dia:")
    contenido=dia +"\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Se ingreso el nombre del dia correctamente")

def verDia():
    datos = libreria.obtener_datos("info.txt")
    if ( datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")

opc=0
max=3
while(opc != max):
    print("######## MENU ##########")
    print("1. Pedir Dia           ")
    print("2. Ver el dia ingresado")
    print("3. Salir")
    print("########################")

    opc=libreria.pedir_numero("Ingresar Opcion:", 1, 3)

    if (opc == 1):
        pedirDia()
    if (opc == 2):
        verDia()

#fin_menu
print("*Fin del programa*")
