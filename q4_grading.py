s1=int(input("Enter marks"))
s2=int(input("Enter marks"))
s3=int(input("Enter marks"))
s4=int(input("Enter marks"))
s5=int(input("Enter marks"))
total=s1+s2+s3+s4+s5
avg=total/500
per=total/5
print("Total=",total)
print("Average=",avg)
print("Percentage=",per)
print("Grade=",end='')
if per>=90:
    print('A')
elif per>=75:
    print('B')
elif per>=60:
    print('C')
else:
    print('D')
    
income=int(input("Enter Cumulative family income to check for Scholarships"))
if per>80 and income<300000:
    print('Eligible for Scholarship')
else:
    print('Not Eligible for Scholarship')
