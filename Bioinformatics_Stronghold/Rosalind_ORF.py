from Bio.Data import CodonTable
from Bio.Seq import Seq # 번역기 가져오기

with open("data/rosalind_orf.txt", "r") as f:
    raw = f.read()

# raw = """
# >Rosalind_99
# AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
# """
raw_list = raw.strip().splitlines()

def find_orf(raw_list: list[str]) -> list[str]:

    # 파싱
    sequence = ""
    for i in raw_list:
        if not i:
            continue
        elif i.startswith(">"):
            continue
        else:
            sequence += i
    print("DNA Sequencing Completed")
    print(sequence)

    # 코돈 테이블 가져오기
    codon_table = CodonTable.unambiguous_dna_by_id[1]
    print("CodonTable Loaded")

    # 번역되는 가능한 모든 가닥 정리
    start = ["ATG"]
    stop = codon_table.stop_codons
    print(stop)

    # 개시 코돈(ATG) 위치 모두 탐색
    results = []
    for i in range(len(sequence) - 2):
        codon = sequence[i : i + 3]
        if codon in start:
            # ATG를 발견하면 해당 위치부터 3bp씩 진행하며 Stop codon 탐색
            for j in range(i, len(sequence) - 2, 3):
                curr_codon = sequence[j : j + 3]
                if curr_codon in stop:
                    # Start부터 Stop 직전까지 슬라이싱 후 번역
                    orf = Seq(sequence[i:j])
                    protein = str(orf.translate())
                    results.append(protein)
                    break  # 가장 먼저 나오는 Stop codon에서 해당 ORF 종결

    # 역방향 탐색
    rev_sequence = str(Seq(sequence).reverse_complement())
    for i in range(len(sequence) - 2):
        codon = rev_sequence[i : i + 3]
        if codon in start:
            # ATG를 발견하면 해당 위치부터 3bp씩 진행하며 Stop codon 탐색
            for j in range(i, len(rev_sequence) - 2, 3):
                curr_codon = rev_sequence[j : j + 3]
                if curr_codon in stop:
                    # Start부터 Stop 직전까지 슬라이싱 후 번역
                    orf = Seq(rev_sequence[i:j])
                    protein = str(orf.translate())
                    results.append(protein)
                    break  # 가장 먼저 나오는 Stop codon에서 해당 ORF 종결

    # 중복 제거
    results = list(set(results))
    print(results)
    print("Traslation Complete")
    return results

print("\n".join(find_orf(raw_list)))










