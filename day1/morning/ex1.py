i = 1
x = "*"
y = " "
xNumber = 6
while i < 5:
	print("{}{}{}{}{}{}{}".format(y, i, i, x * xNumber, i, i))
	xNumber = xNumber - 2
	i = i + 1
	y = " " * i

