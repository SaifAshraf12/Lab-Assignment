# Write a program to show grade of student
marks = float(input('Enter your marks:'))
if marks < 50:
    print('Grade is F')
elif 51 <= marks <= 60:
    print('Grade is E')
elif 61 <= marks <= 70:
    print('Grade is D')
elif 71 <= marks <= 80:
    print('Grade is C')
elif 81 <= marks <= 90:
    print('Grade is B')
else:
    print('Grade is A')

# Write a program to show weather condition
temp = float(input('Enter temperature of today:'))
if temp < 0:
    print('FREEZING')
elif 0 <= temp <= 15:
    print('COLD')
elif 16 <= temp <= 30:
    print('WARM')
elif 31 <= temp <= 40:
    print('HOT')
else:
    print('VERY HOT')
    
