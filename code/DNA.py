filename = "../rosalind_dna.txt"
fr = open(filename, "r")

cnt_A = 0
cnt_C = 0
cnt_G = 0
cnt_T = 0

for line in fr:
    line = line.strip()
    cnt_A += line.count("A")
    cnt_C += line.count("C")
    cnt_G += line.count("G")
    cnt_T += line.count("T")

print(cnt_A, cnt_C, cnt_G, cnt_T)
