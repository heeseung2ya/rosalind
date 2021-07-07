dataset = "rosalind_prot.txt"
codon = "RNA_codon_table.txt"
d_codon = {}
protein = ""

with open(codon, "r") as db:
    for line in db.readlines():
        tmp_split = line.strip().split()
        for i in range(0, len(tmp_split), 2):
            d_codon[tmp_split[i]] = tmp_split[i + 1]

lines = open(dataset, "r").readlines()
for line in lines:
    for i in range(len(line)):
        if (i + 1) % 3 == 2 or (i + 1) % 3 == 0:
            continue
        elif d_codon[line[i : i + 3]] == "Stop":
            print("{} -> STOP".format(line[i : i + 3]))
            break
        else:
            print("{} -> {}".format(line[i : i + 3], d_codon[line[i : i + 3]]))
            protein += d_codon[line[i : i + 3]]
open(dataset, "r").close()
print(protein)

