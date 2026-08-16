with open("data/rosalind_rna.txt", "r") as f:
    DNAseq = f.read().strip()

RNAseq = DNAseq.replace("T", "U")

print(RNAseq)



# str.replace("기존문자", "새문자") : 특정 문자를 찾아 다른 문자로 변경 (새 문자열 반환)
# 예시: rna = dna.replace("T", "U")

# 테이블 = str.maketrans("기존문자들", "치환문자들") : 1:1 대응 변환 규칙 테이블(Table) 생성
# str.translate(테이블) : 생성한 변환 규칙을 적용하여 한 번에 일괄 치환 (상보적 서열 변환에 사용)
# 예시: table = str.maketrans("ATCG", "TAGC"); complement = dna.translate(table)