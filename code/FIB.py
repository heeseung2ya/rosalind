data = 'rosalind_fib.txt'

with open(data, 'r') as db:
    for line in db.readlines():
        tmp = line.split(' ')

month = int(tmp[0])
k = int(tmp[1])

l_result = [1, 1]
for i in range(1, month-1):
    l_result.append(l_result[-1]+(k * l_result[-2]))
print(l_result)


