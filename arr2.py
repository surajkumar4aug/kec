import array as arr
a=arr.array('i')
sum=0
avg=0
no=int(input("enter Number Of Subject:"))
for i in range(no):
      print("Subject "+ str(i+1)+" Mark:",end="") 
      num=int(input())
      a.append(num)
      sum=sum+a[i]
for i in range(no):
      print("Subject "+ str(i+1)+" Mark:"+str(a[i]))       
avg=sum/5                 
print("Total Mark: ",sum)
print("Average Mark: ",avg)  