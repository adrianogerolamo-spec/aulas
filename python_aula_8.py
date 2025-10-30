#ex1
'''
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
        print(f"gene {gene[0]}:")
        for char in "ATCG":
            print(f"{char}: "+str(gene[1].count(char)))
'''
import sys

file = ''
try:
  file = sys.argv[1]
  print("User provided file name:" , file)
  if not file.endswith('.fasta'):
    raise ValueError("Not a FASTA file")
  FASTA = open(file, "r")
  for line in FASTA:
    print(line)
except IndexError:
  print("Please provide a file name")
except IOError as ex:
  print("Can't find file:" , file , ': ' , ex.strerror  )        
