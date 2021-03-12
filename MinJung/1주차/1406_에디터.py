from collections import deque
import sys 

lL=deque([])
fL = deque(list(sys.stdin.readline()))
M = int(sys.stdin.readline())
for i in range(M):
    newS = sys.stdin.readline()
    if "P" in newS:
        newS = newS.split()
        fL.append(newS[1])
    elif newS == "L" and list(fL)!=[]:
        lL.appendleft(fL.pop())
    elif newS=="D" and list(lL)!=[]:
        fL.append(lL.popleft())
    elif newS=="B" and list(fL)!=[]:
        fL.pop()
for i in list(fL+lL):
    print(i, end='')

