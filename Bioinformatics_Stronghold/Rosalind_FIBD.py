# 6달 볼거고 3달이 수명이다, 성체 될 때까지가 1달,
# 0(수명 3개월차 - 사망) 0(수명 2개월차 - 성체) 0(수명1개월차 - 갓 성체) 1(아기) 로 시작, 6달 차에 4마리가 남아야 함.
# 1개월 차 0 0 0 1 = 1 
# 2개월 차 0 0 1 0 = 1
# 3개월 차 0 1 0 1 = 2
# 4개월 차 1 0 1 1 = 2
# 5개월 차 1 1 1 1 = 3
# 6개월 차 2 1 1 2 = 4


# 데이터 가져오기
with open("data/rosalind_fibd.txt") as f:
    raw = f.read()


# 임시 데이터
# raw = """
# 6 3
# """


# 데이터 전처리
raw = raw.strip().split()
months, lifespan = map(int, raw)
# print(months, lifespan)


# 나이 딕셔너리 설정 (0개월 1개월 2개월 3개월에 사망)
age_dict = {i: 0 for i in range(lifespan)}
# print(age_dict)

# 초기 설정
age_dict[0] = 1

for month in range(2, months + 1):
    # 1. 이번 달에 새끼를 낳을 수 있는 성체(Age 1 이상)의 총합 계산
    new_borns = sum(age_dict[age] for age in range(1, lifespan))

    for age in range(lifespan - 1, 0, -1):
        age_dict[age] = age_dict[age - 1]

    age_dict[0] = new_borns

print(sum(i for i in age_dict.values()))