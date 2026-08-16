from collections import Counter

with open("data/rosalind_dna.txt", "r") as f:
    raw_data = f.read()

sequence = raw_data.strip()

Bases = Counter(sequence)

for N in Bases.values():
    print(N, end=" ")

# 딕셔너리.values() : 딕셔너리의 value만 반환
# 딕셔너리.items() : 딕셔너리의 key, value를 튜플 형태로 반환
# 딕셔너리.keys() : 딕셔너리의 key만 반환