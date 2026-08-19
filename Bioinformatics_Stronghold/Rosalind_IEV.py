with open("data/rosalind_iev.txt", "r") as f:
    nums = list(map(int, f.read().strip().split()))

# raw = "1 0 0 1 0 1"

# nums = list(map(int, raw.strip().split()))
# print(nums)

def Offspring(n: list[int]) -> float:
    Dominant = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
    dot_product = sum(2 * x * y for x, y in zip(n, Dominant))
    return dot_product

print(f"{Offspring(nums):.1f}")

# zip(리스트, 리스트) 하면 리스트 요소들끼리 튜플로 묶어서 싹 반환
