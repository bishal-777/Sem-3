#WAP to enter two coordinates from user and print the distance between 

import math 

initial=list(map(int,input("Enter initial coordinate:").split()))
final=list(map(int,input("Enter final coordinate:").split()))

d=round(math.sqrt((final[0]-initial[0])**2+(final[1]-initial[1])**2),4)

print(f"Distance between two points:{d}")