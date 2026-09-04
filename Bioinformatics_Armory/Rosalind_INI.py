with open("data/rosalind_ini.txt") as f:
    raw = f.read()

# raw = """
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# """

sequence = raw.strip()

count_a = sequence.count("A")
count_c = sequence.count("C")
count_g = sequence.count("G")
count_t = sequence.count("T")

print(count_a, count_c, count_g, count_t)