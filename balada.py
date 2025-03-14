print("Controle de Entrada ")
listaban=("[junior],[Maria],[Jessica]").lower
nome=input("Digite Seu nome ! ")
idade=int(input("Digite Sua idade :"))
pais=input("Está acompanhado dos pais? S/N ").lower

if (nome==listaban) or (idade<=17) or (pais=="n"):
    print("Você não pode entrar !")
else:print("Você pode entrar!")


