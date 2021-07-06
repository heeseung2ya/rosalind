data = 'rosalind_hamm.txt'
seq = ''
seq1 = ''
seq2 = ''
result = 0


with open(data, 'r') as db:
    seq = db.readlines()
seq1 = seq[0].strip()
seq2 = seq[1].strip()

for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        result += 1

print(result)
