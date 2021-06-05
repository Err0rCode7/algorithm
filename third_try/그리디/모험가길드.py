# test case

# Q:
# 5
# 2 3 1 2 2

# A:

import sys

input = sys.stdin.readline

n = int(input())
player = list(map(int, input().rstrip().split()))

player.sort()

# 풀이 1
# 불필요한 리스트를 만들어서 풀었으며 불필요한 초기화 문이 있다.
# 요구사항을 해석한 걸로 구현되어있지 않다.

result = 0
target = -1
targetList = []

for p in player :
	if target == -1 :
		target = p
	if target < p:
		target = p;

	targetList.append(p)

	if len(targetList) >= target :
		result += 1
		target = -1
		targetList = []

# 풀이 2
# 리스트를 사용하지 않았으며 간결히 요구사항에 맞게 구현되었다.
# 좀더 요구사항대로 구현하는 방식을 유도해야되겠다.

# result = 0
# count = 0
# for p in player :
# 	count += 1
# 	if count >= p :
# 		count = 0
# 		result += 1

print(result)


