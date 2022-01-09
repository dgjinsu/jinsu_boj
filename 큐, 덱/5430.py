from sys import stdin
from collections import deque
t = int(stdin.readline())
for i in range(t):
	count = 0
	go = 0
	s = stdin.readline().rstrip()  #명령어
	length = int(stdin.readline())  #숫자 개수
	q = deque(stdin.readline().rstrip()[1:-1].split(","))
	if length == 0:
		q = deque()
	for j in range(len(s)):
		if s[j] == "R":
			count += 1
		if s[j] == "D":
			if not q:
				print("error")
				go = 1
				break
			else:
				if count % 2 == 0:
					q.popleft()
				else :
					q.pop()

	if go == 0:
		if count % 2 == 1:
			q.reverse()
			print("["+",".join(q)+"]")

		else:
			print("["+",".join(q)+"]")


