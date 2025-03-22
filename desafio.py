import sys


def calculadora(n1,n2,op):
    if op =="+":
       resultado=n1+n2 
       
    elif op== "-":
        resultado=n1-n2
    elif op== "*":
        resultado=n1*n2
    elif op== "/":
        resultado=n1/n2

    


if __name__=="__main__":
    argumentos=sys.argv[1:]
    numero1=float(argumentos[0])
    numero2=float(argumentos[1])
    operacao=argumentos[2]
    
    print(numero1,numero2, operacao) 