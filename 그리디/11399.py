import sys

n = int(sys.stdin.readline())

list1 = list(map(int, sys.stdin.readline().split()))

list1.sort()
list2 = []
sum = 0
for i in range(n):
	sum = sum + list1[i]
	list2.append(sum)

answer = 0
for i in range(n):
	answer += list2[i]

print(answer)