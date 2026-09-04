import math

with open('data/rosalind_pmch.txt', 'r') as f:
    raw = f.read()

# raw = """
# >Rosalind_23
# AGCUAGUCAU
# """

current_id = ""
seq_dict = {}
for line in raw.splitlines():
    line = line.strip()
    if not line:
        continue
    if line.startswith(">"):
        current_id = line[1:]
        seq_dict[current_id] = ""
    else:
        seq_dict[current_id] += line

sequence = list(seq_dict.values())[0]
print(sequence)

num_A = sequence.count("A")
num_C = sequence.count("C")
print(num_A, num_C)

final = math.factorial(num_A) * math.factorial(num_C)
print(final)