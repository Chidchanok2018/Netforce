nbrs = (1, 2, (3, 4, 5, (6, 7), 8), 9, 10)

def check(data):
	if isinstance(data, int):
		print(data)
	else:
		for i in data:
			if isinstance(i, int):
				print(i)
			else:
				check(i)

check(nbrs)
