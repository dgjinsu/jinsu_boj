import sys

n, m = map(int, sys.stdin.readline().split())

list1 = [[0] * (n+1)]

for i in range(n):
	a = [0] + [int(x) for x in sys.stdin.readline().split()]
	list1.append(a)

for i in range(1, n+1):
	for j in range(1, n):
		list1[i][j+1] += list1[i][j]

for i in range(1, n+1):
	for j in range(1, n):
		list1[j+1][i] += list1[j][i]

for i in range(m):
	a,b,c,d = map(int, sys.stdin.readline().split())
	answer = list1[c][d] - list1[c][b-1] - list1[a-1][d] + list1[a-1][b-1]
	print(answer)