
s = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]

def solution(s) :
	length = len(s)
	result = length
	for offset in range(1, length):
		sum = 0
		flag = 1
		#outstr = ""
		for i in range(0, length, offset):
			if i + 2*offset <= length:
				if s[i:i+offset] == s[i+offset:i+2*offset]:
					flag += 1
				elif flag > 1 and s[i:i+offset] != s[i+offset:i+2*offset]:
					#outstr += str(flag) + s[i:i+offset]
					sum += offset + len(str(flag))
					flag = 1
				else :
					#outstr += s[i:i+offset]
					sum += offset
			else :
				if flag > 1:
					#outstr += str(flag) + s[i:i+offset]
					sum += offset + len(str(flag))
					flag = 1
				else :
					#outstr += s[i:]
					sum += len(s[i:])
					break
		if sum != 0:
			#print(outstr)
			result = min(result, sum)
	return (result)

for string in s :
	print(solution(string))
