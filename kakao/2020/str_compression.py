import sys

def solution(s):
	string = s
	result = []
	for j in range(1, len(string) + 1) :
		temp = ""
		count = 1
		i = 0
		while i < len(string) :
			str_temp = string[i:i+j]
			if str_temp == string[i + j : i + j + j] :
				count += 1
			else :
				if count > 1 :
					temp = temp + str(count) + str_temp
					count = 1
				else : temp = temp + str_temp
			i += j
		result.append(len(temp))
	answer = min(result)
	return answer

string = sys.stdin.readline().rstrip().strip('\"')
print(solution(string))
