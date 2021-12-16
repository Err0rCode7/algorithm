def solution(n):

	dp = [0 for _ in range(n + 1)]
	dp[0] = 1
	for j in range(1, n + 1):
		for step in [1, 2]:
			if j - step >= 0:
				dp[j] += dp[j - step]
		
	answer = dp[n] % 1234567
	return answer

print(solution(4))
print(solution(3))