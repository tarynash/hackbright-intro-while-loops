#i = 1
#while i < 21:
#	print i,
#	i += 1

#i = 1
#while i < 21:
#	if i == 13:
#		print "hello",
#	else:
#		print i,
#	i += 1

#i = 0
#while i < 110:
#	print i,
#	i += 10

#i = 0
#while(i<len(range(0,10))):
#	if(i%2 == 0):
#		i += 1
#	else:
#		print i,
#		i += 1

#i = 10
#while i >= 0:
#	print i
#	i -= 1

#i = 10
#while(i>=0):
#	if i == 0:
#		print "Blastoff!"
#		i -= 1
#	else:
#		print i
#		i -= 1

#fruits = ["apples", "oranges", "bananas"]
#i = 0
#while i < len(fruits):
#	print fruits[i],
#	i += 1

#def sum_nums(num):
#	sum = 0
#	i = 0
#	while i < num:
#		sum = i + sum
#		i += 1
#	print sum
#sum_nums(-3)

def sum_nums2(num):
	sum = 0
	i = 0
	if (num<0):
		while(i>num):
			sum += i
			i -= 1
	else:
		while(i<=num):
			sum += i
			i += 1
	return sum
print sum_nums2(-3)

