instr = input()

start = 0
cur = int(instr[0])
result_a = 0
result_b = 1
flag_a = True
flag_b = False
for i in range(1, len(instr)) :
	next = int(instr[i])
	if next != cur and flag_a:
		result_a += 1
		flag_a = False
		flag_b = True
	if next == cur and flag_b:
		result_b += 1
		flag_a = True
		flag_b = False
print(result_a if result_a < result_b else result_b)
