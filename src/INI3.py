with open("data/rosalind_ini3.txt", "r") as f:
    raw_data = f.readlines()

str_data = raw_data[0].strip()

int_data = raw_data[1].strip()
nums = int_data.split()
a, b, c, d = map(int,nums)

Chunk1 = str_data[a:b+1]
Chunk2 = str_data[c:d+1]

print(f"{Chunk1} {Chunk2}")