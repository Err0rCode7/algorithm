import sys

# 문자열 압축문제
# aabbcc를 2a2b2c로 abcabcabcad를 3abcad와 같이 나타낼 수 있다.
# 숫자를 포함한 최적의 압축 방법을 찾아서 문자열의 길이를 반환하는 문제.

# 문자를 1개 단위부터 문자열의 총 길이 단위까지 압축을 시도해볼 수가 있다.
# 모두 똑같은 블록으로 잘라야 나가야 하기 때문에
# 자르는 블록의 단위를 n이라고 한다면 n개 씩 자르면서 시도를 해볼 수가 있다.
# 1부터 길이 - 1 까지 시도를 해본 값의 길이 들을 리스트에 넣고 최소 값을 답으로 반환하여 해결한다.

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
