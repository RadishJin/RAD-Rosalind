with open("data/rosalind_hamm.txt", "r") as f:
    raw = f.read()

# data = """
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# """

# raw = data.strip().splitlines()

def Hamming_Distance(n: list) -> int:
    a, b = n[0], n[1]
    distance = 0
    for i in range(0, len(a)):
        if a[i] != b[i]:
            distance += 1
    return distance

print(Hamming_Distance(raw.strip().splitlines()))





    