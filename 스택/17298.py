import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []
stack.append(0)
for i in range(1, n):
	while len(stack)>0 and a[stack[-1]] < a[i]:
		answer[stack.pop()] = a[i]
	stack.append(i)

for i in answer:
	print(i,end= " ")