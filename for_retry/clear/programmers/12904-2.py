def solution(s):

	answer = 1
	for i in range(1, len(s) - 1):
		s1, e1 = i - 1, i + 1
		s2, e2 = i, i + 1
		stop1 = False
		stop2 = False

		size1 = 3
		size2 = 2
		offset = 0
		while not stop1 or not stop2:
			if s1 - offset < 0 or e1 + offset >= len(s):
				stop1 = True
			if s2 - offset < 0 or e2 + offset >= len(s):
				stop2 = True
			if not stop1 and s[s1 - offset] != s[e1 + offset] :
				stop1 = True
			if not stop2 and s[s2 - offset] != s[e2 + offset] :
				stop2 = True
			
			if not stop1 :
				answer = max(size1, answer)
			if not stop2 :
				answer = max(size2, answer)
			size1 += 2
			size2 += 2
			offset += 1

	return answer

print(solution("abcdcba"))
print(solution("abacde"))