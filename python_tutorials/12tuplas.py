def calcular_imposto2(preco, ir=0.275, csll=0.035, iss=0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll, imposto_iss #por padrao devolve uma tuplapython como resp
#que sao imutaveis, ex: (275.0, 35.0, 50.0) imutavel

total = calcular_imposto2(1000)
print(total)
""" print(total[0]) #-> pega um indice especifico da tupla
print(total[1])
print(total[2]) """

#unpacking da tupla
ir, csll, iss = total #ta colocando os valores da tupla em 3 objetos diferentes q estao sendo criados
print(ir, csll, iss, sep='\n')

tamanho_tela = (1920, 1080) #isso e um objeto recebendo uma tupla, que e imutavel

print('--------------------------------------------------------------------')
print('EXERCICIO') #3:44:30
#pra cada venda o vendedor ganha R$2 e 1% do valor da venda
#calcular: o valor total de bonus pago e o bonus de cada vendedor

vendas = {
    'Andre': [1000, 500, 300, 5000, 1500, 80, 3000],
    'Andressa': [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    'Alan': [800, 100],
    'Ana': [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180, 100, 120, 110, 130, 140]
}

bonus_total_pago = 0

for vendedor in vendas:
    bonus_vendedor_2 = (len(vendas[vendedor]))*2
    bonus_vendedor_per = sum(vendas[vendedor])*0.01
    bonus_vendedor_total = bonus_vendedor_2 + bonus_vendedor_per
    bonus_total_pago = bonus_total_pago + bonus_vendedor_total
    print(f'vendedor:{vendedor}, bonus total do vendedor: R${bonus_vendedor_total:,.2f}')
print(f'bonus pago pela empresa: R${bonus_total_pago:,.2f}')

#repita utilizando uma funcao
print('--------------------------------------------------------------------')

print(vendas.items()) #transforma os itens do dicionario em tuplas

for vendedor, lista_vendas in vendas.items():
    print(vendedor)
    print(lista_vendas) #lista de vendas vira a segunda parte do item no dicionario e deixa de ser
#tupla, vendedor vai pra "key" e lista_vendas vai pra "value"

print('--------------------------------------------------------------------')
print('EXERCICIO')
def calcular_bonus_total(vendedor):
    bonus_total_pago = 0
    bonus_vendedor_2 = (len(vendas[vendedor]))*2
    bonus_vendedor_per = sum(vendas[vendedor])*0.01
    bonus_vendedor_total = bonus_vendedor_2 + bonus_vendedor_per
    bonus_total_pago = bonus_total_pago + bonus_vendedor_total
    print(f'vendedor:{vendedor}, bonus total do vendedor: R${bonus_vendedor_total:,.2f}') #nao e necessario nesse caso ja q e so pra dar o bonus total pago, mas mostra que pode
    return bonus_total_pago

for vendedor in vendas:
    calcular_bonus_total(vendedor)

print(f'bonus total pago pela empresa: R${bonus_total_pago:,.2f}')
print('--------------------------------------------------------------------')