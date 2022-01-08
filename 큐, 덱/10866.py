from sys import stdin
from collections import deque

n = int(stdin.readline())
q = deque()
for i in range(n):
	word = stdin.readline().split()
	order = word[0]
	if order == "push_front":
		q.appendleft(word[1])
	if order == "push_back":
		q.append(word[1])
	if order == "pop_front":
		if q:
			print(q.popleft())
		else:
			print("-1")
	if order == "pop_back":
		if q:
			print(q.pop())
		else:
			print("-1")
	if order == "size":
		print(len(q))
	if order == "empty":
		if len(q) == 0:
			print("1")
		else:
			print("0")
	if order == "front":
		if q:
			print(q[0])
		else:
			print("-1")
	if order == "back":
		if q:
			print(q[-1])
		else:
			print("-1")


