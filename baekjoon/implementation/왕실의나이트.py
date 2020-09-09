in_str = input()

x = in_str[0]
y = int(in_str[1])

def solution_1(x, y) :

	result = 0
	if x < 'c' or x > 'f' :
		if y <= 1 or y >= 8 :
			result += 1
		else :
			result += 2
	else :
		if y <= 1 or y >= 8 :
			result += 2
		else :
			result += 4
	if y < 3 or y > 6 :
		if x <= 'a' or x >= 'h' :
			result += 1
		else :
			result += 2
	else :
		if x <= 'a' or x >= 'h' :
			result += 2
		else :
			result += 4
	return (result)

def solution_2(x, y) :

	result = 0
	x = int(ord(x)) - int(ord('a')) + 1

	steps = [
		(-2, 1), (-2, -1), (2, 1), (2, -1),
		(1, -2), (-1, -2), (1, 2), (-1, 2)
	]
	for step in steps :
		next_x = x + step[0]
		next_y = y + step[1]
		if next_x <= 8 and next_x >= 1 and next_y >= 1 and next_y <= 8 :
			result += 1
	return (result)

print(solution_2(x, y))
