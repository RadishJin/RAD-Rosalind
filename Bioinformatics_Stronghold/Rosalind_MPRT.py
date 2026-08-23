import re   # 정밀한 문자열 모티프를 검색, 추출, 교체 하게 해주는 툴
import requests  # 웹과의 통신 담당

with open("data/rosalind_mprt.txt", "r") as f:
    raw = f.read()

# raw = """
# A2Z669
# B5ZC00
# P07204_TRBM_HUMAN
# P20840_SAG1_YEAST
# """

raw_ids = raw.strip().split("\n")
motif = r"(?=N[^P][ST][^P])"

def find_motif(raw_ids : list[str], motif : str) -> dict[str, list[int]]:


        # 단백질 코드 정리
    clean_ids = {i.split("_")[0] : i.strip() for i in raw_ids if i}
    print("Completed Code Parsing...")

    query =" OR ".join([f"accession:{k}" for k in clean_ids.keys()])
    print("Completed Query Making...")

        # UniProt으로부터 데이터 수신
    url = "https://rest.uniprot.org/uniprotkb/stream"
    print("Completed URL...")

    params = {"query" : query, "format" : "fasta"}

    data = requests.get(
        url,
        params = params,
        headers = {"User-Agent" : "Mozilla/5.0"}
        )
    if data.status_code == 200:
        print("Successfully Retrieved")
    else:
        print("Not Retrieved from WEB")

    data = data.text
    print(data)

        # 수신한 데이터 정리
    sequence = {}
    current_id = None
    for i in data.splitlines():
        i = i.strip()
        if not i:
            continue
        if i.startswith(">"):
            current_id = i.split("|")[1]
            sequence[current_id] = ""
        else:
            sequence[current_id] += i
    print("Sequence Data Loaded...")

        # 모티브 위치 찾기
    prot_dict = {}
    for rid in raw_ids:
        acc = rid.split("_")[0]
        seq = sequence.get(acc, "")
        num_list = [match.start() + 1 for match in re.finditer(motif, seq)]
        if num_list:
            prot_dict[clean_ids[acc]] = num_list

    return prot_dict


    # 최종 출력
for a, b in find_motif(raw_ids, motif).items():
    print(a)
    print(*b)





# requests.get(
#     "https://rest.uniprot.org/uniprotkb/stream", # 1. url (필수, positional): 데이터를 요청할 API의 기본 주소(문자열)
#     params={"query": "accession:A2Z669", "format": "fasta"}, # 2. params (선택, keyword): URL 뒤에 '?key=value'로 붙는 검색 조건/옵션 사전(dict)
#     headers={"User-Agent": "Mozilla/5.0"}, # 3. headers (선택, keyword): 요청 메타데이터(클라이언트 정보, 인증 토큰 등) 사전(dict)
#     timeout=10, # 4. timeout (선택, keyword): 서버 응답을 기다릴 최대 시간(초 단위 float/int)
#     cookies={"session_id": "xyz123"}, # 5. cookies (선택, keyword): 서버에 전달할 쿠키 정보 사전(dict)
#     auth=("user", "pass"), # 6. auth (선택, keyword): HTTP 기본 인증에 사용되는 (아이디, 비밀번호) 튜플(tuple)
#     verify=True, # 7. verify (선택, keyword): SSL/TLS 인증서 검증 여부 (bool 또는 CA 묶음 경로)
#     allow_redirects=True # 8. allow_redirects (선택, keyword): HTTP 리다이렉트 자동 추적 여부(bool)
# )










