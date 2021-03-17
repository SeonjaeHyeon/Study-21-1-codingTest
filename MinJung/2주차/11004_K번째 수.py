import sys
N, K= sys.stdin.readline().split()
A=[]*int(N)
A =sys.stdin.readline().split()
A=list(map(int,A))
print(A)
A.sort()
print(A)
print(A[int(K)-1])