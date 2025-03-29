matriz =[
    [12,2,3,6],
    [4,15,6,9],
    [7,8,19,10],
    [7,8,19,10]


]
vet_pares =[]
vet_impares =[]
pares = 0
impares = 0 
for i in range (4):
    for j in range (4):
        if matriz[i][j]%2 == 1 :
            impares +=1
            vet_impares.append(matriz[i][j])
        else:
            pares =pares +1
            vet_pares.append(matriz[i][j])    
print(f"Quantidade de numeros pares :{impares}")
print(f"Quantidade de numeros pares :{pares}")

print(f"Os números impares são : {vet_impares}")
print(f"Os números impares são : {vet_pares}")
