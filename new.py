# 1 count the number of digit
'''n=int(input("Enter a number:"))
count=0
while n>0:
    n=n//10
    count=count+1
print("The number of digit in a number are:",count)'''

# 2 print odd number and count the odd number
'''num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
c=0
for i in range(num1,num2):
    if i%2!=0:
        print(i)
        c=c+1
print("number of odd numbers are:",c) '''       
#3 reverse the number and check pallindrome or not
'''num = int(input("enter a number: "))
temp = num
rev = 0 
while temp>0:
	rev = (rev * 10) + (temp % 10)
	temp = temp // 10
if num == rev:
	print("number is palindrome")
else:
	print("number is not palindrome")'''
'''#4 next digit
num = int(input("enter a number: "))
temp = num 
rev = 0
 r=0
while temp>0:
	rev = (rev * 10) + (temp % 10)+1
	temp = temp // 10
while rev>0:
    r = (r * 10) + (rev % 10)
    rev=rev//10
    #print("next digit is:",r)
print(r)
# 5sum of digit'''
'''n=int(input("enter a number:"))
res=0
while n>0:
    r=n%10
    res=res+r
    n=int(n/10)
print("Sum of digit is:",res)'''
#6 display the number from 1 to 500 except the multiple of 100.
'''for i in range(1,501):
    if(i%100!=0):   
         print(i,end=' ')'''
#7 max digit
'''num= int(input("Enter a Number :"))
m = 0
while num > 0:
    c = num % 10
    if m < c:
        m = c
    num = int(num / 10)
print("\nLargest digit is :", m)'''
#8 max number
'''num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("The largest number is", largest)'''

#9 multipy each digit and giv final result
'''n=int(input("enter a number:"))
res=1
while n>0:
    r=n%10
    res=(res*r)
    n=int(n/10)
print("Multipy of given number is:",res)'''

#10 multipy 3 numbers
'''num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
mul=num1*num2*num3
print("multipy of 3 numbers are:",mul)'''

#11 check the given no.is within range or not
'''n=int(input("Enter number for checking "))
if n in range(1,50):
    print("number is in the range")
else:
    print("number is not in given range")

#12

#13 Prime or not'''
'''l=50
u=200
for num in range(l,u+1):
    if num>1:
        for i in range(2,num):
            if(num%2)==0:
                break
        else:
                print(num,end=' ')'''

#14 perfect Square
'''number = int(input("Enter the Number"))

root = math.sqrt(number)
if int(root + 0.5) ** 2 == number:
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")'''
    


# 15 Factorial of a number using recursion
'''def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
num = int(input("Enter a number:"))
# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))'''

# 16 Python program to display the Fibonacci sequence
'''def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = 10
# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))'''
# 17 Python Program to Find the GCD of Two Numbers Using Recursion
'''def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
GCD=gcd(a,b)
print("GCD is: ")
print(GCD)'''

string=raw_input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)
