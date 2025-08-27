#scripts sao o bastante para coisas simples, como automacao de processos simples
#para tarefas mais complexas, como sites e apps, e necessario saber orientacao a objeto
#ao contrario da programacao normal, que da comandos linha a linha pro computador
#voce cria um objeto, define atributos e metodos (funcoes) para ele, e utiliza elas pra interagir 
#com ele no codigo, por exemplo, os textos são objetos (str), que tem funcoes (print) proprias

class ControleRemoto:#geralmente se incia com maiusculas
    def __init__(self, cor, altura, profundidade, largura): #self faz referencia a ele mesmo, o objeto em si
        self.cor = cor #cria o atributo cor pra classe ControleRemoto, que tem seu valor igual a variavel cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao): #cria uma funcao pro objeto
        if botao == "+":
            print("Aumentar canal")
        elif botao == "-":
            print("Diminuir canal")

"""     metodos do controle: #"verbos"
        -passar canal
        -aumentar volume
        -desligar
    pass
 """

controle_remoto = ControleRemoto("preto", "10cm", "2cm", "2cm") #duas instancias da classe ControleRemoto
print(controle_remoto.cor)
botao = input("+/- : ")
controle_remoto.passar_canal(botao) #() no final mostra que e uma funcao

controle_remoto2 = ControleRemoto("cinza", "10cm", "2cm", "2cm")
print(controle_remoto2.cor)
botao2 = input("+/- : ")
controle_remoto2.passar_canal(botao2)