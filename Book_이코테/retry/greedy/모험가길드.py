import sys

input = sys.stdin.readline
N = int(input())
group = list(map(int, input().rstrip().split()))

def solution_1():
	global input, N, group

	asc = sorted(group)
	count = 0
	cur = asc[0]
	cur_index = 0
	if cur <= N :
		count += 1
		for i in range(N):
			if i < cur_index + cur:
				continue
			elif i == cur:
				if asc[i] + i >= N:
					break
				cur_index = i
				cur = asc[i]
				count += 1
	print(count)

def solution_2():
	global input, N, group

	count, result = 0, 0
	group.sort()

	for i in group :
		count += 1
		if i <= count :
			result += 1
			count = 0
	print(result)

solution_2()
