from collections import defaultdict

def solution(n, weak, dist):
	dic = defaultdict(list)
	dic[0].append(tuple(weak))
	dist.sort()
	level,maxlevel = 0,len(dist)
	while level!=maxlevel and dist and () not in dic[level]:
		d = dist.pop()
		temp = set()
		for weak in dic[level]:
			temp |= {tuple(j for j in weak if not (i<=j<=i+d or i<=j+n<=i+d)) for i in weak}
			print(temp)
		level +=1
		dic[level].extend(list(temp))
		print(dic)
	result = sorted(dic.keys())[-1]
	if () not in dic[result] : return -1
	return result

testcase = []
testcase.append((12, [1, 5, 6, 10], [1, 2, 3, 4]))
testcase.append((12, [1, 3, 4, 9, 10], [3, 5, 7]))
for a, b, c in testcase :
	print("answer: ", solution(a, b, c))
