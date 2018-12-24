

length_of_fibonacci = int(input("length of fibonacci:"))
n1 = 0
n2 = 1
for x in range(length_of_fibonacci):
	print(n1,end=",") 
	tt = n1 + n2
	n1 = n2
	n2 = tt
