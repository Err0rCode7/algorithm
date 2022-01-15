n = int(input())

dp = [0 for _ in range(int(1e6 + 1))]
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 3
dp[5] = 5

P = int(1e6)

def pibo(n):
	print(n)
	quota = n // 2
	remainder = n % 2
	count = (n - quota)
	if n <= 5 :
		return dp[n]
	if n > P:
		if remainder == 1:
			return ((pibo(quota) * count) + pibo(quota - 1) * (count - 1)) % P
		else:
			return (pibo(quota) * 3 + pibo(quota - remainder) * 2) % P
	else:
		dp[n] = pibo(quota + 1) * 3 + pibo(quota) * 2
	return dp[n] % P

print(pibo(n))