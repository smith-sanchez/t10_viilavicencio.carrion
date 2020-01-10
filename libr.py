# Devuelve True si numero es un entero positivo
# Parametros:
#    numero (int)
def validar_entero_positivo(numero):
    # 0. cuidado con el bool
    if ( isinstance(numero, bool)):
        return False
    # Si numero es de tipo entero, verificar si es > 0
    # SI numero > 0, retornar True, sino False
    if ( isinstance(numero, int)):
        if ( numero > 0 ):
            return True
        else:
            return False
    else:
        return False
#fin_def

def validar_rango(num,ri,rf):
    # 1. Es un entero positivo
    # 2. Esta dentro del rango
    if ( validar_entero_positivo(num) == True):
        if (num >= ri and num <= rf):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_entero(msg, ri, rf):
    n=input(msg)
    while (validar_rango(n, ri, rf) == False):
        n=input(msg)
        if (n.isdigit() == True):
            n=int(n)
    #fin_while
    return int(n)
#fin_def

def validar_real_positivo(numero):
    if (isinstance(numero,float)):
        if (numero > 0):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_numero(msg, ri, rf):
    n=-1
    while( validar_rango(n, ri, rf) == False):
       n=input(msg)
       if ( n.isdigit() == True):
           n = int(n)
    #fin_while
    return n
#fin_pedir_numero

def validar_cadena(cadena):
    if ( isinstance(cadena, str)):
        return True
    else:
        return False
# fin_def

def validar_nombre(nombre):
    if ( isinstance(nombre, str)):
        if (len(nombre) >= 3):
            return True
        else:
            return False
    else:
        return False

def pedir_nombre(msg):
    nombre=""
    while ( validar_nombre(nombre) == False ):
        nombre=input(msg)
    #fin_while
    return nombre
#fin_pedir_nombre

def guardar_datos(ruta_archivo, contenido, modo):
    archivo=open(ruta_archivo, modo)
    archivo.write(contenido)
    archivo.close()

def obtener_datos(ruta_archivo):
    archivo=open(ruta_archivo)
    contenido = archivo.read()
    archivo.close()
    return contenido

def validar_booleano(booleano):
    if ( isinstance(booleano, bool)):
        return True
    else:
        return False
# fin_def

def validar_dni(dni):
    if (dni.isdigit()==True and len(dni)==8):
        return True
    else:
        return False


def mostrar_ticket(producto1, producto2, producto3, tienda):
    print("######################")
    print("# TIENDA: "+tienda+"#")
    print("######################")
    print("# LISTA DE PRODUCTOS #")
    print("# "+producto1+" #")
    print("# "+producto2+" #")
    print("# "+producto3+" #")
    print("######################")

#fin_Def

# Devuelve true si año es un año valido
# Parametros:
#    año (str)
def validar_año(año):
    # 1. Verificar si año es una cadena
    # 2. Verificar si año tiene 4 caracteres
    # 3. Verificar si año tiene forma de numeros
    # 4. Verificar si el año > 0 y <= 9999
    if ( isinstance(año, str) ):
        if ( len(año) == 4 ):
            if ( año.isdigit() == True ):
                if ( int(año) > 0 and int(año) <= 9999 ):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def validar_mes(mes):
    # 1. Verificar si mes es una cadena
    # 2. Verificar si mes tiene 2 caracteres
    # 3. Verificar si mes tiene forma de numeros
    # 4. Verificar si el mes > 0 y <= 12
    if ( isinstance(mes, str) ):
        if ( len(mes) == 2 ):
            if ( mes.isdigit() == True ):
                if ( int(mes) > 0 and int(mes) <= 12 ):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def validar_dia(dia):
    # 1. Verificar si dia es una cadena
    # 2. Verificar si dia tiene 2 caracteres
    # 3. Verificar si dia tiene forma de numeros
    # 4. Verificar si el dia > 0 y <= 31
    if ( isinstance(dia, str) ):
        if ( len(dia) == 2 ):
            if ( dia.isdigit() == True ):
                if ( int(dia) > 0 and int(dia) <= 31 ):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def validar_fecha(fecha):
    # 1. LA fecha es una cadena
    # 2. La fecha tienen 10 caracteres
    # 3. YYYY-MM-DD (hay 2 caracteres -)
    # 4. YYYY es un año valido
    # 5. MM es un mes valido
    # 6. DD es un dia valido
    if ( isinstance(fecha, str) ):
        if ( len(fecha) == 10 ):
            if( fecha[4] == "-" and fecha[7] == "-" ):
                año=fecha[0:4]
                mes=fecha[5:7]
                dia=fecha[8:]
                if ( validar_año(año) == True and
                     validar_mes(mes) == True and
                     validar_dia(dia) == True):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
#fin_if


#Devuelve True si la nota es vigesima
#Parametro:
#nota (float)   -> 18.5
def validar_nota(nota):
    if ( isinstance(nota, float) or isinstance(nota,int)):
        nota=float(nota)
        if (nota >= 0 and nota <= 20):
            return True
        else:
            return False
    else:
        return False
#fin_def



def mostrar_ticket(producto1, producto2, producto3, tienda):
    print("######################")
    print("# TIENDA: "+tienda+"#")
    print("######################")
    print("# LISTA DE PRODUCTOS #")
    print("# "+producto1+" #")
    print("# "+producto2+" #")
    print("# "+producto3+" #")
    print("######################")

#fin_Def

def mostrar_notas(curso, nota1, nota2, nota3, nota4, nota5, prom):
    print("#####################")
    print("## CURSO: "+curso+"##")
    print("#####################")
    print("# PROMEDIO DE NOTAS #")
    print("# "+nota1+" #")
    print("# "+nota2+" #")
    print("# "+nota3+" #")
    print("# "+nota4+" #")
    print("# "+nota5+" #")
    print("# Prom:"+prom+" #")

