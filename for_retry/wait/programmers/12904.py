def solution(s):
	answer = 1
	if len(s) == 0:
		return 0
	for i in range(len(s) - 1):
		lo, hi = i, i
		lo2, hi2 = i, i + 1
		length1 = 0
		if 0 <= lo < len(s) and 0 <= hi < len(s):
			if s[lo] == s[hi]:
				length1 = 1
		length2 = 0
		if 0 <= lo2 < len(s) and 0 <= hi2 < len(s):
			if s[lo2] == s[hi2]:
				length2 = 2
		one = False
		two = False
		lo -= 1
		hi += 1
		lo2 -= 1
		hi2 += 1
		while True :
			if not (0 <= lo < len(s) and 0 <= hi < len(s)):
				one = True
			if not (0 <= lo2 < len(s) and 0 <= hi2 < len(s)):
				two = True
			if one and two:
				break
			if not one and s[lo] == s[hi]:
				length1 += 2
			else :
				one = True
			if not two and s[lo2] == s[hi2]:
				length2 += 2
			else :
				two = True
			lo -= 1
			hi += 1
			lo2 -= 1
			hi2 += 1
		answer = max(answer, length1, length2)

	return answer

print(solution("abcdcba")) # 7
print(solution("abacde")) # 3
print(solution("abacde")) # 3
print(solution("afffaaaaaaa")) # 7