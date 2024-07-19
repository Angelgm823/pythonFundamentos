lista = ["cadena1","cadena2","cadena3"]
print(lista)

print(lista[2])


lista1 = [1,2,3,4]
lista2 = [5,9,8,7]
lista3 = lista1 + lista2 + ['Nuevo Elemento']
print(lista3)

# Funciones de listas

lista = list(("caddena1", "cadena2", "cadena3"))
print(lista)


#funcion append

lista = [1,2,3,4]
lista.append(99)
print(lista)

lista = [1,2,3,4]
lista.append('Nuevo elemento agregado')
print(lista)

lista = [1,2,3,4]
lista.append([89, "listado nuevo", True])
print(lista)

#funcion pop

lista = [1,2,3,4,5,6]
print(lista.pop())
print(lista)
print(lista.pop())
print(lista)
print(lista.pop())
print(lista)
print(lista.pop())
print(lista)
print(lista.pop())
print(lista)

#funcion clear

lista = [1,2,3,4,5,6]
print(lista.clear())
print(lista)

#funcion extend

lista = [1,2,3,4,5,6]
lista2 =  [7,8,9,10]
lista.extend(lista2)
print(lista)

#funcion len

lista =  [1,2,3,4,5,6,7]
print(len(lista))

#funcion count

lista =  [1,2,3,4,5,6,7]
print(lista.count(1))

#funcion index

lista =  [1,2,3,4,5,6,7]
print(lista.index(5))

#funcion insert

lista = [4,8,9]
lista.insert(2, 88)
print(lista)

#funcion remove

lista =  [1,2,3,4,5,6,7]
lista.remove(4)
print(lista)

#funcion reverse
lista =  [1,2,3,4,5,6,7]
lista.reverse()
print(lista)

#funcion sort
lista =  [1,2,3,4,5,6,7]
lista.sort(reverse=False)
print(lista)