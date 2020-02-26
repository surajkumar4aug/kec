
def countoccur(x, i): 
	count = 0 
	while (x): 
		if (x % 10 == i): 
			count += 1; 
		x = int(x / 10) 

	return count
def maxoccur(x):  
	if (x < 0): 
		x = -x 
	result = 0 
	max_count=1 
	for i in range(10): 
		count = countoccur(x, i)
		if (count >= max_count): 
			max_count = count 
			result = i
	print("max occur number is " +str(result)) 
	print("number of count is "+str(max_count))
num=int(input("enter number"))
maxoccur(num)
