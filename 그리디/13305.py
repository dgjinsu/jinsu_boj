import sys
n = int(sys.stdin.readline())

dis = list(map(int, sys.stdin.readline().split()))

price = list(map(int, sys.stdin.readline().split()))

min_price = price[0]
total = 0
for i in range(len(dis)):
	if price[i] < min_price:
		min_price = price[i]
	total += (min_price*dis[i])


print(total)