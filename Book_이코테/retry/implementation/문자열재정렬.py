import sys, heapq

input = sys.stdin.readline

instr = input().rstrip()

def solution_1() :
	global instr
	# maybe O(N + 2logK) => O(N)

	alpha = []
	sum = 0
	for c in instr :
		if 'A' <= c <= 'Z' :
			heapq.heappush(alpha, c)
		else :
			sum += int(c)

	outstr = ""
	while alpha :
		outstr += heapq.heappop(alpha)

	print(outstr + str(sum))

def solution_2():
	global instr

	alpha = []
	sum = 0
	for c in instr :
		if 'A' <= c <= 'Z' :
			alpha.append(c)
		else :
			sum += int(c)

	alpha.sort()
	print("".join(alpha) + str(sum))

#solution_1()
solution_2()
