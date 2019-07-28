# Part 2 of the Python Review lab.

def encode(x, y):
	if x not in range(500,1000) and y not in range(1,250):
			print("Invalid input: outside range")
	else: 
		return(x * y)

print(encode(300, 300))


def decode(coded_message):
	pass