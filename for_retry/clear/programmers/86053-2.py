def solution(a, b, g, s, w, t):

	start = 0
	end = int(1e9 * 2 * 1e5 * 2)
	m = len(g)
	result = end
	while start <= end:
		time = (start + end) // 2
		gold = 0
		silver = 0
		total = 0
		for i in range(m):
			size = time // (t[i] * 2)
			if time % (t[i] * 2) >= t[i]:
				size += 1
			
			gold += min(size *  w[i], g[i])
			silver += min(size * w[i], s[i])
			total += min(size * w[i], g[i] + s[i])
		
		if gold >= a and silver >= b and total >= a + b:
			result = min(result, time)
			end = time - 1
		else:
			start = time + 1
	return result

print(solution(10, 10, [100], [100], [7], [10]))
# print(solution(90, 500, [70,70,0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))