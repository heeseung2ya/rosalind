# 2021년 9월 26일 업데이트

# import sys
filename = "rosalind_gc.txt"
# filename = sys.argv[1]

d_DNA = {}
d_GC = {}
header = ""
read_file = open(filename, "r")
for line in read_file:
    line = line.strip()

    if line.startswith(">"):
        header = line[1:]
        d_DNA[header] = ""
    else:
        d_DNA[header] += line


for key, value in d_DNA.items():
    d_GC[key] = (value.count("G") + value.count("C")) / len(value) * 100

for key, value in d_GC.items():
    if value == max(d_GC.values()):
        max_key = key
        max_value = value

print(max_key)
print(f"{max_value:.6f}")




'''
# 이전 코드
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
'''
