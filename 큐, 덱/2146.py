import sys
from collections import deque

n = int(sys.stdin.readline())
card = deque()
for i in range(1,n+1):
	card.append(i)

while True:
	if len(card)>1:
		card.popleft()
	if len(card) == 1:
		break
	card.append(card.popleft())
print(card[0])
	
