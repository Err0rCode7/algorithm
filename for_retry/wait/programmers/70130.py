
def solution(a):
	answer = 0

	n = len(a)
	
	for i in range(n - 1):
		if a[i] == a[i + 1]:
			continue

	return answer

print(solution([0]))
print(solution([5,2,3,3,5,3]	))
print(solution([0,3,3,0,7,2,0,2,2,0]	))