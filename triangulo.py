("---TRIANGULO---")
num=float(input("Digite o primeiro lado : "))
num2=float(input("Digite o segundo lado : "))
num3=float(input("Digite o terceiro lado : "))

if (num==num2==num3):
    print("É um triangulo equilátero")
elif(num==num2) or (num2==num3) or (num==num3):
    print("É um triângulo isóceles")
else: print("É um triângulo escaleno ")