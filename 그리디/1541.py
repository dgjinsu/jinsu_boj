import sys

n = sys.stdin.readline().strip().split('-')
answer = []
for i in range(len(n)):
	sum = []
	sum = list(map(int, n[i].split('+')))
	a = 0
	for i in range(len(sum)):
		a += sum[i]
	answer.append(a)
last = answer[0]
for i in range(1, len(answer)):
	last = last - answer[i]
print(last)

