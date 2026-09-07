import math
import random
import itertools

# with open("data/rosalind_perm.txt") as f:
#     raw = f.read()

raw = "6"

n = int(raw.strip())
# print(n)

# permutations = math.factorial(n)
# print(permutations)

# num_list = list(range(1, n + 1))

# num_set = []

# for i in range(1000):
#     random.shuffle(num_list)
#     num_set.append(num_list.copy())

# num_set = set(tuple(x) for x in num_set)
# # print(num_set)

# for element in num_set:
#     print(" ".join(map(str, element)))

num_list = list(range(1, n + 1))

perms = list(itertools.permutations(num_list))
# print(perms)

print(len(perms))
for perm in perms:
    print(" ".join(map(str, perm)))


