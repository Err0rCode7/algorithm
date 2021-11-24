import sys, heapq
input = sys.stdin.readline
N = int(input())
cards = []
for i in range(N):
	card = int(input())
	heapq.heappush(cards, card)

i = len(cards)
_sum = 0
while i > 1:
	result = heapq.heappop(cards) + heapq.heappop(cards)
	_sum += result
	i -= 1
	heapq.heappush(cards, result)
print(_sum)