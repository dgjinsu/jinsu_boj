import sys
n = int(sys.stdin.readline())
list1 = []
result = []
plus_minus = []
count = 1
compare = []
for i in range(n):
	num = int(sys.stdin.readline())
	compare.append(num)
	while count <= num:
		list1.append(count)
		plus_minus.append("+")
		count += 1
		result.append(list1.pop())
		plus_minus.append("-")

if compare == result:
	for i in plus_minus:
		print(i)
else :
	print("NO")
print("practice")

