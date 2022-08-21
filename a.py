N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
A = A[:3]

from itertools import permutations
ans = 0
for p in permutations(A):
    s = str(p[0])+str(p[1])+str(p[2])
    ans = max(int(s), ans)

print(ans)