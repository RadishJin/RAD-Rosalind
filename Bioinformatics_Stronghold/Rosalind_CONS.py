import numpy as np 
import sys


with open("data/rosalind_cons.txt", "r") as f:
    raw = f.read()

# raw = """
# >Rosalind_1
# ATCC
# AGCT
# >Rosalind_2
# GGGC
# AACT
# >Rosalind_3
# ATGG
# ATCT
# >Rosalind_4
# AAGC
# AACC
# >Rosalind_5
# TTGG
# AACT
# >Rosalind_6
# ATGC
# CATT
# >Rosalind_7
# ATGG
# CACT
# """

raw_lines = raw.splitlines()

def profile(raw_lines : list[str]) -> list[int]:

    # 데이터 딕셔너리 형태로 파싱
    sequences = {}
    for i in raw_lines:
        i = i.strip()
        if not i:
            continue
        if i.startswith(">"):
            current_id = i[1:]
            sequences[current_id] = ""
        else:
            sequences[current_id] += i
    print("FASTA Successfully Parsed")

    # for i in sequences.keys():
    #     print(len(str(sequences[i])))
    

    # 원하는 형태의 딕셔너리로 재구성 (Numpy 이용)
    seq_matrix = np.array([list(s) for s in sequences.values()])

    lengths = [len(s) for s in sequences.values()]
    print(set(lengths))

    print("Completed ordinating Matrix")
    A = (seq_matrix == "A").sum(axis = 0)
    C = (seq_matrix == "C").sum(axis = 0)
    G = (seq_matrix == "G").sum(axis = 0)
    T = (seq_matrix == "T").sum(axis = 0)

    profile_matrix = np.array([A,C,G,T])
    print("Profile Completed")

    return profile_matrix

# 원래 터미널 출력을 백업
original_stdout = sys.stdout

with open('output.txt', 'w', encoding='utf-8') as f:
    sys.stdout = f  # 이후 모든 print는 output.txt로 들어감

    profile_matrix = profile(raw_lines)

    # 빈도 수 가장 높은 서열 정하기
    bases = np.array(["A", "C", "G", "T"])
    max_indices = profile_matrix.argmax(axis = 0)
    consensus = bases[max_indices]
    print("".join(consensus))
    for base, row in zip(bases, profile_matrix):
        row_str = " ".join(map(str,row))
        print(f"{base}: {row_str}")

