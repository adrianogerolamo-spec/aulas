#ex1:
lista = ['chocolate', 'cafe', 'jogos', 'arte', 'livros']

def imprimir_meio(lista):
    if len(lista)%2 != 0:
        meio_lista = lista[len(lista)//2]
        #// da o inteiro do valor
        print(len(lista)//2)
        print(meio_lista)
    else:
        print("numero da lista e par")

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
#x = y cria uma "referência mutavel"
print(my_list)

my_list2 = ['a', 'bb', 'ccc']
# x = y.copy() e um metodo, literalmente faz uma copia do que esta na memoria da variavel y e passa para a x
list_copy2 = my_list2.copy()
print(my_list2)
list_copy2.append('dddd')
print(my_list2)

#ex5:
n = 1000

# Initialize the factorial variable to 1
fact = 1

# Calculate the factorial using a for loop
for i in range(1, n + 1):
    fact *= i

print(fact)

contador = 1
fact2 = 1

while contador <= 1000:
    contador += 1
    fact2 *= contador

print(fact2)

#ex12:
#https://www.w3schools.com/python/python_lists_comprehension.asp
lista_12 = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

