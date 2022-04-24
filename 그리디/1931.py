import sys

n = int(sys.stdin.readline())
list1 = []

for i in range(n):
	a, b = map(int, sys.stdin.readline().split())
	list2 = [a,b]	
	list1.append(list2)

list1.sort(key = lambda x : x[::-1])

end = list1[0][1]
index = 0
count = 1

for i in range(index+1, n):
	if list1[i][0] >= end:
		end = list1[i][1]
		index = i
		count += 1
print(count)

	

