faturamento = 1000
custo = 700
lucro = faturamento - custo

print(f'faturamento:{faturamento}, custo:{custo}, lucro:{lucro}')
print('faturamento:' + str(faturamento) + ', custo:' + str(custo) + 
      ', lucro:' + str(lucro))

email = 'email_FALSO@gmail.com'
#        01234567891011 ->o "@" esta na posição 11
print(email.lower())
print(email.find('@')) #o find da a posição do carctere no texto
print(email.find('$')) #se não houver o cartere, a posição é -1

posicao = email.find('@')
servidor = email[posicao:] #posicao 11 até o final
nome_email = email[:posicao]
print(servidor)
print(email[posicao + 1:]) #o +1 faz pular uma posição
print(nome_email.lower())

#tamanho de um texto
tamanho = len(email)
print('total de caracteres:' + str(tamanho))

#trocar um pedaço do texto
print(email.replace('@gmail.com','@hotmail'))
print(email.lower().replace('@gmail.com','@hotmail'))

nome = 'adriano gerolamo'
print(nome.capitalize()) #primeira letra fica maiuscula
print(nome.title()) #cada primeira letra fica maiuscula

#especiais - formatacao numerica
print(f'faturamento:R${faturamento:,.2f}')
# , marcador de milhar
# : vou editar
# . vou por casas decimais
# 2 duas casas
# f de float

margem = lucro / faturamento
print(f'margem {margem:.1%}') #codigo pra percentual

print(f'faturamento:{faturamento}\ncusto:{custo}\nlucro:{lucro}')
#\ no texto traz um carctere especial, no caso o "n" seria o "enter"

#exercicios
print('exercicios')
email2 = 'emailfalso2@gmail.com'
nome2 = 'adriano gerolamo do nascimento'

#descubra o servidor do email
posicao2 = email2.find('@')
servidor2 = email2[posicao2:]
print(f'o servidor é:{servidor2}')

#exibir o primeiro nome do usuario
posicao3 = nome2.find(' ')
p_nome = nome2[:posicao3]

print(f'o primeiro nome é: {p_nome}')

#construa a mensagem: usuario primeiro nome cadastrado com sucesso com email tal
print(f'usuario {p_nome.capitalize()} foi registrado com sucesso utilizando o email {email2}')

#construa a mensagem: enviamos uma mensagem de confirmação para o email e***@gmail.com
nome_email2 = email2[1:posicao2]
print(f'enviamos uma mensagem de confirmação para o email {email2.replace(nome_email2,'****')}')