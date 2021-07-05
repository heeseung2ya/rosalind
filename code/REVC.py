data = 'rosalind_revc.txt'

rev_seq = ''
rev_com_seq = ''

with open(data, 'r') as db:
    for line in db.readlines():
        rev_seq = line[::-1]
        for s in rev_seq:
            if s == 'A':
                rev_com_seq += 'T'
            elif s == 'C':
                rev_com_seq += 'G'
            elif s == 'G':
                rev_com_seq += 'C'
            elif s == 'T':
                rev_com_seq += 'A'
print(rev_com_seq)          
