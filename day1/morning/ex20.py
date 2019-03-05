i = 1
j = str(i)
while i < 6:
	iPrint = j * i
	starPrint = "*" * i
	print("{}{}{}".format(iPrint, starPrint, iPrint))
	i = i + 1
	j = str(i)
