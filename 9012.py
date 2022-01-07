import sys
k = int(sys.stdin.readline())
stack = []
for i in range(k):
	s = sys.stdin.readline()
	count = 0
	for j in range(len(s)):
		if s[j] == "(":
			stack.append("k")
		if s[j] == ")":
			if len(stack) == 0:
				stack.append("k")
				break
			else :
				stack.pop()
	if len(stack) == 0:
		print("YES")
	else :
		print("NO")
	stack.clear()
	
		
