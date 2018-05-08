# for i in range(1,10):
#     print("No {} squared is {} and cubed is {}".format(i,i**2,i**3))
#     print("hello")
#
# name = input("Please Enter your name");
# age = int(input("How old are you,{0}".format(name)))
# print(age)
#
# if age >= 18:
#     print("you are old engouh to vote")
#     print("Please put a X in box")
# else:
#     print("Please come back is {0} years".format(18-age))
#
# print("Please gues a number between 1 and 10:")
#
# guess = int(input())
#
# if guess < 5:
#     print("Please guss higher")
#     guess = int(input())
#     if guess ==5:
#         print("Well done, you gussed it")
#     else:
#         print("Sorry, you have not gussed correctly")
# elif guess > 5:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you gussed it")
#     else:
#         print("Sorry, you have not gussed correctly")
# else:
#     print("You got it first time")
#
#
#

# age = int(input("ENter age"))
# if age >=16 and age <= 60:
#     print("welcome")
# if not (age <18):
#     print("teen")

# num = 1,2,3,4,5,6,7,8
# for i in range(0, len(num)):
#     print(num[i])

array = "1,2,3,4,5,6,7,87,8"
cleanNum =''
for char in array:
    if char in '0123456789':
     cleanNum = cleanNum + char

newNumber = int(cleanNum)
print("The number is {0}".format(newNumber))

#skipping number

for i in range(0,50,5):
    print("i is {}".format(i))

#Nesting for loop

for i in range(0,10):
    for j in range (0,10):
        print("{1} times {0} is {2}".format(i,j,i*j))
    print("============Continue Example=====================")

shoppingList = ["milk","butter","pasta","eggs","rice","oil"]

for item in shoppingList:
    if item == 'eggs':
        continue
    print("buy "+item)

print("============Break Example================")
for item in shoppingList:
    if item == 'eggs':
        break
    print("buy "+item)

print("===========While loop============")
i=0
while i <10 :
    print("i is now {}".format(i))
    i +=1

available_exit = ["east","north","south","west"]
choosen_exit =""
while choosen_exit not in available_exit:
    choosen_exit= input("Please choose a direction:")
    if choosen_exit == "quit":
        print("Game Over")
        break;
else:
   print("are not you glad!")