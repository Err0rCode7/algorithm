def solution(n, money):

	dp = [set() for _ in range(100001)]
	value = [0] * (100001)
	money.sort()
	print(dp)
	for m in money:
		dp[m].add(str(m))
	
	for i in range(1, n + 1):
		print(i, m)
		for m in money:
			# print(i, m)
			if i >= m:
				print(dp[i-m])
				for dp_str in list(dp[i - m]):
					# print(dp_str)
					dp[i].add(dp_str + "+" + str(m))

	answer = len(dp[n])
	return answer

print(solution(5, [1,2,5]))