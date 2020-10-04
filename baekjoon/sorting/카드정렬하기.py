import sys, heapq

input = sys.stdin.readline

n = int(input())
cards = []
for i in range(n) :
	heapq.heappush(cards, int(input()))

total = 0

if n == 1:
	print(0)
else :
	while len(cards) > 1 :
		a = heapq.heappop(cards)
		b = heapq.heappop(cards)
		total += (a + b)
		heapq.heappush(cards, a + b)
	print(total)
