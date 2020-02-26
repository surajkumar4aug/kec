def float_bin(number, places = 3): 
	no, dec = str(number).split(".") 
	no = int(no) 
	dec = int (dec) 
	res = bin(no).lstrip("0b") + "."
	for x in range(places): 
		no, dec = str((deci(dec)) * 2).split(".") 
		dec = int(dec) 
		res += no 
	return res 
def deci(num): 
	while num > 1: 
		num /= 10
	return num 
num = input("Enter your floating point value number: \n")  
place = int(input("Enter the number,you want to print after decimal: \n")) 
print(float_bin(num,place)) 
