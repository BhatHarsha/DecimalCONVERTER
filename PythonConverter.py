x=int(input("Decimal number: "))
b=x+3
a=[]
while(x>0):
	y=x%2;
	a.append(y)
	x=x//2
a.reverse()
print('Binary number: ')
for i in a:
	print(i,end=" ")
a=[]
while(b>0):
	z=b%2
	a.append(z)
	b=b//2
a.reverse()
print("Excess-3 number: ")
for i in a:
	print(i,end=" ")
