# with open("data/rosalind_prob.txt", "rt") as f:
#     raw = f.read()

raw = """
ACGATACAA
0.129 0.287 0.423 0.476 0.641 0.742 0.783
"""

sequence, prob = raw.strip().splitlines()
print(sequence, prob)