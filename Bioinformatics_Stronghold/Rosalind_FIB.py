with open("data/rosalind_fib.txt", "r") as f:
    n, k = map(int, f.read().split())

def reproduce(n: int, k: int) -> int:
    if 0 < n <= 2:
        return 1
    elif n <= 0:
        return 0
    else:
        prev1, prev2 = 1, 1
        for i in range(3, n + 1):
            C = prev1 + k * prev2
            prev1, prev2 = C, prev1
        return prev1

print(reproduce(n, k))


# n = 5, k = 3
# (0, 1) - (1, 0) - (1, 3) - (4, 3) - (7, 12), 1, 1, 4, 7, 19