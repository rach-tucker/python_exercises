#Exercise 1: Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop

num = 0
cube = 0
while cube < 1000:
    cube = pow(num,3)
    num = num + 1
    print(cube)

#Exercise 2: Get first prime numbers up to 100

for num in range(1,101):
    for i in range(2,num):
        if num % i !=0:
            print(num)
            break
        else:
            break

print("")
for num in range(2,101):
    if all((num % i != 0) for i in range(2,num)):
        print(num)



#Exercise 3: Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors


age= '50'
age_as_an_int = int(age)

if age_as_an_int < 18: 
    print('kids')
elif age_as_an_int == 18:
    print('adults')
elif age_as_an_int <= 65:
    print ('adults')
else:
    print('seniors')



  


