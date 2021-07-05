data = 'rosalind_dna.txt'

base = ['A', 'C', 'G', 'T']
base_cnt = [0, 0, 0, 0]

with open(data, 'r') as db:
    for line in db.readlines():
        for b in base:
            base_cnt[base.index(b)] += line.count(b)
for i in base_cnt:
    print(i, end=' ')
