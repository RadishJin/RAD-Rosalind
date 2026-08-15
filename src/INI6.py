with open("data/rosalind_ini6.txt", "r") as f:
    raw_data = f.read()

# word_list = raw_data.strip().split()
# count = {}
# for w in word_list:
#     if w in count:
#         count[w] += 1
#     else:
#         count[w] = 1

# for k, v in count.items():
#     print(f"{k} {v}")

from collections import Counter
word_list = raw_data.strip().split()

count = Counter(word_list)

for k, v in count.items():
    print(f"{k} {v}")   