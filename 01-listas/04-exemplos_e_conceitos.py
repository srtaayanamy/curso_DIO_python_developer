'''Métodos:'''

#Append = adiciona, armazena

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)  # [1, "Python", [40, 30, 20]]

#clear = limpa a lista

lista2 = [1, "Python", [40, 30, 20]]

print(lista2)  # [1, "Python", [40, 30, 20]]

lista2.clear()

print(lista2)  # []

#copy = repete a lista, cria uma cópia

lista = [1, "Python", [40, 30, 20]]

lista2 = lista.copy()

print(lista2)  # [1, "Python", [40, 30, 20]]

