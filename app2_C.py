# menu sobre la compra de una pasta dental
import libreria
def comprarPasta():
    marca=libreria.pedir_marca("ingrese la marca: ")
    cantidad=libreria.pedir_entero(" ingrese cantidad: ")
    tamano=libreria.pedir_tamano("ingrese tamaño(grande/pequeño): ")
    contenido=marca+"-"+str(cantidad)+"-"+tamano+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("se guardo la compra")
def mostrarCompras():
    datos=libreria.obtener_datos("info.txt")
    if(datos!=""):
        print(datos)

opc=0
max=3

while(opc!=max):
    print("--------- MENU ---------")
    print("1: comprar pasta dental")
    print("2: mostra compra ")
    print("3: salir ")
    print("------------------------")

    opc=int(input("ingrese opcion: "))
    if (opc==1):
        comprarPasta()
    if (opc==2):
        mostrarCompras()
    # fin_ if
print("gracias por su compra...")