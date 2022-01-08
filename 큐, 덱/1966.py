import sys
from collections import deque

t = int(sys.stdin.readline())
for i in range(t):
	n,m = map(int, sys.stdin.readline().split())
	queue = deque(list(map(int,sys.stdin.readline().split())))
	index = m
	count = 0
	while True:
		a = max(queue)
		if queue[0] != a:
			queue.rotate(-1)
			if index == 0:
				index = len(queue)-1
			else:
				index -= 1
		else:
			queue.popleft()
			if index == 0:
				count+=1
				break
			else :
				count+=1
				index -= 1
	print(count)

