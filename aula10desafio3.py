matriz =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


for linha in matriz:
    print(f"|",end=" ")
    for elemento in linha:
       print(elemento,end=' | ')
    print()
matriz = [[int(input(f"Digite o valor para [{i}][{j}]: ")) for j in range(4)] for i in range(4)]