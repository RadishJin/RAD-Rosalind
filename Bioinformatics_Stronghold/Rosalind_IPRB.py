import math

def MFL(k: int, m: int, n: int):
    t = k + m + n
    if t < 2:
        return 0.0
    else:
        F1 = (
            math.comb(m, 2) * 0.25
            + math.comb(n, 2) * 1.0
            + math.comb(m, 1) * math.comb(n, 1) * 0.5
        ) / math.comb(t, 2)
        return 1.0 - F1
    
with open("data/rosalind_iprb.txt", "r") as f:
    DNAseq = f.read().split()

k, m, n = map(int, DNAseq)

print(MFL(k, m, n))


# import math: 조합(Combination) 계산을 위한 수학 라이브러리 활용
# math.comb(n, k): 조합(Combination, nCk) 기반의 표본 공간 구축

# Complementary Probability (여사건): P(Dominant) = 1 - P(Recessive)
#      * 열성(aa) 자손이 나오는 단일 조건에 집중하여 상태 공간(State Space) 축소

# Weighting (가중치 적용): 부모 유전자형 조합별 aa 자손 형성 비율 반영
#      * Aa x Aa (0.25) / aa x aa (1.0) / Aa x aa (0.5)

# Exception Handling: 개체 수 부족(t < 2) 시 0.0 반환 처리 (Edge Case)

# Implicit Type Casting: 1.0, 0.25 등 실수(float) 명시를 통한 연산 의도 명확화

