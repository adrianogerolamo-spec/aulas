#ler arquivos no geral
arquivo = open('vendas.txt', 'r') #se nao estiver no msm local tem que por o caminho completo (C:\...)
# o 'r' significa read(ler)

#fazer o que quiser com o arquivo

arquivo.close() #tem que fechar se nao o arquivo fica eternamente aberto

with open('vendas.txt', 'r') as arquivo:
    #fazer o que quiser com o arquivo, e o with fecha ele automaticamente
    infos = arquivo.readlines()

vendas_totais = 0

for item in infos:
    item = item.replace('\n', '')
    resultado = item.split(',') #cria uma lista com textos(str)
    valor = resultado[1] #pega o segundo item dessa lista
    valor = valor.replace(' ', '')
    valor = float(valor)
    vendas_totais = vendas_totais + valor

print(vendas_totais)