
def solution(a, b, g, s, w, t):
	
	end = int(1e9 * 1e5 * 4 - 1e5)
	start = 0
	mid = (start + end) // 2
	time = int(1e9 * 1e5 * 4 - 1e5)
	while start <= end:
		mid = (start + end) // 2
		gold = 0
		silver = 0
		total = 0
		# gold
		# min_take_time
		for i in range(len(g)):
			take_time = t[i] * 2
			count = mid // take_time
			if mid % take_time >= t[i]:
				count += 1
			move = w[i] * count
			gold += min(move, g[i])
			silver += min(move, s[i])
			total += min(g[i] + s[i], move)
			
		# print(gold, silver, mid)
		if gold >= a and silver >= b and total >= a + b:
			time = min(time, mid)
			end = mid - 1
		else :
			start = mid + 1

	return time



print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))