#count = conta quantas vezes um elemento tá na lista

cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1

#extend = junta lista e não elimina valores replicados

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

#index = qual a primeira ocorrencia de um objeto

linguagens = ["python", "java", "c", "java", "csharp"]

print(linguagens.index("java"))  # 1
print(linguagens.index("python"))  # 0

#pop = remove o ultimo elemento da pilha (a nao ser que passe índice)

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python