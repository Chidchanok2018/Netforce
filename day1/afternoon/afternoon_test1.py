nbrs =  (1,2,(3,4,5,(6,7),8),9,10)

for i in nbrs:
	if isinstance(i, int):
		print(i)
	else:
		for j in i:
			if isinstance(j, int):
				print(j)
			else:
				for k in j:
					print(k)

