2#to count the numbers even or odd
list1=[1,21,4,45,66,93,1,7]
evencount, oddcount=0,0
for num in list1:
	if num%2==0:
		evencount+=1
	else:
		oddcount+=1
print("even numbers in the list:",evencount)
print("odd numbers in the list:",oddcount)