import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

t = []
max_t = 0
for i in range(n):
	t.append(int(input()))
	max_t = max(max_t, t[i])

t.sort()
e = max_t * m
s = 0
result = e

while s <= e:
	took_time = (s + e) // 2
	evaluation_total_count = 0
	for i in range(n):
		evaluation_time = t[i]

		count = took_time // evaluation_time
		evaluation_total_count += count
	
	if evaluation_total_count >= m:
		e = took_time - 1
		result = min(result, took_time)
	else :
		s = took_time + 1

print(result)