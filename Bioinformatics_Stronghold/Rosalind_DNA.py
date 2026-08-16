from collections import Counter

with open("data/rosalind_dna.txt", "r") as f:
    raw_data = f.read()

sequence = raw_data.strip()

Bases = Counter(sequence)
Sorted_Bases = dict(sorted(Bases.items()))

# print(f"{Sorted_Bases})")

for N in Sorted_Bases.values():
    print(N, end=" ")

# 딕셔너리.values() : 딕셔너리의 value만 반환
# 딕셔너리.items() : 딕셔너리의 key, value를 튜플 형태로 반환
# 딕셔너리.keys() : 딕셔너리의 key만 반환

# sorted(딕셔너리) : 딕셔너리의 key를 기준으로 정렬된 리스트 반환 (Value 데이터 다 날아감)
# sorted(딕셔너리.items()) : 딕셔너리의 key를 기준으로 정렬된 튜플 리스트 반환
# dict(튜플 리스트) : 튜플 리스트를 딕셔너리로 반환