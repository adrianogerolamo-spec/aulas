#ex1

with open("Python_08.fasta", "rt") as file:
    #print(len(file.read()))
    #text = file.read()
    fasta = file.read().split('>')
    genes = []
    count = 1
    for gene in fasta:
        genes.append([str(count), gene])
        count += 1
    #print(len(genes))
    for gene in genes:
        print("gene "+gene[0]+":\n"+ "A: "+str(gene[1].count('A')))
        
