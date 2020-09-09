import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

numbers.sort(reverse=True)

# 1

def solution_1(N, M, K, numbers) :
	i = 0
	j = 0
	result = 0
	num_len = len(numbers)
	while i < M :

		if j < K :
			result += numbers[0]
			j += 1
		elif num_len > 1 and j >= K :
			j = 0
			result += numbers[1]
		i += 1

	return result

def solution_2(N, M, K, numbers) :

	iteration_num = (numbers[0] * K + numbers[1])
	max_num = numbers[0]

	result = int(M / (K + 1)) * iteration_num
	result += M % (K + 1) * max_num

	return result

print(solution_1(N, M, K, numbers))
print(solution_2(N, M, K, numbers))
