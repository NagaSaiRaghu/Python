def add(n):
    s=0
    while n>0:
        s=s+n
        n=n-1
    return s

while True:
 try:
  x=int(input("enter a number?\n"))
 except  ValueError:
  print("you didnt enter a valid number")
 if x<0:
    print("enter a positive number")
 elif x>0:
    print("the sum of natural numbers from ", x , "is")
    print(add(x))
 again=input("do u want to do again?(yes or no)\n")
 if again == "yes":
     continue
 elif again =="no":
     print("bye")
     break
 else:
    print("enter a valid argument")
    break
