import sys

input = sys.stdin.readline

N = int(input().rstrip())
coins = list(map(int, input().rstrip().split()))

def solution_test():
	global coins

	coins.sort(reverse=True)
	i = 1

	while True :
		result = 0
		for c in coins :
			if i < c :
				continue
			if result == i :
				break
			if result + c <= i :
				result += c
		if i != result:
			break
		i += 1
	print(i)

def solution():
	global coins

	coins.sort()
	target = 1
	for i in coins :
		if target < i:
			break
		target += i
	print(target)

solution()
