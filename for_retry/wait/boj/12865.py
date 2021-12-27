import sys, heapq

input = sys.stdin.readline

n, k = map(int, input().strip().split())
dp = [0 for _ in range(int(1e5) + 1)]
stuffs = []
dp[0] = 0
dp[k] = 0

for i in range(n):
	w, v = map(int, input().strip().split())
	heapq.heappush(stuffs, (-(v / w),  w, v))

for p, w, v in stuffs:
	dp[w] = max(dp[w], v)

while stuffs:
	priority, w, v = heapq.heappop(stuffs)

	if w >= k:
		continue

	dp[k] = max(v + dp [k - w], dp[k])

print(dp[k])

"""TC

4 6
2 2
3 6
3 6
5 12

3 10
11 1
1 10
2 10

"""

