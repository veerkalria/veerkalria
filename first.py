print("please select the number-")
print("1 for veer\n2 for kavya\n3 for jiya")
a=int(input("enter number here-\n"))


print("please select the number")
print("1 for exercise chart\n2 for diet chart")
b=int(input("enter number here-\n"))


print("please select the number")
print("1 for add info. in chart\n2 for read info. from chart")
c=int(input("enter number here-\n"))

def getdate(x):
    import datetime
    return datetime.datetime.now()

if a==1 and b==1 and c==1:
 with open("veerex.txt", "a") as f:
     temp=getdate(":")
     f.write(str(temp))
     f.write("=")
     f.write(input("enter which exercise you have done-\n"))
     f.write("\n")

if a==1 and b==1 and c==2:
    f=open("veerex.txt","r")
    for lines in f:
      print(lines)

if a==1 and b==2 and c==1:
 with open("veerfood.txt", "a") as f:
     temp=getdate(":")
     f.write(str(temp))
     f.write("=")
     f.write(input("enter which food you have taken-\n"))
     f.write("\n")

if a==1 and b==2 and c==2:
    f=open("veerfood.txt","r")
    for lines in f:
      print(lines)

if a==2 and b==1 and c==1:
 with open("kavyaex.txt", "a") as f:
     temp=getdate(":")
     f.write(str(temp))
     f.write("=")
     f.write(input("enter which exercise you have done-\n"))
     f.write("\n")

if a==2 and b==1 and c==2:
    f=open("kavyaex.txt","r")
    for lines in f:
     print(lines)

if a==2 and b==2 and c==1:
 with open("kavyafood.txt", "a") as f:
     temp=getdate(":")
     f.write(str(temp))
     f.write("=")
     f.write(input("enter which food you have taken-\n"))
     f.write("\n")

if a==2 and b==2 and c==2:
    f=open("kavyafood.txt","r")
    for lines in f:
      print(lines)

if a==3 and b==1 and c==1:
 with open("jiyaex.txt", "a") as f:
     temp=getdate(":")
     f.write(str(temp))
     f.write("=")
     f.write(input("enter which exercise you have done-\n"))
     f.write("\n")

if a==3 and b==1 and c==2:
    f=open("jiyaex.txt","r")
    for lines in f:
      print(lines)

if a==3 and b==2 and c==1:
 with open("jiyafood.txt", "a") as f:
     temp=getdate(":")
     f.write(str(temp))
     f.write("=")
     f.write(input("enter which food you have taken-\n"))
     f.write("\n")

if a==3 and b==2 and c==2:
    f=open("jiyafood.txt","r")
    for lines in f:
      print(lines)


