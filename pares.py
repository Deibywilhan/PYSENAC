matriz =[
    [12,2,3,6],
    [4,15,6,9],
    [7,8,19,10],
    [7,8,19,10]


]

pares = 0 
for i in range (4):
    for j in range (4):
        if matriz[i][j]%2 == 1 :
            pares +=1
print(f"Quantidade de numeros pares :{pares}")