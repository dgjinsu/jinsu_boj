import sys

n, k = map(int, sys.stdin.readline().split())

list1 = []

for i in range(n):
	a = int(sys.stdin.readline())
	list1.append(a)

count = 0
for i in range(1,n+1):
	if k >= list1[-i]:
		count = count + (k // list1[-i])
		k = k % list1[-i]
	if k == 0:
		break

print(count)