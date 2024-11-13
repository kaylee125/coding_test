from itertools import combinations

w=[int(input()) for _ in range(9) ]

for i in combinations(w,7):
    if sum(i)==100:
        for x in sorted(i):
            print(x)
        break


## combinations안쓰고 푸는 방법
