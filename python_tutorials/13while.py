#similar ao for, mas permite que o codigo execute eternamente até receber um comando pra parar,
#o que e util para manter um jogo funcionando ate o usuario sair dele, por exemplo
contador = 0
while contador < 5:
    print('eae')
    contador = contador +1

produtos = ['iphone', 'ipad', 'airpod']

while True: #loop infinito
    novo_produto = input("digite o produto aqui, ou digite 'sair':")
    novo_produto = novo_produto.lower()
    novo_produto = novo_produto.replace("'sair'", 'sair')

    if 'sair' == novo_produto:
        break #interrompe o loop

    if novo_produto in produtos:
        print('produto ja cadastrado')
    else:
        print(f'produto {novo_produto} cadastrado com sucesso')
        produtos.append(novo_produto)

print(produtos)

# fazer o jogo_da_forca_com_while.py nos testes