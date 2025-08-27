vendas = [53, 100, 50, 130, 80, 120, 200] #lista de itens separados por virgula
#         0   1    2   3    4   5    6
print(vendas[0]) #pega o item na posição 0, ou seja, na primeira
print(vendas[-1]) #[-1] pega o item na ultima posição
print(vendas[-2])#[-2] pega o item na penuultima posição

total_vendas = sum(vendas) #soma total dos valores
quantidade = len(vendas) #quantidade de valores na lista
v_maximo = max(vendas)
v_minimo = min(vendas)

print(f'o total as vendas foi de {total_vendas}')
print(f'o numero de vendas foi {quantidade}')
print(f'o valor mais alto de venda foi {v_maximo}')
print(f'o valor mais baixo de venda foi {v_minimo}')

posicao = vendas.index(130) #da a posição de um valor dentro da lista
print(posicao)

print(vendas[:3])
#----------------------------------------------------------------------------
produtos = ['iphone', 'ipad', 'airpod']
print('iphone' in produtos) #verifica se aquele valor esta contido na lista, se esta nela
produto_usuario = input('digite seu produto aqui: ')
print(produto_usuario in produtos)

precos = [4000, 8000, 10000]
print(precos) #lista inicial
precos[0] = precos[0] * 1.1 #modifica o valor na posição de [X], que no caso é a 0
print(precos)
precos[0] = int(float(input('novo primeiro valor: '))) #permite q o usuario modifique o valor
print(precos)

#append adiciona um novo item no final da lista
produtos.append('macbook')
precos.append(15000)
print(produtos)
print(precos)

#remover itens da lista
produtos.remove('macbook') #remove pelo valor
precos.pop(-1) #remove pelo indice
print(produtos)
print(precos)

#inserir um valor
produtos.insert(1, 'airpod') #insere o valor na posição indicada
print(produtos)

#contar valores
print(produtos.count("airpod")) #conta qnts vezes o valor aparece na lista

#ordenar
precos.sort() #sort crescente por padrão
print(precos)

precos.sort(reverse=True) #reverse faz virar decrescente
print(precos)
