i = [1, 2, 3, 4, 5]
j = [5, 4, 3, 2, 1]
line = 0
line2 = 6
star = "*"
while line < 5:
	iPrint = ''.join(map(str, i[line:]))
	jPrint = ''.join(map(str, j[line:line2]))
	print("{}{}{}".format(jPrint, star, iPrint))
	line = line+1
	line2 = line2-1
	star = star*line
 
