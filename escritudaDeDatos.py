# import random
# f = open('numeros.txt', 'w')
# for count in range (100):
#     num = random.randint(1, 1000)
#     f.write(str(num) + '\n')
#     f.close()
    
f = open('numeros.txt', 'r')
sumatoria = 0 
for linea in f:
    linea = linea.strip()
    numero = int(linea)
    sumatoria += numero
print(sumatoria)