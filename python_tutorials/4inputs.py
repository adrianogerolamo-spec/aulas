email2 = input('digite seu email:').lower()
nome2 = input('digite seu nome completo:')

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