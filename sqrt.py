def sqrt(z,eps=0.000001):
	k = 1
	x0 = z/2
	while abs(x0**2-z)>eps:
		k = k+1
		x0 = x0 - (x0**2-z)/(2*x0)
	return x0, k



def test(x):
	y,k = sqrt(x) 
	print("Input {0} -- output: {1} -- output squared: {2} -- iterations: {3}".format(x, y, y**2, k))

test(0)
test(1)
test(2)
test(4)
test(9)
test(81)
test(10000)
test(40)
test(555)
test(77777)


def sqrtB(z,eps=0.000001):
	x0 = z/2
	while abs(x0**2-z)>eps:
		x0 = (x0**2+z)/(2*x0)
	return x0

def test2(x):
	y1,_ = sqrt(x)
	y2 = sqrtB(x)
	print(y1,y2)#,y1**2,y2**2)


print("----------------------")
test2(0)
test2(1)
test2(2)
test2(4)
test2(9)
test2(81)
test2(10000)
test2(40)
test2(555)
test2(77777)
