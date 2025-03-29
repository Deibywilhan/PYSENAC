
matriz =[
    [12,2,3,6],
    [4,15,6,9],
    [7,8,19,10],
     [7,8,19,10]


]
for i in range(4):
    maior = matriz[i][0]
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
    print(f"Maior valor da linha {i}: {maior}")