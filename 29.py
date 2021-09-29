# Please write a function that calculates liquid volume in a sphere using the following formula. The radius r  is always 10, so consider making it a default parameter.
# You can then test your solution by passing 2 for h and you should get the expected output.

from math import pi
def vol(r,h):
	v = ((4*pi*(r**3)/3)-(((pi*(h**2))*((3*r)-h))/3))
	return(v)

print(vol(10,2))