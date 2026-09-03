from Bio.Seq import Seq

# 파일 읽어오기
with open('data/rosalind_revp.txt', 'r') as f:
    raw = f.read()


# # 테스트용 임시 데이터
# raw = """
# >Rosalind_24
# TCAATGCATGCGGGTCTATATGCAT
# """


# 파싱 1차 (읽기)
raw_list = raw.splitlines()

current_id = ""
seq_dict = {}
for line in raw_list:
    line = line.strip()
    if not line:
        continue
    if line.startswith(">"):
        current_id = line[1:]
        seq_dict[current_id] = ""
    else:
        seq_dict[current_id] += line

template = Seq(list(seq_dict.values())[0])
print(template)
print("Template Saved")

rev_comp = template.reverse_complement()
print(rev_comp)
print("Reverse Complement Saved")

# T0 E1 M2 P3 L4 A5 T6 E7

# 제한효소 위치 찾기 반복문
locus_list = []
n = len(template)

# 길이가 4부터 12까지 (2k 형태가 아닌 전체 길이 length로 탐색)
for length in range(4, 13):
    for i in range(n - length + 1):
        segment = template[i : i + length]
        
        # 서브스트링 자체가 자신의 역상보쇄와 일치하는가?
        if segment == segment.reverse_complement():
            locus_list.append((i + 1, length)) # 1-based index

# Rosalind 문제 요구사항대로 출력 (순서 상관없음)
for pos, length in locus_list:
    print(pos, length)
