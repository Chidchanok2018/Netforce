string = "987654321"
space = " "
i = 1
j = 0
k = 0
while i < 6:
	space = " " * i
	print("{}{}".format(space, string[j:]))
	j = k + 2
	i = i + 1
	if k%2 != 0:
		k = k + 1
	else:
		k = k + 2	
