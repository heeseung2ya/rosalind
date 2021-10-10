filename = "../rosalind_tran.txt"
fr = open(filename, "r")

d_transi = {"A":"G", "G":"A", "C":"T", "T":"C"}
d_transv = {"A":(["C", "T"]), "G":(["C", "T"]), "C":(["A", "G"]), "T":(["A", "G"])}
transi_cnt = 0
transv_cnt = 0


s_cnt = -1
s = []
for line in fr:
    line = line.strip()
    if line.startswith(">"):
        s_cnt += 1
    else:
        try:
            s[s_cnt] += line
        except:
            s.append(line)

for i in range(len(s[0])):
    if s[1][i] == d_transi[s[0][i]]:
        transi_cnt += 1
    elif s[1][i] in d_transv[s[0][i]]:
        transv_cnt += 1

sv_ratio = transi_cnt / transv_cnt  
print(sv_ratio)      
