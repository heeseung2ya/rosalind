filename = "../rosalind_rna.txt"
fr = open(filename, "r")

rseq = ""
for line in fr:
    line = line.strip()
    rseq += line.replace("T", "U")

print(rseq)
