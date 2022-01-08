from sys import stdin
from collections import deque
n,m = map(int, stdin.readline().split())
q = deque()
for i in range(1,n+1):
	q.append(i)
a = list(map(int, stdin.readline().split()))
count = 0
while a:
	index = q.index(a[0]) #몇번 인덱스에 있는지
	if index == 0:
		q.popleft()
		a.pop(0)
		continue
	if index+1 > (len(q)+1)//2:
		q.rotate(1)
		count += 1
	else :
		q.rotate(-1)
		count += 1
print(count)