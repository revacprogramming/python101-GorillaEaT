hrs = input("Enter Hours:")
h = float(hrs)
rate=input("enter rate:")
r=float(rate)
if(h<=40):
	x=h*r
if(h>40.0):
	x=40*r+((h-40)*(r*1.5))
print(x)
