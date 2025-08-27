faturamento = 1_000 # o _ não edita o numero, é uma ajuda visual
custo = 700
novas_vendas = 300

faturamento = faturamento + novas_vendas
imposto = faturamento * 0.1
lucro = faturamento - custo - imposto

#print('imposto', imposto)
#print('faturamento', faturamento)
#print('lucro', lucro)

margem_lucro = lucro / faturamento

#print('margem lucro', margem_lucro)

restituicao = imposto * 0.1
#print('restituicao', restituicao)

restituicao = faturamento ** 0.1
#print('restituicao', restituicao)

#Mod(%) -> resto da divisão de um numero pelo outro
#ex: 10/3 -> resto 1 -> 10%3 = 1
#print('mod de 10 por 3 é igual a', 10 % 3)

tempo_em_meses = 160
tempo_em_anos = tempo_em_meses / 12
tempo_em_anos_int = int(tempo_em_meses / 12)
meses_restantes = tempo_em_meses % 12

print('tempo_em_meses', tempo_em_meses)
print('tempo_em_anos', tempo_em_anos)
print('tempo_em_anos_int', tempo_em_anos_int)
print('meses_restantes', meses_restantes)

numero = 6.7
print(round(numero))