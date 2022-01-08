import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque()
for i in range(k,n+k):
	if i <= n:
		queue.append(i)
	else:
		queue.append(i-n)
result = []
for i in range(n):
	result.append(queue.popleft())
	if len(queue) == 0:
		break
	for j in range(k-1):
		queue.append(queue.popleft())
print("<",end="")
for i in range(len(result)-1):
	print("{0}{1}".format(result[i],","),end=" ")
print(result[-1],end="")
print(">")
