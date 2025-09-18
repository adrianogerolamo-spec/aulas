lista = ['chocolate', 'cafe', 'jogos', 'arte', 'livros']

def imprimir_meio(lista):
    meio_lista = lista[len(lista)//2]
    print(meio_lista)

imprimir_meio(lista)

#lista.append('trigger')
#imprimir_meio(lista)
#lista.append('steam')
#imprimir_meio(lista)

#ex2:
taxa = "sapiens, erectus, neanderthalensis"
print(type(taxa))
taxa_list = taxa.split(", ")
print(taxa_list)
print(sorted(taxa_list))
print(type(taxa_list))

#ex3:
my_list = ['a', 'bb', 'ccc']
list_copy = my_list
print(my_list)
list_copy.append('dddd')
#adicionou??
print(my_list)

my_list2 = ['a', 'bb', 'ccc']
list_copy2 = my_list2.copy()
print(my_list2)
list_copy2.append('dddd')
print(my_list2)
