

#ex5
genes = {}
count = 0

with open("Python_06.fastq", "r") as file:
    while True:
        count += 1        
        for line in file:
            if count%2 ==0:
                line = line.rstrip()
                id, seq = line.split()
                genes[id] = seq

print(genes)
