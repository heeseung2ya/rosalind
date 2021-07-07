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

# dataset이 항상 "AUG"부터 시작한다는 보장이 없으니, 첫 번째 "AUG"가 등장하면 그 때부터 string 변수 protein에 amino acid를 저장하기 시작하는 기능도 추가하고 싶었는데 일단 졸려서 포기... 다음에 추가하는 걸로...ㅎㅎ

