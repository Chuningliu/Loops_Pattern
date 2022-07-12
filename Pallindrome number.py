# PALLINDROME NUMBER:


# i=int(input("Enter the number:"))
# x=i
# rev=0
# while i>0:
#     rev=(rev*10)+i%10
#     i=i//10
# if x==rev:
#     print ("is a pallindrome number")
# else:
#     print("is not a pallindrome number")


# FOR LOOPS

x=int(input("Enter the string:"))
w=" "
for i in x:
    w=i+w
if (x==w):
    print("yes")
else:
    print("No")