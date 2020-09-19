instr = input()

alpha = []
number = 0
for c in instr :
	if 'A' <= c <= 'Z' :
		alpha.append(c)
	elif '0' <= c <= '9' :
		number += int(c)
alpha.sort()
for c in alpha :
	print(c, end='')
print(number)
