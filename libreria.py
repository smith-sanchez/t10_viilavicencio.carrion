# libreria
# funcion validar talla
def validar_talla(num):
    # tiene que ser un entero
    if(isinstance(num,int)):
        return True
    # fin if
    else:
        return False

# funcion validar rango
def validar_rango(num,ri,rf):
    if(validar_talla(num)==True):
        if(num>=ri and num<=rf):
            return True
    # fin_if
        else:
            return False
    else:
        return False
# funcion pedir rango
def pedir_rango(msg,ri,rf):
    n=-1
    while(validar_rango(n,ri,rf)==False):
        n=input(msg)
        if(n.isdigit()==True):
            n=int(n)
        # fin_ if
    #fin_while
    return n
# funcion pedir edad
def pedir_edad(msg,ri,rf):
    n=-1
    while(validar_rango(n,ri,rf)==False):
        n=input(msg)
        if(n.isdigit()==True):
            n=int(n)
    return n
# funcion pedir nombre
def pedir_nombre(msg):
    m=""
    while(validar_color(m)==False):
        m=input(msg)
    return m
# funcion validar color
def validar_color(color):
    # es una cadena
    if(isinstance(color,str)):
        # longitud >3
        if(len(color)>=3):
            return True
        else:
            return False
    else:
        return False
    # fin_if
# funcion pedir solo dos colores
# solo puede elejir una--> blanco / negro
def pedir_color(msg):
    m=""
    while(validar_color(m)==False):
        m=input(msg)
        while (m!="blanco" and m!="negro"):
            m = input(msg)
            # fin_while
    return m
# fumcion pedir colores
# solo se puede ingresar colores seleccionadas segun el programador
def pedir_colores(msg):
    m=""
    while(validar_color(m)==False):
        m=input(msg)
        while (m!="blanco" and m!="negro" and m!="amarillo" and m!="rojo" and m!="rosado"
               and m != "dorado" and m!="verde" and m!="celeste" and m!="azul"):
            m = input(msg)
        # fin_while
    return m

# funciom validar marca
def validar_marca(sapatilla):
    # tiene que ser cadena
    if(isinstance(sapatilla,str)):
        # su longitud es mayo que dos
        if(len(sapatilla)>2):
            return True
        else:
            return False
    else:
        return False
    # fin_if
# fin_def

# funcion pedir marca
def pedir_marca(marca):
    m=""
    while(validar_marca(m)==False):
        m=input(marca)
        # fin_while
    return m
# fin_def
# funcion pedir postre
# condicion ==> ( gelatina / mazamorra )
def pedir_marcas(marca):
    m=""
    while(validar_marca(m)==False):
        while(m!="gelatina" and m!="mazamorra"):
            m=input(marca)
        # fin_while
    return m
# fin_def
# funcion pedir elejir menu con la condicion
# si solo es ( desayuno / almuerzo / cena )
def pedir_marcas_condic(marca):
    m=""
    while(validar_marca(m)==False):
        while(m!="desayuno" and m!="almuerzo" and m!="cena"):
            m=input(marca)
        # fin_while
    return m
# fin_def
# funcion validar entero
def validar_entero(numero):
    # en entero-->int
    if(isinstance(numero,int)):
        # entero positivo
        if(numero>=0):
            return True
        else:
            return False
    else:
        return False
# funcion pedir entero
def pedir_entero(msg):
    n=-1
    while(validar_entero(n)==False):
        n=input(msg)
        if(n.isdigit()==True):
            n=int(n)
        # fin_if
    # fin:while
    return n
# funcion validar tamaño
def validar_tamano(tamano):
    # tiene queser una cadena
    if(isinstance(tamano,str)):
        # su longitud >3
        if(len(tamano)>3):
            return True
        else:
            return False
    else:
        return False
def pedir_tamano(msg):
    n=""
    while(validar_tamano(n)==False):
        n=input(msg)
        while(n!="grande" and n!="pequeño"):
            n=input(msg)
    return n

# funcion validar mes
def validar_mes(mes):
    # tiene que ser cadena
    if(isinstance(mes,str)):
        # su longitud nmayor que cuatro
        if(len(mes)>4):
            return True
        else:
            return False
    else:
        return False

def pedir_peli(msg):
    n=""
    while(validar_mes(n)==False):
        # solo se podra ingresar una pelicula ==>
        while(n!="star wars" and n!="stand de besos" and n!="naruto" and
              n!="dragon ball" and n!="el barco" and n!="la casa de papel"):
            n=input(msg)
    return n
def pedir_mes(msg):
    n=""
    while(validar_mes(n)==False):
        n=input(msg)
        while(n!="enero" and n!="febrero" and n!="marzo" and n!="abril" and n!="mayo" and n!="junio"
               and n!="julio" and n!="agosto" and n!="septiembre" and n!="octubre" and n!="noviembre"
               and n!="diciembre"):
            n=input(msg)
    return n
# funcion pedir escuela

def pedir_escuela(msg):
    n=""
    while(validar_mes(n)==False):
        n=input(msg)
        while(n!="ing. electronica" and n!="matematica" and n!="ing. informatica" and
              n!="estadistica" and n!="fisica" ):
            n=input(msg)
    return n
def pedir_dia(msg):
    n=""
    while(validar_mes(n)==False):
        n=input(msg)
        # tiene que ingresar un dia : lunes/martes/miercoles/jueves/viernes/sabado/dommingo:
        while(n!="lunes" and n!="martes" and n!="miercoles" and n!="jueves" and n!="viernes" and
               n!="sabado" and n!="domingo"  ):
            n=input(msg)
    return n


def pedir_curso(msg):
    n=""
    while(validar_mes(n)==False):
        n=input(msg)
        while(n!="matematica" and n!="programacion" and n!="analisis"):
            n=input(msg)
    return n

# funcion validar año
def validar_ano(ano):
    # tiene que ser un entero
    if(isinstance(ano,int)):
        # rango entre 1950 y 2020
        if(ano>=1950 and ano <=2020):
            return True
        else:
            return False
    else:
        return False
# funcion pedir año
def pedir_ano(msg):
    n=0
    while(validar_ano(n)==False):
        n=input(msg)
        if(n.isdigit()==True):
            n=int(n)
    return n

# funcion validar telefono
def validar_telefono(telefono):
    # sus digitos tienen que ser enteros
    if(isinstance(telefono,int)):
        # el telefono tiene que tener la forma(925780779)
        if(telefono>=900000000 and telefono<=999999999):
            return True
        else:
            return False
    else:
        return False
# funcion pedir telefono
def pedir_telefono(msg):
    n=-1
    while(validar_telefono(n)==False):
        n=input(msg)
        if(n.isdigit()==True):
            n=int(n)
    return n
# funcion validar dni
def validar_dni(dni):
    if(isinstance(dni,int)):
        # sus digitos  son enteros
        # el dni tiene que tener la forma( 74286646 )
        if(dni>=10000000 and dni<=99999999):
            return True
        else:
            return False
    else:
        return False

# funcion pedir dni
def pedir_dni(msg):
    n=-1
    while(validar_dni(n)==False):
        n=input(msg)
        if(n.isdigit()==True):
            n=int(n)
    return n

def guardar_d(nombre_archivo,contenido,modo):
    archivo=open(nombre_archivo,modo)
    archivo.write(contenido)
    archivo.close()
def obtener_datos(nombre_archivos):
    archivo = open(nombre_archivos, "r")
    datos = archivo.read()
    archivo.close()
    return datos
