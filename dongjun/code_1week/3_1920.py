import sys
N = sys.stdin.readline()
arr = set(sys.stdin.readline().split())
M = sys.stdin.readline()
search = set(sys.stdin.readline().split())
for i in search:
    if i in arr:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")
