#def saudacao(nome="Mundo"):
   # print(f"Olá {nome}!")

#saudacao() #Saída 

def listar_nomes(*nomes):
    for nome in nomes:
        print(nome)
listar_nomes("Alice","2","Charlie")