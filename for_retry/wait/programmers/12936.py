from math import factorial

def solution(n, k):
	people = [i for i in range(1, n + 1)]
	answer = []
	def get_tail(people_list, n, k):

		if n == 1:
			return people_list
		n_fact = factorial(n)
		prefix_count = n_fact // n
		prefix = k // prefix_count + 1
		rest = k % prefix_count
		if rest == 0 and prefix > 1 :
			prefix -= 1
		people = people_list[:prefix - 1] + people_list[prefix:]
		if rest == 0:
			return [people_list[prefix - 1]] + people[::-1]
		elif rest == 1:
			return [people_list[prefix - 1]] + people
		return [people_list[prefix - 1]] + get_tail(people, n - 1, rest)


	answer = get_tail(people, n, k)
	return answer

print(solution(3, 5))
print(solution(4, 8))