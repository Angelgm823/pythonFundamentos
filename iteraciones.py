estados = {"CDMX", "Guanajuato", "Ciudad Victoria", "Sonora", "Puebla", "Durango"}
for estado in estados:
    print(estado)
    
#union
A = {'rojo', 'verde', 'azul'}
B = {'amarillo', 'rojo', 'naranja'}
print(A.union(B))
print(A|B)

#intersdección
print(A.intersection(B))
print(A&B)

#diferencia
print(A.difference(B))
print(A-B)


diplomado = "Ciencia de Datos"
for index in range(len(diplomado)):
    print(index, diplomado[index])