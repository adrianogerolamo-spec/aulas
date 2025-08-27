faturamento = 1000
custo = 800
lucro = faturamento - custo

#= recebe
#== comparação

#if condicao (comparacao):
    #tudo que você quer que aconteça caso a condição seja VERDADEIRA

""" if lucro > 0:
    print(f'lucro:{lucro}')  #indentação, ajuda organizar o código, no py serve pra dizer oq ta no if
else:
    print('ha prejuizo') #o que voce quer que ocorra caso o if seja falso

produtos = ['iphone', 'ipad', 'airpod']
novo_produto = input('digite o produto aqui:')

novo_produto = novo_produto.lower() #IMPORTANTE TRATAR A INFO DADA PELO USUARIO

if novo_produto in produtos:
    print('produto ja cadastrado')
else:
    print('produto cadastrado com sucesso')
    produtos.append(novo_produto)

print(produtos) """ # """ comenta o bloco todo """

#vendas acima de 15k -> bonus de 500

vendas = input('digite o seu total de vendas:')
vendas = vendas.replace('R$','')
vendas = int(float(vendas))

vendas_empresa = input('digite o total da:')
vendas_empresa = vendas_empresa.replace('R$','')
vendas_empresa = int(float(vendas_empresa))

""" if vendas > 15000:
    print('bonus de 500 recebido')
    bonus = 500
else:
    print('trbalhe mais escravo !!!')
    bonus = 0
print(f'bonus total: {bonus}') """

#vendas_empresa = >50k
#vendas > 15k:bonus 500
#vendas > 10k:bonus 150
#vendas > 5k:bonus 50

if not vendas_empresa > 50000: #se X não for verdadeiro
    bonus = 'nada seu pobre'
else:
    if vendas > 15000: #elif=else+if
        bonus = 500
    elif vendas > 10000: #and= mais uma condição
        bonus = 150
    elif vendas > 5000: #or= ou
        bonus = 50
    else:
        bonus = 'nada seu pobre'

""" if vendas > 5000:
    if vendas > 10000:
        if vendas > 15000:
            bonus = 500
        else:
            bonus = 150
    else:
        bonus = 50
else:
    bonus = 0 """

print(f'bonus: {bonus}')