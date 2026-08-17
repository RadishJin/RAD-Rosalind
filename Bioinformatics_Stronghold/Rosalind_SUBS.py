with open("data/rosalind_subs.txt", "r") as f:
    raw = f.read().strip().splitlines()

# data = """
# GATATATGCATATACTT
# ATAT
# """

# raw = data.strip().splitlines()
# # print(raw)

def Finding(n: list) -> list:
    a, b = n[0], n[1]
    Locus = []
    for i in range(0, len(a) - len(b) +1):
        if a[i : i + len(b)] == b:
            Locus.append(i + 1)
    return Locus

print(*Finding(raw))

# *리스트 하면 언패킹 즉 리스트 안의 요소들을 공백으로 띄워서 반환해줌

# .join 사용법 (Gemini)

# words = ["DNA", "RNA", "Protein"]

# # 1. 공백으로 이어 붙이기
# result1 = " ".join(words)
# print(result1)  # 출력: DNA RNA Protein

# # 2. 쉼표(,)와 공백으로 이어 붙이기
# result2 = ", ".join(words)
# print(result2)  # 출력: DNA, RNA, Protein

# # 3. 구분자 없이 그냥 붙이기
# result3 = "".join(words)
# print(result3)  # 출력: DNARNAProtein

# # 4. 줄바꿈(\n)으로 이어 붙이기
# result4 = "\n".join(words)
# print(result4)
# # 출력:
# # DNA
# # RNA
# # Protein

