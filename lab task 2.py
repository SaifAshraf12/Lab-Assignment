# a number is positive or negative or zero
number = int(input('Enter a number:'))
if number > 0:
    print('number is positive.')
elif number < 0:
    print('number is negative.')
else:
    print('number is zero.')

# to determine a leap year
year = int(input('Enter a year:'))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('year is a leap year.')
else:
    print('year is nat a leap year.')

# Make a simple calculator
num1 = int(input('Enter 1st number.'))
num2 = int(input('Enter 2nd number.'))
operator = input('Enter a operator (+,-,*./):')
if operator == '+':
	print('Result:', num1 + num2)
elif operator == '-':
	print('Result:', num1 - num2)
elif operator == '*':
	print('Result:', num1 * num2)
elif operator == '/':
	if num2 != 0:
		print('Result:', num1 / num2)
	else:
		print('Undeined. (Division by zero)')
else:
	print('Invalid Operator.')
