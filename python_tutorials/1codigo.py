faturamento = 1200 #numeros inteiros -> int
custo = 770
novas_vendas = 300
faturamento = novas_vendas + faturamento
taxa_imposto = 0.1 #decimal -> float
mensagem = 'o faturamento foi de' #texto -> string ->str
teve_lucro = False #verdadeiro ou falso -> boolean
imposto = taxa_imposto * faturamento
#numeros inteiros
#numeors decimais
#texto
#booleanos

print('faturamento', faturamento)
print('custo', custo)
print('lucro', faturamento - custo - imposto)
print(mensagem, faturamento)