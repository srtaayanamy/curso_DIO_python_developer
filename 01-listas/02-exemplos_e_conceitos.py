#fatiamento

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"] (é 2-1, ou seja, o "y")
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"] com step
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

print(20*"--") 

#iteração de listas

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)
    
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

