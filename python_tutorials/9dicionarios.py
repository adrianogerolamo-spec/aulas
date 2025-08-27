""" precos = [1500, 1000, 800, 2000]
produtos = ['celular', 'camera', 'fone de ouvido', 'monitor'] """

dic_precos = {'celular':1500, 'camera':1000, 'fone de ouvido':800, 'monitor':2000}

""" #pegar o valor de um item
preco_celular = dic_precos['celular']
print(preco_celular)

#editar o valor de um item do dicionario
dic_precos['celular'] = 2000
print(dic_precos)

#adicionar um item no dicionario
dic_precos['iphone'] = 3000 #se o item nao existir, ele e adicionado no dicionario
print(dic_precos)

#remover um item
dic_precos.pop('iphone')
print(dic_precos)

#qnt de itens (nao de valores) no dic
print(len(dic_precos))

#procurar um item 
print('televisao' in dic_precos) #procura o item no dic, não o valor

#procurar um valor
print(1000 in dic_precos.values())

#valores e chaves(itens) no dicionario
print(dic_precos.values())
print(dic_precos.keys()) """

#exercicio: refaca o sistema de cadastro (2:44:26)
print(f'produtos disponiveis: {dic_precos.keys()}')
i_pesquisado = input('deseja saber o preço de qual produto?:').lower()
if i_pesquisado in dic_precos:
    print(f'R${dic_precos[i_pesquisado]:,.2f}')
else:
    print('produto não encontrado, tente novamente!')