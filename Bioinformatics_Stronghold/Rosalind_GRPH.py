with open("data/rosalind_grph.txt", "r") as f:
    raw = f.read()

# raw = """
# >Rosalind_0498
# AAATAAA
# >Rosalind_2391
# AAATTTT
# >Rosalind_2323
# TTTTCCC
# >Rosalind_0442
# AAATCCC
# >Rosalind_5013
# GGGTGGG
# """

data = raw.strip().splitlines()

def fasta_parse(lines: list[str]) -> dict[str, str]:
    fasta_dict = {}
    current = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            current = line[1:]
            fasta_dict[current] = ""
        else:
            fasta_dict[current] += line
    return fasta_dict

def overlap_graph(fasta_dict: dict[str, str], k: int) -> list[tuple[str, str]]:
    # Prefix를 키로, 해당 Prefix를 가진 ID 목록을 값으로 갖는 Hash Map 생성
    prefix_map = {}
    for seq_id, seq in fasta_dict.items():
        prefix = seq[:k]
        prefix_map.setdefault(prefix, []).append(seq_id)
    
    edges = []
    # 각 서열의 Suffix가 Prefix Map에 존재하는지 O(1)로 확인
    for u_id, u_seq in fasta_dict.items():
        suffix = u_seq[-k:]
        if suffix in prefix_map:
            for v_id in prefix_map[suffix]:
                # Self-loop 방지 (자기 자신으로 향하는 간선 제외)
                if u_id != v_id:
                    edges.append((u_id, v_id))
                    
    return edges

# 실행 및 출력
parsed_fasta = fasta_parse(raw.strip().splitlines())
results = overlap_graph(parsed_fasta, k=3)

for u, v in results:
    print(f"{u} {v}")


# 참조 테이블 만들어서 시간복잡도 줄이기
# 셋디폴트 체화하기
