# take fictorial of number entered by user
number = int(input('Enter a number:'))
fictorial = 1
if number == 0:
    print('1')
elif number == 1:
    print('1')
else:
    for i in range(1,number+1):
        fictorial = fictorial*i
        print(fictorial)


# OR
number = int(input('Enter a number:'))
fictorial = 1
if number == 0:
    print('1')
elif number == 1:
    print('1')
else:
    for i in range(1,number+1):
        fictorial = fictorial*i
print(fictorial)
