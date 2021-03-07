# https://www.acmicpc.net/problem/5397

from sys import stdin
# import queue
for _ in range(int(stdin.readline())):
  testCase = stdin.readline().strip()
  output = []
  # temp = queue.Queue()
  temp = []
  for char in testCase :
    if char == "<":
      if len(output) :
        # temp.put(output.pop())
        temp.append(output.pop())
    elif char == ">":
      # if temp.qsize() != 0 :
      if len(temp) :
        output.append(temp.pop())
    elif char == "-":
      if len(output):
        output.pop()
    else :
      output.append(char)
  # while temp.qsize() != 0 :
  #   output.append(temp.get())
  while len(temp) :
    output.append(temp.pop())
  print(''.join(output))