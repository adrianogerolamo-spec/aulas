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
'''
for id in fastaDict.keys():
#    print(f'id: {id}')
#    print(f'fasta: {fastaDict[id]}')
    if id not in ntCounts:
        ntCounts[id]={}
    nt_uniq = set(fastaDict[id])
    for nt in nt_uniq:
        if nt not in ntCounts[id]:
            ntCounts[id][nt] = fastaDict[id].count(nt)

with open("output.txt", "w") as o:
    for id in ntCounts:
        o.write(f'id : {id} \n count: {ntCounts[id]} \n fasta:{fastaDict[id]}')

'''
