# submenu --> Estrenos de peliculas
import libreria
def  verDatosub():
    datos=libreria.obtener_datos("info.txt")
    if(datos!=""):
        print(datos)

def ingresarSub():
    peli=libreria.pedir_nombre("-- Ingrese Pelicula: ")
    cant=libreria.pedir_rango("-- Ingrese cantidad de pesonas: ",1,100)
    dia=libreria.pedir_dia("-- Ingrese el dia: ")
    contenido=peli+"-"+str(cant)+" - "+dia+"\n"
    libreria.guardar_d("info.txt",contenido,"a")
    print("--SE gurdaro los datos ")
def terrorP():
    opc=0
    max=3
    while(opc!=max):
        print("-------  T E R R O R   --------")
        print("- 1. Ingresar Pelicula       --")
        print("- 2. Ver Datos               --")
        print("- 3. Salir                   --")
        print("-------------------------------")
        opc = libreria.pedir_rango("ingrese opcion: ", 1, 3)
        if (opc == 1):
            ingresarSub()
        if (opc == 2):
            verDatosub()
        # fin if

def accionP():
    opc=0
    max=3
    while(opc!=max):
        print("-------  A C C I O N   --------")
        print("- 1. Ingresar Pelicula       --")
        print("- 2. Ver Datos               --")
        print("- 3. Salir                   --")
        print("-------------------------------")
        opc = libreria.pedir_rango("ingrese opcion: ", 1, 3)
        if (opc == 1):
            ingresarSub()
        if (opc == 2):
            verDatosub()
        # fin if

def romanticasP():
        opc = 0
        max = 3
        while (opc != max):
            print("------- R O M A N T I C A S --------")
            print("- 1. Ingresar Pelicula            --")
            print("- 2. Ver Datos                    --")
            print("- 3. Salir                        --")
            print("-------------------------------------")
            opc = libreria.pedir_rango("ingrese opcion: ", 1, 3)
            if (opc == 1):
                ingresarSub()
            if (opc == 2):
                verDatosub()
            # fin if


opc=0
max=3

while(opc!=max):
    print("------- E S T R E N O S  --------")
    print("- 1. T E R R O R               --")
    print("- 2. A C C I O N               --")
    print("- 3. R O M A N T I C A S       --")
    print("- 4. S A L I R                 --")
    print("---------------------------------")
    opc=libreria.pedir_rango("ingrese opcion: ",1,3)
    if(opc==1):
        terrorP()
    if(opc==2):
        accionP()
    if(opc==3):
        romanticasP()
    # fin if
# fin menu
print("--- ESTRENOS INOLVIDABLES ")