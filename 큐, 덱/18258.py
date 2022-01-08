import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()
for i in range(n):
	word = sys.stdin.readline().split()
	order = word[0]
	if order == "push":
		queue.append(word[1])
	if order == "pop":
		if len(queue) > 0:
			print(queue.popleft())
		else:
			print("-1")
	if order == "size":
		print(len(queue))
	if order == "empty":
		if len(queue) == 0:
			print("1")
		else:
			print("0")
	if order == "front":
		if len(queue) > 0:
			print(queue[0])
		else:
			print("-1")
	if order == "back":
		if len(queue) > 0:
			print(queue[-1])
		else:
			print("-1")
			