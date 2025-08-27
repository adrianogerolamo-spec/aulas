for i in range(5): #repita o codigo abaixo range(x) vezes
    print('bruhh')

#for item in lista: #para cada item em uma lista
    #faca este codigo

precos = [900, 1000, 1500]

for preco in precos: #o codigo repete pra cada item da lista
    imposto = preco * 0.1 #preco vira o objeto que representa o item da lista
    print(f'preço: {preco}, imposto: {imposto}, total: {preco - imposto}')

#exercicios
# preco até 1000 imposto de 10%
# preco acima de 1000 imposto de 15%

for preco in precos:
    if preco >1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1

    print(f'preço: {preco}, imposto: {imposto}, total: {preco - imposto}')

#exibir o total de imposto
imposto_total = 0 #acumulado zerado
for preco in precos:
    if preco >1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1
    imposto_total = imposto_total + imposto #cada iteracao do for adiciona no objeto do acumulado
print(f'o total cobrado em impostos foi: R${imposto_total:,.2f}') #printa o total

print('--------------------------------------------------------------')
print('EXERCICIO DIFICIL') #3:06:28

vendas_22 = {'jan': 15000, 'fev': 15500, 'mar': 14000, 'abr': 16600, 'mai': 16300, 'jun': 17000}
vendas_23 = {'jan': 17000, 'fev': 15000, 'mar': 17500, 'abr': 16900, 'mai': 16000, 'jun': 18500}

#saber o quanto variou percentualmente cada mes de 2023 em comparação com 2022
""" for mes in vendas_23:
    diferenca = vendas_23[mes] - vendas_22[mes]
    variacao = (100 * diferenca)/vendas_22[mes]
    print(f'A variacao foi de {variacao:.2f}%')
 """
#também pode ser feito como

for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    dif_perc = valor_23 / valor_22 - 1 #ex pra jan: 1.1333
    print(f'A variacao foi de {dif_perc:.2%}')

#simulem: se a empresa tivesse pelo menos empatado com 2022 nos dias que ela vendeu menos, qual
#seria o faturamento?

faturamento = 0
for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    if valor_23 < valor_22:
        valor_23 = valor_22 #XDXDXDXD no it isn't
    faturamento = faturamento + valor_23
print(f'O valor do faturamento seria R${faturamento:,.2f}')