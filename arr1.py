import array as arr
a=arr.array('i')
no=int(input("enter limitation\b"))
for i in range(no):
      num=int(input())
      a.append(num)
print("3rd to 7th Element Of The Array")      
for i in range(2,7):      
      print(a[i],end=",")  
print("\b")      