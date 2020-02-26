
def consect(num, base): 
    a = fun(num, base) 
    if (check(a)): 
        print("Yes") 
    else: 
        print("No") 

def fun(num, base): 
    w = 1
    s = 0
    while (num != 0): 
        r = num % base 
        num = num//base 
        s = r * w + s 
        w = w*10
    return s 
def check(num):   
    fl = False
    while (num != 0): 
        r = num % 10
        num = num//10
        if (fl == True and r == 0): 
            return False
        if (r > 0): 
            fl = False
            continue
        fl = True
    return True
  
# Main code
num=int(input("Enter Any Number : "))
bas= int(input("Enter Base Number : "))
consect(num, bas) 
