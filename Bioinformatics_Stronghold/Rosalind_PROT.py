# from Bio.Data import CodonTable

# ==============================================================================
# 1. 코돈 테이블 불러오기 (Standard Table: NCBI Table ID 1)
# ==============================================================================

# ID로 불러오기 (가장 흔히 사용)
# standard_table = CodonTable.unambiguous_dna_by_id[1]

# 이름으로 불러오기 (동일한 객체 반환)
# standard_table = CodonTable.unambiguous_dna_by_name["Standard"]

# RNA 코돈 테이블이 필요한 경우
# rna_table = CodonTable.unambiguous_rna_by_id[1]

# 전체 코돈 표 매핑 상태 및 정보 시각화 출력
# print("=== Standard Codon Table Summary ===")
# print(standard_table)


# ==============================================================================
# 2. Forward Lookup (코돈 -> 아미노산)
# ==============================================================================

# 코돈(DNA 3연구서열)을 key로 하여 대응하는 Single-letter 아미노산 반환
# 주의: Stop Codon(TAA, TAG, TGA)은 forward_table에 존재하지 않음 (KeyError 발생)
# try:
#     atg_aa = standard_table.forward_table["ATG"]
#     print(f"\nATG codes for: {atg_aa}")  # M (Methionine)

#     tgg_aa = standard_table.forward_table["TGG"]
#     print(f"TGG codes for: {tgg_aa}")  # W (Tryptophan)
# except KeyError as e:
#     print(f"Stop codon cannot be looked up in forward_table: {e}")


# ==============================================================================
# 3. Start / Stop Codon 확인
# ==============================================================================

# 시작 코돈 리스트 (Standard에서는 ['TTG', 'CTG', 'ATG'])
# print(f"\nStart Codons: {standard_table.start_codons}")

# 정지 코돈 리스트 (Standard에서는 ['TAA', 'TAG', 'TGA'])
# print(f"Stop Codons: {standard_table.stop_codons}")

# 특정 코돈이 Stop Codon인지 검증하는 패턴
# target_codon = "TGA"
# is_stop = target_codon in standard_table.stop_codons
# print(f"Is {target_codon} a Stop Codon? -> {is_stop}")


# ==============================================================================
# 4. Reverse Lookup (아미노산 -> 해당 코돈 전체 목록)
# ==============================================================================

# forward_table(Dict)을 순회하여 특정 아미노산을 암호화하는 Degenerate Codon 추출
# target_amino_acid = "L"  # Leucine
# leucine_codons = [
#     codon
#     for codon, aa in standard_table.forward_table.items()
#     if aa == target_amino_acid
# ]

# print(f"\nCodons for Leucine ({target_amino_acid}): {leucine_codons}")
# Output: ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG']


# ==============================================================================
# 5. 다른 생물체/기관의 코돈 테이블 다루기 (예: Mitochondrial, Bacterial)
# ==============================================================================

# Vertebrate Mitochondrial (NCBI Table ID 2)
# 인간 미토콘드리아는 AGA/AGG가 Stop Codon, AUA가 Met, UGA가 Trp으로 코딩됨
# mito_table = CodonTable.unambiguous_dna_by_id[2]

# print(f"\nVertebrate Mito Stop Codons: {mito_table.stop_codons}")
# Output: ['TAA', 'TAG', 'AGA', 'AGG']

# print(f"Mito UGA codes for: {mito_table.forward_table['UGA']}")
# Output: W (Tryptophan) - 표준 테이블에서는 Stop Codon이지만 미토콘드리아에선 Trp


# ==============================================================================
# 6. 간단한 Custom Translation / Mutation Effect Check 함수 작성 예시
# ==============================================================================


# def check_mutation_type(
#     wt_codon: str, mut_codon: str, table_id: int = 1
# ) -> str:
#     """두 코돈을 비교하여 Synonymous / Nonsynonymous / Nonsense 변이 판별"""
#     table = CodonTable.unambiguous_dna_by_id[table_id]

#     wt_is_stop = wt_codon in table.stop_codons
#     mut_is_stop = mut_codon in table.stop_codons

#     if wt_is_stop or mut_is_stop:
#         return "Nonsense/Stop-related Mutation"

#     wt_aa = table.forward_table.get(wt_codon)
#     mut_aa = table.forward_table.get(mut_codon)

#     if wt_aa == mut_aa:
#         return f"Synonymous ({wt_aa} -> {mut_aa})"
#     else:
#         return f"Nonsynonymous ({wt_aa} -> {mut_aa})"


# # 테스트
# print(
#     f"\nMutation (TCT -> TCC): {check_mutation_type('TCT', 'TCC')}"
# )  # Synonymous (S -> S)
# print(
#     f"Mutation (TCT -> ACT): {check_mutation_type('TCT', 'ACT')}"
# )  # Nonsynonymous (S -> T)

from Bio.Data import CodonTable

with open("data/rosalind_prot.txt", "r") as f:
    seq = f.read().strip()

# seq = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

def Translater(n: str) -> str:
    rna_table = CodonTable.unambiguous_rna_by_id[1]
    amino = []
    for i in range(0, len(n), 3):
        codon = n[i:i+3]
        if len(codon) < 3 or codon in rna_table.stop_codons:
            break
        amino.append(rna_table.forward_table[codon])
    return "".join(amino)

print(Translater(seq))
