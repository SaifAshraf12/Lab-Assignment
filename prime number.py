# Display that number entered by user is a prime number or not
number = int(input('Enter a number:'))
if number < 2:
    print(number, "is not a prime number")
elif number == 2:
    print(number, 'is a prime number')
else:
    for i in range(2,number):
        if number % i == 0:
            print(number, 'is not a prime number')
            break
    else:
            print(number, 'is a prime number')
            

# Display prime numbers between 1 to 100
for number in range (1,101):
    if number < 2:
        print(number, 'is not a prime number')
    elif number == 2:
        print(number, 'is a prime number')
    else:
        for i in range (2,number):
            if number % i == 0:
                print(number, 'is not a prime number')
                break
        else:
            print(number, 'is a prime nuber')


# Prime numbers between starting and ending values
start = int(input('Enter a starting number '))
end = int(input('enter an ending  number '))
for number in range (start,end+1):
    if number < 2:
        print(number, 'is not a prime number')
    elif number == 2:
        print(number, 'is a prime number')
    else:
        for i in range (2,number):
            if number % i == 0:
                print(number, 'is not a prime number')
                break
        else:
                print(number, 'is a prime number')
