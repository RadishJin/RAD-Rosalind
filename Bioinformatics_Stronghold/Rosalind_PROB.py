from math import log10
with open("data/rosalind_prob.txt", "rt") as f:
    raw = f.read()

# raw = """
# ACGATACAA
# 0.129 0.287 0.423 0.476 0.641 0.742 0.783
# """

sequence, prob = raw.strip().splitlines()
# print(sequence, prob)
prob_list = list(map(float, prob.split()))
# print(prob_list)

# test
total_list = []
for pb in prob_list:
    gc_pb = pb/2
    at_pb = (1-pb)/2
    gc_num = sequence.count("C") + sequence.count("G")
    at_num = sequence.count("A") + sequence.count("T")
    total = "{:.3f}".format(log10((gc_pb ** gc_num) * (at_pb ** at_num)))
    total_list.append(total)

print(" ".join(total_list))

