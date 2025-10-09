#ex5
import sys

file = sys.argv[1]
fastaDict = {}

#seq = ''
#identificador = ''

with open(file, 'rt') as f:
    for line in f:
        line = line.rstrip() #remove o char invisivel
        if line.startswith("@"):
            identificador = line.split(" ")[0].replace('@','')
            if identificador not in fastaDict.keys():
                fastaDict[identificador] = ''
        else:
            fastaDict[identificador] = fastaDict[identificador] + line
for id in fastaDict.keys():
    print(f'id: {id}')
    print(f'fasta: {fastaDict[id]}')
