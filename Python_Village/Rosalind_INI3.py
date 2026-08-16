with open("data/rosalind_ini3.txt", "r") as f:
    raw_data = f.readlines()

str_data = raw_data[0].strip()

int_data = raw_data[1].strip()
nums = int_data.split()
a, b, c, d = map(int,nums)

Chunk1 = str_data[a:b+1]
Chunk2 = str_data[c:d+1]

print(f"{Chunk1} {Chunk2}")

# with 구문은 파일을 열고 닫는 것을 자동으로 처리해주는 구문, 에러가 나도 close 보장
# with (context) as variable:

# open 구문은 파일과 파이썬을 연결해줌
# open("파일이름", "r")
# r: read(읽기모드), w: write(새 파일 생성), a: append(기존에 이어붙이기), b: binary(바이너리모드)

# .read() : 파일 전체를 읽어옴 하나의 덩어리 string으로 반환
# .strip() : 문자열 양쪽 공백 제거(양쪽만)
# .split() : 문자열을 공백 기준으로 나눠서 리스트로 반환

# map() : 리스트의 각 요소를 지정한 함수로 처리해주는 함수
# map(함수, 리스트)