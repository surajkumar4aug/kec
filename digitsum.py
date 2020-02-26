num=int(input("enter number"))
even=0
odd=0
while(num!=0):
    rem=int(num%10)
    if(rem%2==0):
        even=even+rem
    else:
        odd=odd+rem
    num=num/10    
diff=even-odd      
print("difference between even and odd digit "+str(diff))      