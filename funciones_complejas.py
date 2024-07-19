print("Hola de nuevo")

def sumarNumeros(*args):
        resultado = 0
        for numero in args:
                resultado = resultado + numero
                return resultado
print(sumarNumeros(50, 50, 50))
    
def factorial(n):
        if(n == 0):
                return 1;
        else:
                return n * factorial(n - 1)
        factorial(0)
        factorial(10)
        print(factorial)
        
        
miLista = [1,2,3,4,5]
print(miLista)
print(miLista[0])
print(miLista[-1])
#modificacion de lista
miLista[0] = 10
miLista.append(6)
print(miLista)