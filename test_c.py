# assert de las funcion
import libreria

# assert de la funcion ---> validar talla
assert (libreria.validar_talla("hola")==False)
assert (libreria.validar_talla(45)==True)
assert (libreria.validar_talla(10)==True)
print("validar talla ==> OK... ")

# assert de la funcion ---> validar talla
# solo vereficamos si es una cadena
assert (libreria.validar_tamano("hola")==True)
assert (libreria.validar_tamano(12)==False)
assert (libreria.validar_tamano("grande")==True)
assert (libreria.validar_tamano("pequeño")==True)
print("validar tamaño ==> CAÑON... ")

# assert de la funcion ---> validar color
# vereficamos si una cadena
assert (libreria.validar_tamano("pequeño")==True)
assert (libreria.validar_tamano("pequeño")==True)
assert (libreria.validar_tamano("pequeño")==True)
print("validar color ==> CAÑON... ")

# assert de la funcion ---> validar marca de una zapatilla
assert (libreria.validar_entero("2")==False)
assert (libreria.validar_entero("nike")==False)
assert (libreria.validar_entero("nike")==False)
assert (libreria.validar_entero(23)==True)
print("validar entero ==> CAÑON... ")

# assert de la funcion ---> validar marca de una zapatilla
assert (libreria.validar_marca("nike")==True)
assert (libreria.validar_marca("ni")==False)
assert (libreria.validar_marca(3)==False)
print("validar marca ==> OK... ")

# assert de la funcion ---> validar rango
assert (libreria.validar_rango(12,5,20)==True)
assert (libreria.validar_rango(20,5,2)==False)
assert (libreria.validar_rango("hola",5,20)==False)
print("validar rango ==> OK... ")

# assert de la funcion ---> validar mes
assert (libreria.validar_mes(2)==False)
assert (libreria.validar_mes("hola")==False)
assert (libreria.validar_mes("enero")==True)

print("validar mes ==> OK... ")

# assert de la funcion ---> validar año
assert (libreria.validar_ano("hola")==False)
assert (libreria.validar_ano("546")==False)
print("validar año ==> OK... ")

# assert de la funcion ---> validar telefono
assert (libreria.validar_telefono("hola")==False)
assert (libreria.validar_telefono("123456789")==False)
assert (libreria.validar_telefono(925674)==False)
assert (libreria.validar_telefono(925780779)==True)
print("validar telefono ==> CAÑON... ")

# assert de la funcion ---> validar dni
assert (libreria.validar_dni("hola")==False)
assert (libreria.validar_dni("12")==False)
assert (libreria.validar_dni(12)==False)
assert (libreria.validar_dni("74286646")==False)
assert (libreria.validar_dni(74286646)==True)
print("validar DNI ==> CAÑON... ")


