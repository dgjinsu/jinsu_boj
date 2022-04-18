import sys

def find(list1, target):
	low = 0
	high = len(list1) - 1
	while low <= high:
		mid = (low + high) // 2
		if list1[mid] == target:
			return True
		elif list1[mid] > target:
			high = mid - 1
		else :
			low = mid + 1

	return False

n = int(sys.stdin.readline())
list1 = list(map(int, sys.stdin.readline().split()))
list1.sort()


m = int(sys.stdin.readline())
list2 = list(map(int, sys.stdin.readline().split()))


for i in range(m):
	target = list2[i]
	if find(list1, target):
		print(1)
	else :
		print(0)

	

