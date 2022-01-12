from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().rstrip().split()))
numbers.insert(0, 0)
m = int(input())
dp = defaultdict(lambda: defaultdict(list))

for i in range(m):
	l, r = map(int, input().rstrip().split())
	mid = (r + l) // 2
	even = (r + l) % 2
	nl, nr = 0, 0
	if dp[mid][even] :
		nl, nr = dp[mid][even]
	else :
		if even == 0: # 홀수
			nl = mid - 1
			nr = mid + 1
		else: # 짝수
			nl = mid
			nr = mid + 1

	def is_pelin(start, end):
		if l == r :
			return True
		while start >= l and end <= r:
			if numbers[start] == numbers[end]:
				start -= 1
				end += 1
			else :
				return False
		return True

	if is_pelin(nl, nr):
		# even, l, r,
		if len(dp[mid]) == 0 or len(dp[mid][even]) == 0:
			dp[mid][even] = [l, r]
		else:
			if dp[mid][even][0] > l and dp[mid][even][1] < r:
				dp[mid][even] = [l, r]
		print(1)
	else:
		print(0)