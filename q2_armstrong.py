n=int(input("ENTER A NUMBER"))
q=n
t=str(n)
pow=len(t)
sum=0
while n>0:
	dig=n%10
	sum=sum+(dig**pow)
	n=n//10
if sum==q:
	print("ARMSTRONG")
else:
	print("NOT ARMSTRONG")
