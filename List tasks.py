# activity # 1
# Accept two lists from user and display their join
mylist1 = []
print('enter objects of first list...')
for i in range (5):
    val = input('enter a value:')
    n = int(val)
    mylist1.append(n)
mylist2 = []
print('enter objectives of second list...')
for i in range (5):
    val = input("enter a value")
    n = int(val)
    mylist2.append(n)
mylist3 = mylist1 + mylist2
print(mylist3)
mylist3.sort()
print(mylist3)


# activity # 2
# find smallest and largest element of list
mylist = []
for i in range (5):
    val = input('Enter a value')
    n = int(val)
    mylist.append(n)
print(mylist)
print('maximum value is ', max(mylist))
print('minimum value of list is ', min(mylist))

# activity # 3
# find smallest and largest element of list
mylist = []
for i in range (5):
    val = input('Enter a value')
    n = int(val)
    mylist.append(n)
print(mylist)
print('maximum value is ', max(mylist))
print('minimum value of list is ', min(mylist))
print(mylist.index(max(mylist)))
print(mylist.index(min(mylist)))

# activity # 4
# find smallest and largest element of list
mylist = []
for i in range (5):
    val = input('Enter a value')
    n = int(val)
    mylist.append(n)
print(mylist)
mylist.sort()
print(mylist)
mylist.reverse()
print(mylist)

