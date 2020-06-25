7#print odd numbers within in a given range
start=int(input("enter the start of the range:"))
end=int(input("enter the end of the range:"))
for num in range(start,end+1):
	if num%2!=0:
		print(num,end=" ")