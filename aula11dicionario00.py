pessoa ={"nome":"Ana","Idade":"30","cidade":"São Paulo"}
pessoa["email"]="ana@email.com"
#print(f"Dados da pessoa:{pessoa}")
pessoa["Idade"]=31
del pessoa["cidade"]
pessoa["endereço"]="Rua tadada"
#print(pessoa)



d1={"a":1,"b":2}
d2={"b":3,"c":4}
#print(d1)
#print(f"{d2}")
#d1.update(d2)
#print(d1)
#d3={**d1,**d2}
#print(d1)

frase="O rato roeu a roupa do rei de roma"
palavras =frase.split()
contagem ={}
for palavra in palavras :
    contagem[palavra] = contagem.get(palavra,0)+1
    print(contagem)