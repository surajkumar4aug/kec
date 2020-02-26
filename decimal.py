def deci(num): 
	while num > 1: 
		num /= 10
	return num 

def octfloat(number, places): 
	no, dec = str(number).split(".")  
	no = int(no) 
	dec = int (dec) 
	res = oct(no).lstrip("0o") + "."
	for x in range(places): 
		no, dec = str((deci(dec)) * 8).split(".") 
		dec = int(dec) 
		res += no 
	return res 

num = input("Enter your floating point value : \n") 
dec = int(input("Enter the number of decimal places of the result : \n")) 

print(octfloat(num,dec)) 
