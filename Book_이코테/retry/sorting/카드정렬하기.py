import heapq
import sys

input = sys.stdin.readline

N = int(input().rstrip())

card = []

for i in range(N):
	card.append(int(input().rstrip()))

heapq.heapify(card)

_sum = 0
len_card = len(card)
while len_card >= 2:
	result = heapq.heappop(card) + heapq.heappop(card)
	_sum += result
	len_card -= 1
	heapq.heappush(card, result)
print(_sum)
