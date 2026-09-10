from scipy.stats import binom

with open("data/rosalind_lia.txt", "r") as f:
    raw = f.read()

# raw = """
# 2 1
# """

gen, num = map(int, raw.strip().split())
# print(gen, num)

# AaBb - AaBb 에서 AaBb 나올 확률은 0.25
n = 2**gen
p = 0.25

# P(X >=N) = 1 - P(X <= N-1)
samples = 1 - binom.cdf(num-1, n, p)

print(round(samples, 3))