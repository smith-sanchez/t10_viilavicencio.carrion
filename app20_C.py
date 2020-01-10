import libreria
def comprarPasta():
    # se ingresa la marca del producto
    marca=libreria.pedir_marca("ingrese la marca: ")
    # se ingresa la cantidad del producto
    cantidad=libreria.pedir_entero(" ingrese cantidad: ")
    # silo desea grande o pequeño
    tamano=libreria.pedir_tamano("ingrese tamaño(grande/pequeño): ")
    contenido=marca+"-"+str(cantidad)+"-"+tamano+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("se guardo la compra")
def mostrarCompras():
    datos=libreria.obtener_datos("info.txt")
    if(datos!=""):
        print(datos)

def iniciarcompra():
    opc = 0
    max = 3

    while (opc != max):
        print("--------- MENU ---------")
        print("1: Comprar            --")
        print("2: mostra compra      --")
        print("3: salir              --")
        print("------------------------")

        opc = int(input("ingrese opcion: "))
        if (opc == 1):
            comprarPasta()
        if (opc == 2):
            mostrarCompras()
        # fin_ if
    print("gracias por su compra...")
opc=0
max=2

while(opc!=max):
    print("--------- MENU ---------")
    print("1: Iniciar Compra")
    print("2: salir              --")
    print("------------------------")

    opc=libreria.pedir_rango("ingrese opcion: ")
    if (opc==1):
        iniciarcompra()

    # fin_ if
print("gracias por su compra...")