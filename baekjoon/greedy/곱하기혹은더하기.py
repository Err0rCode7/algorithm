instr = input()

result = 0
for c in instr :
	c = int(c)
	if c <= 1 or result <= 1:
		result += c
	elif c > 1 and result > 1 :
		result *= c

print(result)
