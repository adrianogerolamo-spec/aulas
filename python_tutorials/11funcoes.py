precos = [1500, 1000, 800, 2000]

imposto_total = 0

def calcular_imposto(preco, aliquota1=0.15, aliquota2=0.1):#as variaveis criadas dentro de uma funcao so
    if preco >1000:#existem dentro dela, e mais de um parametro pode ser definido
        imposto = preco * aliquota1
    else:
        imposto = preco * aliquota2
    print(f'preco {preco}, imposto {imposto}')
    return imposto#retorna a variavel pro codigo


for preco in precos:
    imposto = calcular_imposto(preco) # o valor de um parametro pode
    imposto_total = imposto_total + imposto #ser redefinido caso haja necessidade 
#ex: calcular_imposto(preco, aliquota1 = 0.25, aliquota2 = 0.15)
#tbm pode ser definido por posicao, ex: calcular_imposto(preco, 0.25, 0.15)
print(imposto_total)

""" def calcular_imposto2(preco, ir=0.275, csll=0.035, iss=0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll, imposto_iss #retorna multiplos valores como resposta

total = calcular_imposto2(1000)
print(total) """