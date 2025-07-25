'''um set é uma coleção que não possui objetos repetidos, usamos set para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável'''

#declarando 

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"} | não garante a ordem 

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

#acessando dados

numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])

#iterar conjuntos

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
    
'''Métodos'''
    
#union

conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b)
print(resultado)

