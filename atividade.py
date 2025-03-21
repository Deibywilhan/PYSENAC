import sys 

def saudacao():
    print("Olá, seja bem-vindo(a) ao curso de Phyton!")
  
def soma (a,b):
    return a+b 
   
def testar_soma ():
    resultado=soma(5,7)
    print("A soma é :",resultado)


def fatorial(n):
    if n<0:
        return" Número inválido para fatorial. "
    elif n==0:
        return 1
    else:
        for i in range(1,n+1):
            resultado *= i
        return resultado

def testar_fatorial():
    print("Fatorial de 5: ", fatorial(5))

if __name__=="__main__":
    testar_fatorial()

