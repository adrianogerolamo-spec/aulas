#sistema de consulta de preço, se o produto não existe, informar que não existe (2:21:38)
#supondo que a posicao do valor na lista e igual a posicao do produto que ela representa
precos = [1500, 1000, 800, 2000]
produtos = ['celular', 'camera', 'fone de ouvido', 'monitor']

v_pesquisado = input('deseja saber o preco de qual aparelho? digite N caso nao queira: ').lower()

if not v_pesquisado == 'n':
    if v_pesquisado in produtos:
        posicao_produto = produtos.index(v_pesquisado)
        print(f'o preco do produto e: R${precos[posicao_produto]:,.2f}')
    else:
        print('produto indisponivel!')
else:
    print('ok')

#pro usuario ser capaz de modificar o preco do produto
p_p_mudar = input('deseja mudar o valor de qual produto? digite N caso nao queira: ').lower()

if not p_p_mudar == 'n':
    if p_p_mudar in produtos:
        posicao_ppm = produtos.index(p_p_mudar)
        n_preco = input('digite o novo valor: ')
        n_preco = n_preco.replace('R$', '')
        n_preco = int(float(n_preco))
        precos[posicao_ppm] = n_preco
        print(f'o novo preco do produto e: R${precos[posicao_ppm]:,.2f}')
    else:
        print('produto indisponivel!')
else:
    print('ok')