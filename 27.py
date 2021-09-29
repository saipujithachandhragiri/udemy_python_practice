# Create a function that calculates acceleration given initial velocity v1, final velocity v2, start time t1, and end time t2. The formula for acceleration is: a=v2-v2/t2-t1
# To test your solution, call the function by inputting values 0, 10, 0, 20 for v1, v2, t1, and t2, respectively, and you should get the expected output.

def acc(v1,v2,t1,t2):
	a=(v2-v1)/(t2-t1)
	return(a)

print(acc(0,10,0,20))
