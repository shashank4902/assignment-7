8#count the number of digits in a number
def countdigit(n):
       if n==0:
       	return 0
       return 1+countdigit(n//10)
n=3456789
print("number of digits:%d"%(countdigit(n)))
