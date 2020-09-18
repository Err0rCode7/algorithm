n = int(input())
coins = list(map(int, input().rstrip().split()))
coins.sort()

target = 1
for coin in coins :
	if coin > target :
		break
	target += coin
print(target)
