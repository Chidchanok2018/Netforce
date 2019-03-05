products = {
	"000": "Keyboard",
	"001": "PC",
	"002": "Notebook",
	"003": "Mouse",
}

shops = {
	"shop1": {"003": 500, "000": 100},
	"shop2": {"002": 30, "001": 20},
	"shop3": {55: "001", 44: "003"},
	"shop4": {50: "001", 60: "003"},
	"shop5": {"002": 800, "001": 300},
}

def printout(data):
		loopin_round = 1
		for key_main, value in data.items():
			for subkey, subvalue in value.items():		
				if loopin_round%2 != 0:
					if isinstance(subkey, str):
						string1 = "{} has {} {} PCE and ".format(key_main, products[subkey], value[subkey])
					else:
						string1 = "{} has {} {} PCE and ".format(key_main, products[subvalue], value[subkey])
					loopin_round = loopin_round + 1
				else:
					if isinstance(subkey, str):
						string2 = "{} {} PCE".format(products[subkey], value[subkey])
					else:
						string2 = "{} {} PCE".format(products[subvalue], value[subkey])
			loopin_round = 1
			print("" + string1 + string2)

printout(shops)		
