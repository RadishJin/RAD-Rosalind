with open("data/rosalind_lcsm.txt", "r") as f:
    raw = f.read()

# raw = """
# >Rosalind_1
# GATTACA
# >Rosalind_2
# TAGACCA
# >Rosalind_3
# ATACA
# """

raw_list = raw.splitlines()

# Parsing
current_id = ""
seq_dict = {}
for i in raw_list:
    i = i.strip()
    if not i:
        continue
    if i.startswith(">"):
        current_id = i[1:]
        seq_dict[current_id] = ""
    else:
        seq_dict[current_id] += i
print(seq_dict)

# 가장 짧은 strand를 main으로 처리하고, 나머지 문자열 짧은 순서대로 리스트화
seq_list = list(seq_dict.values())
print(seq_list)
main = min(seq_list, key = len)
seq_list.remove(main)
seq_list = sorted(seq_list, key= lambda x: len(x))
print(main, seq_list)

# 가장 긴 공통부분 찾기
test = ""
found_motif = ""
for sub_len in range(len(main), 0, -1):
    for start in range(len(main) - sub_len + 1):
        test = main[start : start + sub_len]
        if all(test in seq for seq in seq_list):
            found_motif = test
            break
    if found_motif:
        break

print(found_motif)
    
