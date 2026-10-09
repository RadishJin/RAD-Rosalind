from math import factorial
from itertools import permutations, product

# with open("data/rosalind_pre.txt", "r") as f:
#     raw = f.read()

raw = '4'

n = int(raw.strip())
total = (2**n) * factorial(n)

n_list = list(permutations(range(1, n+1)))
sign_list = list(product([-1, 1], repeat= n))

print(total)
for i in n_list:
    for j in sign_list:
        result = [a * b for a, b in zip(i, j)]
        print(*result)

