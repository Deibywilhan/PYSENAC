print("===EXERCÍCIO 2===")

idade_str=input("Digite sua idade:  ")
idade=int(idade_str)
if idade>=18: 
    print("Seu voto é obrigatório ! ")
elif idade>=16:
    print("Você  pode votar !")

else: 
    print("Você é menor de idade !")