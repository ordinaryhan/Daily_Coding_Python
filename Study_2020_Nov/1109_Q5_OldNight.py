# 백준 1783 / 병든 나이트
# 병든 나이트가 여행을 하면서 방문하는 칸의 최대 수는?
# 움직임 패턴은 4가지
# 1. 2칸 위로, 1칸 오른쪽 (2, 1)
# 2. 1칸 위로, 2칸 오른쪽 (1, 2)
# 3. 1칸 아래로, 2칸 오른쪽 (-1, 2)
# 4. 2칸 아래로, 1칸 오른쪽 (-2, 1)

# 문제 좀 이상한 것 같은데...


"""
100 50

Answer : 48
"""


import sys


# 체스판의 세로길이(n), 가로길이(m)
n, m = map(int, sys.stdin.readline().rstrip().split())

# 움직일 수 없는 경우
if n <= 1:
    print(1)
# 위아래로 한 칸씩 움직여야 되는 경우
elif n == 2:
    print(min(4, m//2 + m%2))
# 이동횟수가 4보다 작은 경우
elif m <= 6:
    print(min(4, m))
# 위 경우에 해당하지 않는 경우
else:
    print(m - 2)







