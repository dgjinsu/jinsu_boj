import sys
sentence = []
while True:
	a = sys.stdin.readline().rstrip()
	if a == ".":
		break
	sentence.append(a)
stack = []
for i in range(len(sentence)):
	stack.clear()
	a = sentence[i]
	for j in range(len(a)):
		if a[j] == "(":
			stack.append("(")
		if a[j] == "[":
			stack.append("[")
		if a[j] == "]":
			if len(stack) == 0:
				print("no")
				stack.append("아무거나")
				break
			if stack[-1] != "[":
				print("no")
				stack.append("아무거나")
				break
			else :
				stack.pop()
		if a[j] == ")":
			if len(stack) == 0:
				print("no")
				stack.append("아무거나")
				break
			if stack[-1] != "(":
				print("no")
				stack.append("아무거나")
				break
			else :
				stack.pop()
	if len(stack) == 0:
		print("yes")
	elif not "아무거나" in stack:
		print("no")

