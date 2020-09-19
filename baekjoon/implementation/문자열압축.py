
def solution(s) :

	block_size = 1
	min = len(s)
	answer = s
	while block_size < len(s) :
		result = ""
		count = 1
		for i in range(0, len(s), block_size) :
			if s[i:i+block_size] == s[i+block_size:i+2*block_size] :
				count += 1
			elif s[i:i+block_size] != s[i+block_size:i+2*block_size] :
				if count == 1 :
					result += s[i:i+block_size]
				else :
					result += str(count) + s[i:i+block_size]
				count = 1
		print(result)
		if min > len(result) and len(result) > 0:
			answer = result
			min = len(result)
		block_size += 1
	return(len(answer))
instr = input()
solution(instr)
