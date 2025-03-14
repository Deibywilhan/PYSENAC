idade=int(input("Digite a sua idade : "))
tem_carteira=input("Você tem habilitação? s/n")
tem_carteira=tem_carteira.lower()
if (idade >=18) and (tem_carteira == "s"):
    print("Você pode dirigir !")
else: print("Você não pode dirigir !")