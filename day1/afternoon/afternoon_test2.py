products={
        "001": "PC",
        "002": "Notebook",
        "003": "Mouse",
}

product = ["Keyboard", "PC", "Notebook", "Mouse"]

shops = {
        "shop1": {3: 500, 0: 100},
        "shop2": {2: 30, 1: 20},
        "shop3": {1: 55, 3: 44},
        "shop4": {1: 50, 3: 60},
        "shop5": {3: 500, 0: 100},
}


f = 1
for keyMain, value in shops.items():
	for key, value in value.items():
		if f%2 != 0:
			valueIndex = key
			# print("{} has {} {} PCE and ".format(keyMain, product[valueIndex], value))
			string1 = "{} has {} {} PCE and ".format(keyMain, product[valueIndex], value)
		else:
			valueIndex = key
			# print("{} {} PCE".format(product[valueIndex], value))	
			string2 = "{} {} PCE".format(product[valueIndex], value)
		f = f + 1
	print("" + string1 + string2)

