import sys

input = sys.stdin.readline

n, c = map(int, input().rstrip().split())
routers = []
for i in range(n):
	routers.append(int(input()))

routers.sort()

# 라우터가 1개만 일때 ?
# 집의 개수는 무조건 2 개 이상

bot = 1
top = routers[-1] - routers[0]
result = top
while bot <= top:
	term = (top + bot) // 2
	count = 1
	cur = routers[0]
	for i in range(1, n):
		if cur + term <= routers[i]:
			count += 1
			cur = routers[i]
		if count > c:
			break
	if count >= c :
		bot = term + 1
		result = term
	else :
		top = term - 1

print(result)