# 코돈테이블 가져오기
from Bio.Data import CodonTable
# 전사, 번역기 가져오기
from Bio.Seq import Seq 

# raw 데이터 가져오기
with open("data/rosalind_splc.txt", "r") as f:
    raw = f.read()


# raw = """
# >Rosalind_10
# ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
# >Rosalind_12
# ATCGGTCGAA
# >Rosalind_15
# ATCGGTCGAGCGTGT
# """


def splice_and_translator(raw:list) -> str:
    # Parsing

    # 줄별 리스트로 바꾸기
    raw_list = raw.splitlines()
    current_id = ""
    seq_dict = {}
    for line in raw_list:

        # 공백이면
        if not line:
            # 뛰어넘기
            continue

        # 해당 줄이 > 로 시작한다면
        if line.startswith(">"):
            # > 제외한 나머지 뒷부분을 seq_dict에 Key로 저장
            current_id = line[1:]
            seq_dict[current_id] = ""
        # 서열이 적힌 줄이라면
        else:
            # 현재 key에 계속 이어붙이기
            seq_dict[current_id] += line
    print(seq_dict)
    print("Data Successfully Parsed")


    # 서열 길이대로 딕셔너리 솔팅 (오류 방지를 위해 긴 인트론부터 제거하고싶음)
    seq_dict = dict(sorted(seq_dict.items(), key= lambda x : len(x[1]), reverse = True)) # 튜플변환, 길이변환용 일회용함수, 큰 -> 작은
    print(seq_dict)
    print("Data Successfully Sorted")


    # Coding Strand만 따로 가져오고, 인트론 리스트 만들기
    introns = []
    coding_strand = None
    for i in seq_dict.values():

        if len(i) >= len(max(seq_dict.values(), key = len)) :
            coding_strand = i
        else:
            introns.append(i)
    print(coding_strand)
    print(introns)
    print("Data Ready to Splice")

    # Splicing
    spliced = coding_strand
    for i in introns:
        if i in spliced:
            spliced = spliced.replace(i, "")

    print(spliced)
    print("Successfully Spliced" if len(coding_strand) - len(spliced) == len("".join(introns)) else "Fail")

    # Translation
    prot_seq = Seq(spliced).translate(to_stop = True)
    
    return prot_seq

print(splice_and_translator(raw))


