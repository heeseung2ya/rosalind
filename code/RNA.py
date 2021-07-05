data = 'rosalind_rna.txt'

with open(data, 'r') as db:
    for line in db.readlines():
        print(line.replace('T', 'U'))
