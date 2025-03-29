matriz =[
    [12,2,3,6],
    [4,15,6,9],
    [7,8,19,10],
     [7,8,19,10]


]

num=int(input("Digite o multiplicador : "))
linha=int(input("Digite a linha escolhida(0-4) :"))
for j in range(4):
    matriz[linha][j]*=num 
for linha in matriz:
    print(linha)
    