from modulefiles import find_locus_location

with open("data/rosalind_subs.txt", "r") as f:
    raw = f.read()

# raw = """
# GATATATGCATATACTT
# ATAT
# """

seq_list = raw.strip().splitlines()

n = find_locus_location(seq_list[1], seq_list[0])

print(" ".join(str(i+1) for i in n))


