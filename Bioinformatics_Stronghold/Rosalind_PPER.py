from math import perm

# with open("data/rosalind_pper.txt", "r") as f:
#     raw = f.read()

raw = """
86 8
"""

n, k = map(int, raw.strip().split())
# print(n, k)

a = perm(n, k)
b = a % 1000000

print(b)
