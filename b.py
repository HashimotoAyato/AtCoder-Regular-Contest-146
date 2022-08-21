N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = [bin(a)[2:].zfill(30) for a in A]

B.sort()