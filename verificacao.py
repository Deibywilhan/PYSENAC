print("===VERIFICAÇÃO===")
idade=(input("Qual a sua idade ?"))
senha=(input("Digite a senha : "))
idade1=int(idade)
senha1=int(senha)
if (idade1>=18) and ( senha1==1234 ):
    print("Você está conectado! ")
elif (idade1<=17):
    print("Você é menor de idade ,e não tem permissão para acesso.")
else: 
    print("Senha incorreta ! ") 