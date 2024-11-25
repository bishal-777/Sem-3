'''WAP to take input coordinate and angle and
rotate bout origin by angle'''
import math

def rotate(x,y,theta):
    theta=math.radians(theta)#sin and cos functions doesn't take in degree,so converting to radian
    x_temp=round(x*math.cos(theta)-y*math.sin(theta),4)
    y_temp=round(x*math.sin(theta)+y*math.cos(theta),4)
    return(x_temp,y_temp)


x1,y1=map(int,input("Enter the coordinates:").split())
theta=int(input("Enter angle:"))

x2,y2=rotate(x1,y1,theta)

print(f"New coordinates:({x2},{y2})")