import time

#time at the start of execution
start = time.time()

#We will store the products in a set to avoid duplicates
products = set()

#Digits from 1-9 which will be checking later
to_be_checked = set('123456789')

#for single digit multiplicand
for i in range(9):
	for j in range(999,9999):
		s = str(i)+str(j)+str(i*j)
		if len(s) == 9 and set(s) == to_be_checked:
			products.add(i*j)
		elif len(s) > 9:break

#for double digit multiplicand
for i in range(9,99):
	for j in range(99,999):
		s = str(i)+str(j)+str(i*j)
		if len(s) == 9 and set(s) == to_be_checked:
			products.add(i*j)
		elif len(s)>9: break

#printing the result
print(sum(products))

#time at the end of execution
end = time.time()

#total time taken for execution
print(end - start)