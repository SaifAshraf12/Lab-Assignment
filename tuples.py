# tuples in python
academic_tuple = ('name', 'father nane', 'reg number', 'CNIC number', 'CGOA')
print(academic_tuple)

# single item tuple
registration_number = ('SP24-BBA-099',)
single = (2,)
print(single)  
print(registration_number)

# tuple of integers
integers = (2, 3, 5, 6)
print(integers)

# tuple of strings
fruit_tuple = ('apple', 'bnana', 'cherry')
print(fruit_tuple)

# tuple of mix data types
mix_tuple = (1, 'apple', 4.56, True)
print(mix_tuple)

# accessing elements of tuples
integers = (1, 23, 45, 7)
print(integers[0])
fruits = ('banana', 'apple', 'cherry')
print(fruits[1])

# negative indexing
print(fruits[-1])
print(integers[-3])

# imutability of tuples
fruits = ('banana', 'apple', 'cherry',)
# print(fruits[1]) = 'orange'
# tuple elements cannot be modifyed

# tuple operations
# concatenation
tuple1 = (1, 2, 3, 4,)
tuple2 = (5, 6, 7, 8,)
combined_tuple = tuple1 + tuple2
print(combined_tuple)

# repetition
tuple1 = ('banana',)
repeated_tuple1 = tuple1 * 3
print(repeated_tuple1)

# tuple slicing
numbers = (1, 2, 3, 4, 5, 6, 7, 8)
print(numbers[1:4])
print(numbers[:6])
print(numbers[2:])
print(numbers[0:7])

# count returns that how many times an item repeats in tuple
fruits = ('apple', 'banana', 'cherry', 'cherry', 'cherry', 'orange')
print(fruits.count('cherry'))

# index of an item of tuple
fruits = ('apple', 'banana', 'cherry', 'cherry', 'cherry', 'orange')
print(fruits.index('banana'))

# break and continue statement in for loop
# exercise 1
for i in range(10):
    if i == 5:
        break
    print(i)

# exercise 2
for i in range(10):
    if i == 4:
        continue
    print(i)

# exercise 3
for i in range(10):
    if i == 7:
        break
    if i%2 == 0:
        continue
    print(i)

# break and continue statement in for loop
# exercise 4
count = 0
while (count <= 10):
    count = count+1
    if count == 5:
        continue
    if count == 8:
        break
    print(count)




