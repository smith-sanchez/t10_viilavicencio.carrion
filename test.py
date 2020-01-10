import libreria

assert (libreria.validar_entero_positivo(10) == True)
assert (libreria.validar_entero_positivo(100) == True)
assert (libreria.validar_entero_positivo("100") == False)
assert (libreria.validar_entero_positivo(-10) == False)
assert (libreria.validar_entero_positivo("hola") == False)
assert (libreria.validar_entero_positivo(True) == False)
print("Validar_entero_positivo -> OK")


assert (libreria.validar_rango(15,16,20) == False)
assert (libreria.validar_rango("hola",15,24) == False)
assert (libreria.validar_rango("hola",12,"aprobe") == False)
assert (libreria.validar_rango(2,1,152) == True)
assert (libreria.validar_rango(58,45,65) == True)
assert (libreria.validar_rango(15,15,15) == True)
print("validar_rango -> OK")


assert (libreria.validar_dia("Domingo") == True)
assert (libreria.validar_dia("hola") == False)
assert (libreria.validar_dia(12) == False)
assert (libreria.validar_dia("Miercoles") == True)
assert (libreria.validar_dia("Viernes") == True)
assert (libreria.validar_dia(True) == False)
print("validar_dia -> OK")


assert (libreria.validar_nombre("Programacion") == True)
assert (libreria.validar_nombre("hl") == False)
assert (libreria.validar_nombre(12) == False)
assert (libreria.validar_nombre("smith") == True)
assert (libreria.validar_nombre("Viernes") == True)
assert (libreria.validar_nombre(True) == False)
print("validar_nombre -> OK")


assert (libreria.validar_carrera("Fisica") == True)
assert (libreria.validar_carrera("mundo") == False)
assert (libreria.validar_carrera(152) == False)
assert (libreria.validar_carrera("Matematica") == True)
assert (libreria.validar_carrera("Ingenieria Electronica") == True)
assert (libreria.validar_carrera(False) == False)
print("validar_carrera -> OK")


assert (libreria.validar_celular("LG") == True)
assert (libreria.validar_celular("UNI") == False)
assert (libreria.validar_celular(-7892) == False)
assert (libreria.validar_celular("IPHONE") == True)
assert (libreria.validar_celular("SAMSUNG") == True)
assert (libreria.validar_celular(False) == False)
print("validar_celular -> OK")


assert (libreria.validar_planeta("Mercurio") == True)
assert (libreria.validar_planeta("mundo") == False)
assert (libreria.validar_planeta(983) == False)
assert (libreria.validar_planeta("Tierra") == True)
assert (libreria.validar_planeta("Marte") == True)
assert (libreria.validar_planeta(True) == False)
print("validar_planeta -> OK")


assert (libreria.validar_satelite("Luna") == True)
assert (libreria.validar_satelite("mundo") == False)
assert (libreria.validar_satelite(-45) == False)
assert (libreria.validar_satelite("Matematica") == False)
assert (libreria.validar_satelite("Venus") == False)
assert (libreria.validar_satelite(False) == False)
print("validar_satelite -> OK")


assert (libreria.validar_super("STD") == True)
assert (libreria.validar_super("0.50") == True)
assert (libreria.validar_super(-45) == False)
assert (libreria.validar_super("1.00") == True)
assert (libreria.validar_super("Venus") == False)
assert (libreria.validar_super(False) == False)
print("validar_super -> OK")


assert (libreria.validar_viaje("Aire") == True)
assert (libreria.validar_viaje("Tierra") == True)
assert (libreria.validar_viaje(-4548) == False)
assert (libreria.validar_viaje("Agua") == True)
assert (libreria.validar_viaje("peru") == False)
assert (libreria.validar_viaje(False) == False)
print("validar_viaje -> OK")


assert (libreria.validar_habitacion("Simple") == True)
assert (libreria.validar_habitacion("Matrimonial") == True)
assert (libreria.validar_habitacion(48) == False)
assert (libreria.validar_habitacion("Doble") == True)
assert (libreria.validar_habitacion("profe") == False)
assert (libreria.validar_habitacion(True) == False)
print("validar_habitacion -> OK")
