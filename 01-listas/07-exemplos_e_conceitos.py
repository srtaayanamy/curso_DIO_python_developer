'''Métodos:'''

#len = tira o tamanho das coisas, nesse caso da lista

linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens))  # 5

#sorted = ordena interaveis, a diferença é que sorted é uma função

linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]