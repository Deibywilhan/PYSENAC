print(" = = = CADASTRO DE USUÁRIO = = = ")
nome=input("Digite seu nome : ")
senha=input("Cadastre sua senha")
if(len (nome) <3) :
    print("Seu nome deve ter mais de 3 letras ! ")
elif (len (senha) <6):
    print(" A senha deve ter pelo menos 6 digitos ! ")

elif(senha==123456) or (senha=="senha"):
    print("Senha fraca ,por favor cadastre outra senha.")

else: print("Cadastro ativado com sucesso")