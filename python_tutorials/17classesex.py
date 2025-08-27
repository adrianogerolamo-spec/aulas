# criar classe pra clientes da Netflix
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("plano invalido")
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("plano invalido")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"ver filme {filme}")
        elif self.plano == "premium":
            print(f"ver filme {filme}")
        elif self.plano == "basic" and plano_filme == "premium":
            print("Faça upgrade para premium")
        else:
            print("plano invalido")

cliente = Cliente("Lira", "lira@gmail.com", "basic")
print(cliente.nome, cliente.plano)

cliente.ver_filme("Harry Potter", "premium")

#no botao de upgrade
cliente.mudar_plano("premium")
print(cliente.nome, cliente.plano)

cliente.ver_filme("Harry Potter", "premium")