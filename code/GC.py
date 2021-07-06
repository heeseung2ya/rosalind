data = 'rosalind_gc.txt' # path of data

d_seq = {}

with open(data, 'r') as db:
    for line in db.readlines():
        if line.startswith('>') == True:
            total_len = 0
            gc_cnt = 0
            seq_name = line[1:].strip()
            d_seq[seq_name] = 0
        else:
            total_len += len(line.strip())
            gc_cnt += line.strip().count('G') + line.strip().count('C')
            d_seq[seq_name] = round(gc_cnt / total_len * 100, 6)

print(d_seq)
for k, v in d_seq.items():
    if max(d_seq.values()) == v:
        print(k)
        print(v)
