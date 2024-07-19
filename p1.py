# print('"estoy" \n ""aprendiendo"" \n """python"""')

# #suma
# suma = 4 + 6
# print(suma)

# #resta
# resta = 26 + 12
# print(resta)

# #multiplicacion
# mult = 5 *9
# print(mult)

# #division
# cociente = 5 / 2
# print(cociente)

# #esxponencial
# exp =4 ** 4
# print(exp)

# #floor divisio
# div = 16//2
# print(div)

# #operador modulo residuo de una division
# mod = 7 % 3
# print(mod) 

# x = 10
# y = 5
# z = -3
# rest = (x-2) + (y * z)
# print(rest)

# res = 5 
# res = res + 10
# print(res)

# res = 5 
# res += 10
# print(res)


# res = 5 
# res -= 10 #resta 5 a la variable res
# print(res)

# #precision de números flotantes
# print(1.23 + 2.80)

# print(1.26 + 1.32)

# print(.1 + .1 + .1)

# x1 = 0.1+0.1+0.1
# x2 = 0.3
# print(x1 == x2)

# import math
# format(math.pi, '.4g') #da 12 digitos
# format(math.pi, '.4f')#12 digitos despues del punto

# num1 = 2
# num2 = 15

# esPar = num1 %2 == 0
# esPar

# esPar = num2 %2 == 0
# esPar

# import math
# num1 = 100
# num2 = 95
# print(math.isclose(num1, num2, rel_tol=0.04))
# print(math.isclose(num1, num2, rel_tol=0.5))

# a = True, 5
# b = True, 10
# c = False, 5
# d = False, 20
# print(a and c and b and d)
# print(a != c)


# numeroOperaciones = 7
# altura = 1.75
# nombre = 'angel'
# numComplex = 1.3 - 7j

# mensaje = nombre + "mide " + str(altura)
# print(mensaje)


# x = 3
# print("* Tipo de x: ")
# print(type(x)) #imprime el tipo (o clase ) de x
# print("* Valor de x: ")
# print(x)


# user = 'Angel'
# lineas = 55
# print("Hola, " + user + "ya escribiste, " + str(lineas) + " de codigo")



#De enteros a texto
# j = 6
# k = 4.456734
# print("de entero a texto ")
# print("j = " + str(j))
# print("k = " + str(k))

# usando %s
# nombre, edad = 'Alan', 22
# res1 = "Hola %s, tu edad es: %s" %(nombre, edad)
# print(res1)

# #usando str format
# mensaje =  "Hola {0}, tu edad es: {1}".format(nombre, edad)
# print(mensaje)

# #usando F-STRING
# mensaje2 = f"Hola {nombre}, tu edad es: {edad}"
# print(mensaje2)


produccion_total = 45400
capacidad = 260
piezas_defectuosas = 3809
tiempo_disponible = 300 - 16
tiempo_muerto = 34+4
tiempo_operativo = 284 - 38

diponibilidad = tiempo_operativo / tiempo_disponible

eficiencia = produccion_total / (tiempo_operativo * capacidad)
print(eficiencia)
print(round(eficiencia, 2))

calidad = (produccion_total - piezas_defectuosas) / produccion_total
print(round(calidad, 2))

eficiencia_general = diponibilidad * eficiencia * calidad
print(round(eficiencia_general, 2))



# Tabla de opratadores como funciona

# 1. ()
# 2. **
# 3. %, /, //, y *
# 4. + y -