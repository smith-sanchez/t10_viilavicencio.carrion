import libreria
# Aplicacion para pedir marca de celular mas reconocibles y de alto precio
def marcaCelular():
    # 1. Pedir marca celular    SAMSUNG-LG-IPHONE-HUAWEI
    # 2. Guardar los datos en el archivo info.txt
    celular = libreria.pedir_celular("Ingrese marca de celular:")
    precio = libreria.pedir_numero("ingrese el precio del celular:",1000,3000)
    contenido=celular+"-"+str(precio)+"\n"
    libreria.guardar_datos("info.txt", contenido, "a")
    print("Se ingreso la marca del celular")

def verCelular():
    datos = libreria.obtener_datos("info.txt")
    if ( datos != ""):
        print(datos)
    else:
        print("Archivo sin datos")

opc=0
max=3
while(opc != max):
    # 1. Impresion del menu
    print("########## MENU ###########")
    print("1. Ingrese marca de celular")
    print("2. Ver celular registrado  ")
    print("3. Salir")
    print("###########################")

    opc=libreria.pedir_numero("Ingresar Opcion:", 1, 3)

    if (opc == 1):
        marcaCelular()
    if (opc == 2):
        verCelular()

#fin_menu
print("*Fin del programa*")
