print("A is must be array and please use , for seperate")
myarray = input("A:").split(",")
print("K is must be integer")
myinteger = int(input("K:"))

new_array = myarray.copy()
for x in range(len(myarray)):
	new_array[(x + myinteger) % len(myarray)] = myarray[x]

print(new_array)