with open("data/rosalind_revc.txt", "r") as f:
    DNAseq = f.read().strip()

Comp_table = str.maketrans("GCAT", "CGTA")

rev_comp = DNAseq.translate(Comp_table)[::-1]

print(rev_comp)


# 문자열 뒤집기 (Reverse) : sequence[::-1]
# reverse=True 정렬과 차이점 : [::-1]은 순서를 거꾸로 뒤집고, sorted(..., reverse=True)는 알파벳 역순 정렬임
# 역상보 서열(Reverse Complement) : dna.translate(table)[::-1]
