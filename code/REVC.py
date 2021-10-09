filename = "../rosalind_revc.txt"
fr = open(filename, "r")

d_comp = {"A":"T", "C":"G", "G":"C", "T":"A"}
comp_seq = ""
for line in fr:
    line = line.strip()
    for base in line:
        comp_seq += d_comp[base]
rev_comp_seq = comp_seq[::-1]
print(rev_comp_seq)
