data = 'rosalind_subs.txt'
seq = ''
motif = ''

with open(data, 'r') as db:
    tmp = db.readlines()
seq = tmp[0].strip()
motif = tmp[1].strip()

for i in range(len(seq)):
    if seq[i:i+len(motif)] == motif:
        print(i+1, end=' ')
