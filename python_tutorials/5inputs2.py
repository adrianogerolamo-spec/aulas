#o vendedor deve receber um bonus de 1% das vendas
vendas = input('digite a soma total de suas vendas:') #input cria um formato de texto!!!
vendas = vendas.replace('R$','')
vendas = int(float(vendas)) #float transforma texto em numero com casa decimal
bonus = vendas * 0.01 
print(f'seu bonus hoje foi de: R${bonus:,.2f}')