n, m = map(int, input().rstrip().split())

ball = list(map(int, input().rstrip().split()))

weight = [0] * (m + 1)
result = 0

for b in ball :
	weight[b] += 1

for i in range(1, m + 1) :
	n -= weight[i]
	result += weight[i] * n
print(result)
