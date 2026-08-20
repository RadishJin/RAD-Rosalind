# with open("data/rosalind_fibd.txt", "r") as f:
#     months, lifespan = map(int, f.read().strip().split())

months, lifespan = 1,1

def mortal_fibonacci(months: int, lifespan: int) -> int:
    """
    계산: months개월 후 살아있는 토끼 쌍의 개수
    
    규칙: 각 쌍은 성숙하는 데 1개월, 그 후 lifespan개월을 산다
    따라서 나이 2 이상 lifespan+1 이하인 동안 번식
    
    alive[i] = alive[i-1] + alive[i-2] - alive[i-lifespan]
    """
    if months <= 0 or lifespan <= 0:
        return 0
    if months == 1:
        return 1
    
    # alive[i] = i개월에 살아있는 쌍의 개수
    alive = [0] * (months + 2)
    alive[1] = 1
    alive[2] = 1 if months >= 1 else 0
    
    # 점화식: alive[i] = alive[i-1] + alive[i-2] - alive[i-lifespan]
    for i in range(3, months + 2):
        alive[i] = alive[i-1] + alive[i-2]
        # i-lifespan 시점의 쌍이 i시점에서 죽음
        if i - lifespan > 0:
            alive[i] -= alive[i - lifespan]
    
    return alive[months + 1]

print(mortal_fibonacci(months, lifespan))