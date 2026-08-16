with open("data/rosalind_ini4.txt", "r") as f:
    raw_data = f.read()

a, b = map(int, raw_data.strip().split())

odd_nums = []

for i in range(a, b+1):
    if i%2 == 0:
        continue
    else:
        odd_nums.append(i)

total = sum(odd_nums)
print(f"{total}")