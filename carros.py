class Carro:
    #Método construtor 
    def __init__(self ,marca ,modelo, ano ):
        self.marca = marca #Atributo
        self.modelo = modelo #Atributo
        self.ano = ano #atributo
        self.ligado = False #Atributo co valor padrão 
    


    def exibir_info(self):
        if self.ligado == True :
            status = "ligado"
        else :
            status = "Desligado"    
        
        print(f"{self.marca}{self.modelo}{self.ano}{status}")
    
    def ligar (self):
        self.ligado= True
        print(f"O carro está ligado .")
    
    def desligar(self):
        self.desligado= False
        print(f"O carro está desligado .")

if __name__=="__main__":
    #Criando um objeto da classe carro
    print(f"Criando um objeto da classe carro ")
    meu_carro = Carro("Palio "," Fiat ", 2008) 
    meu_carro.exibir_info()
    meu_carro.ligar()
