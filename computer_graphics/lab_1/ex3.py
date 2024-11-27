#WAP to print first n fibonacci series
num=int(input("Enter nth number:"))

a,b=0,1

print(f"{a}\t",end="")
print(f"{b}\t",end="")
for i in range(num-2):
    s=a+b
    print(f"{s}\t",end="")
    a,b=b,s
print("\n")