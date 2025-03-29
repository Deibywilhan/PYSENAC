
matriz =[
    [1,2,3,6],
    [4,5,6,9],
    [7,8,9,10]
]


soma=0
for i in range(4):
    for j in range(i+1,4):
        soma += matriz[i][j]
print(f'Soma dos elementos acima da diagonall principal :{soma}')
    
