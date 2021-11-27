a, b = input(), input()

dp = []
for y in range(len(b) + 1):
	line = []
	for x in range(len(a) + 1):
		if x == 0 or y == 0:
			line.append(1e9)
		else:
			line.append(0)
	dp.append(line)

dp[0][0] = 0
for y in range(1, len(b) + 1):
	for x in range(1, len(a) + 1):
		dp[y][x] = min(dp[y - 1][x - 1], dp[y - 1][x], dp[y][x - 1])
		if a[x - 1] != b[y - 1] :
			dp[y][x] += 1

print(dp[len(b)][len(a)])