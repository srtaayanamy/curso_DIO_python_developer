#declarando

frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python") #iteravel
print(letras) # = [p,y,t,h,o,n]

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",) #a virgula ao final é boa prática. mas funciona sem em casos de mais de um elemento {python entende como precedencia de operadores}
print(pais)

#acesso direto

frutas = ("maçã", "laranja", "uva", "pera",)

print(frutas[0])  # maçã
print(frutas[2])  # uva

#índices negativos

frutas = (
    "maçã",
    "laranja",
    "uva",
    "pera",
)

print(frutas[-1])  # pera
print(frutas[-3])  # laranja

#matriz

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])  # (1, "a", 2)
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

#fatiamento

tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])  # ("t", "h", "o", "n")
print(tupla[:2])  # ("p", "y")
print(tupla[1:3])  # ("y", "t")
print(tupla[0:3:2])  # ("p", "t")
print(tupla[::])  # ("p", "y", "t", "h", "o", "n")
print(tupla[::-1])  # ("n", "o", "h", "t", "y", "p")

