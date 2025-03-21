import sys
def principal(parametros):
    for dado in parametros:
        print(dado)

def soma(numeros):
    somatorio=0
    for valor in numeros :
        somatorio=somatorio + valor 
       

if __name__=="__main__":
    resultado=soma(sys.argv[1:])
    print(f"O valor da soma dos hnúmeros é {resultado}")