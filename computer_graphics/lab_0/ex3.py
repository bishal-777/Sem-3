#WAP to print first n fibonacci series
num=int(input("Enter nth number:"))

a,b=0,1

print(a,end="")
print(b,end="")
for i in range(num-2):
    s=a+b
    print(s,end="")
    a,b=b,s
print("\n")