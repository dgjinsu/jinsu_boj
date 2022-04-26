import sys

n, k = map(int, sys.stdin.readline().split())

list1 = list(map(int, sys.stdin.readline().split()))
start = 0
end = k-1
sum = 0
for i in range(k):
	sum = sum + list1[i]

list2 = [sum]

for i in range(n-k):
	end += 1
	sum = sum + list1[end] - list1[start]
	start += 1
	list2.append(sum)
	
print(max(list2))
	