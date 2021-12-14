def solution(s):

	answer = []
	strings = s
	for s in strings:
		l_l, l_r = 0, 2
		r_l, r_r = len(s) - 3, len(s) -1
		while True:
			# print(l_l, l_r, r_l, r_r)
			# find 110 from right
			find_right = False
			while r_l >= 0:
				if s[r_l:r_r+1] == "110":
					find_right = True
					break
				r_l -= 1
				r_r -= 1
			# find insert index from left
			find_left = False
			while find_right and l_r < r_l:
				if s[l_l:l_r + 1] == "111":
					find_left = True
					break
				l_l += 1
				l_r += 1
			# 두가지 l_l이 r_l 앞인경우와 r_r 뒤인경우
			size = len(s) - r_r - 1
			back = False
			front = False
			if not find_left and size <= 2:
				if size == 1 and s[r_r + 1: r_r + 1 + size] == "0":
					l_l = r_r + 1
					l_r = l_l + size - 1
					find_left = True
					back = True
				elif size == 2 and s[r_r + 1: r_r + 1 + size] != "11":
					l_l = r_r + 1
					l_r = l_l + size - 1
					find_left = True
					back = True

			if not find_left and r_l <= 2:
				# 뒤에서 넣을 공간을 못찾고 앞에가 2개 이상 남았을 때
				size = r_l
				if (size == 2 and s[:r_l] == "11") or size == 1 and s[:r_l] == "1":
					# 앞으로 땡겨오기 가능
					find_left = True
					front = True
					l_l = 0
					l_r = size - 1
			if find_left and find_right:
				# print(l_l, l_r, r_l, r_r)
				# insert index is l_l
				result = ""
				if back :
					result += s[:r_l]
					result += s[l_l : l_r + 1]
					result += s[r_l:r_r + 1]
					s = result
					break
				elif front:
					result += s[r_l:r_r + 1]
					result += s[l_l:l_r + 1]
					result += s[r_r + 1:]
					s = result
					break
				else :
					result += s[:l_l]
					result += s[r_l:r_r + 1]
					result += s[l_l:r_l]
					result += s[r_r + 1:]
					l_l += 3
					l_r += 3
					r_l += 2
					r_r += 2
					s = result
			else:
				break
		answer.append(s)
	return answer

print(solution(["1110","100111100","0111111010"]	))
# print(solution(["1110"]	))