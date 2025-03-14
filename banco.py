print("===BANCO===")
nome=(input("Digite seu nome : "))
idade=(int(input("Para prosseguir com sua análise digite sua idade :")))
nom=(input("Voce possui alguma restrição no seu nome? S/N ")).lower
salario=(float(input("Digite o seu sálario :")))

#if (idade<=20):
#    print("Você é muito jovem para acessar esse serviço: ")
#elif(nom=="s"):
    #print("Devido a restrição no seu nome ,você não tem acesso ao serviço :")

#elif(salario<=2000):
   # print("Você não possui renda o suficiente para acessar o serviço !")

#else:("PARABÊNS,você pode contratar esse serviço !")#

if (idade<=20) or (salario<=2000) or (nom=="s"):
    print("Você não pode acessar esse tipo de serviço : ")
else:print ("Você pode prosseguir com o empréstimo : ")