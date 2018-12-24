


positive_number = int(input("give me positive number for find length of longest binary gap :"))

if positive_number < 0:
	print("Only Positive !")
	exit()

print(len(max(format(positive_number,'b').strip("0").split("1"))))