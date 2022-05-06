import sys

n, m = map(int, sys.stdin.readline().split())

list1 = list(map(int, sys.stdin.readline().split()))
list2 = []

sum = 0
for i in range(len(list1)):
	sum += list1[i]
	list2.append(sum)

for i in range(m):
	a, b = map(int, sys.stdin.readline().split())
	if a == 1:
		print(list2[b-1])
	else:
		print(list2[b-1] - list2[a-2])


