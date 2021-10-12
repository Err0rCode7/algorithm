'''
문자열 압축

문자열안에 문자열을 블록 단위로 잘라서 압축할 때 가장 압축률이 좋게 블록을 만들어서 압축한 결과를 출력
'''

def plusCount(result, pre, count) :
	if count > 1 :
		result += str(count) + pre
	else :
		result += pre
	return result

def solution(s) :
	
	compressionResult = len(s)

	for size in range(1, len(s)):
		result = str()
		pre = str()
		count = 1
		for i in range(0, len(s), size) :
			if i + size > len(s) :
				break
			cur = s[i: i + size]
			if len(pre) == 0 :
				pre = cur
				continue
			if pre == cur :
				count += 1
			else :
				result = plusCount(result, pre, count)
				count = 1
				pre = cur
		if len(pre) != 0 :
			result = plusCount(result, pre, count)
		compressionResult = min(compressionResult, len(result) + len(s) % size)

	return compressionResult



questions = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]

# print(solution("aabbaccc"))

for question in questions :
	print(solution(question))