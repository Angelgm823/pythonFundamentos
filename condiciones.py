# Ejemplo Ciclo While
# n = 5
# while n > 0:
#     n -= 1
#     print(n)
#     if n == 2:
#         break
#     else:
#         print('Fin del programa') 



# edad = int(input('¿Cúal es tu edad?  '))
# if edad < 18 :
#     print('Eres menor de edad')
# else:
#     print('Ya eres mayor de edad')


# nota = float(input('Introdusca el resultado:  '))
# if nota >= 7:
#     print('Aprobado')
# else:
#     print('Reprobado')

# nombre = 'Angel'
# if nombre == 'Angel':
#     print('Hola angel')
# elif nombre == 'Luis':
#     print('Hola Luis')
# elif nombre == 'Juan':
#     print('Hola Juan')
# elif nombre == 'Antonio':
#     print('Hola Antonio')
# else:
#     print('No se quien seas xd')


# contador = 3
# while contador !=0:
#     contador = contador -1
#     print('el contenido es el siguente: ', contador)

# intentos = 3
#     while intentos > 0:
#         if input("Escriba la contraseña: ") == "Python":
#             print("Correcto")
#             break
#         intentos = intentos -1
#         print("Incorrecto")
#     else:
#         print("mala suerte adios")



# miLista = ['Alejandro', 'Ramon', 'Luis']
# for elemento in miLista:
#     print(elemento)

# for iterador in ['Angel', 'Raul', 'Pedro']:
#     print(iterador)


# a = ['foo', 'bar', 'baz']
# itr = iter(a)
# next(itr)
# next(itr)
# next(itr)


lista = ['vamos', 'a', 'acceder', 'a', 'esta' ,'lista', 'por', 'indice']

for indice in range(len(lista)):
    print('indice: ', indice, 'Elemento: ', lista[indice])