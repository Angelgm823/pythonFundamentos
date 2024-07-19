persona = {'nombre': 'Angel Gomez', 'edad': 24}
print(persona)
print(persona['nombre'])

capitales = {"Jalisco": "Guadalajara", 'Morelos': 'Cuernavaca'}
print(capitales.get("Jalisco"))
print(capitales.get("Morelos"))

persona['telefono'] = '5533107241'
persona['coloresFavoritos'] = ['negro', 'verde', 'azul']
print(persona)

persona['edad'] = 35
print(persona['edad'])


persona = {'nombre': 'Angel','edad':25}
edad = persona.pop('edad')
print(persona)
persona.clear()
print(persona)

#metodos integrados en los diccionarios
print("Items", list(capitales.items()))
print("Keys", list(capitales.keys()))
print("Keys", list(capitales.values()))


capitales = {"Jalisco": "Guadalajara", 'Morelos': 'Cuernavaca'}
for key in capitales.keys():
    print(f'La capital de {key} es {capitales.get(key)}')