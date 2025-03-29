matriz =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    print(linha)