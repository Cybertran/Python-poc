#list Example

# ipAddress = input("Enter an IpAddress:")
# print(ipAddress.count("."))

char_list = ["a","b","c","d"]
char_list.append("e")
for i in char_list:
    print("alphabets = {}".format(i))

print(char_list)

print("===============Array SOrting ========")
arr = [2,3,5,-1]
arr.sort()
print(arr)
arraySorted = sorted(arr)

if arr == arraySorted:
    print("list equals")
else:
    print("list not equals")

print("=============List ==============")

list1 = []
list2 = list()
print("List1: {}".format(list1))
print("List 2 {}".format(list2))

if list1 == list2:
    print("list are equals")

print(list("list are equals"))

even =  [2,4,6,8]
another_even = even
print(another_even is even)
another_even.sort(reverse=True)
print(even)

odd = [1,3,5,7]
masterList = [even, odd]
print(masterList)
for number_set in masterList:
    print(number_set)
    for val in number_set:
        print(val)

print("==============iterator===========")
stirng = "12345678"

myIter = iter(stirng)
print(next(myIter))

for char in stirng:
    print(char)
print("--------------another for -----------")
for char in iter(stirng):
    print(char)

days = ["mon","tue","wed","thus","sat","sun"]
dayIter = iter(days)
for i in range(0,len(days)):
    next_Item = next(dayIter)
    print(next_Item)

#example list with range
listRange = list(range(10))
print(listRange)

print("===============tuples example -> immutable object===========")

myTuple = "hello world",10987
print(myTuple)

print(myTuple[0])
print(myTuple[1])
# modifying tuple
myTuple = myTuple[0],"hey",myTuple[1]
print(myTuple)
# myTuple[0] ="hey" wont work because immutable object
# print(myTuple)
myTuple2 = "hello" ,"world" ,2011,(1,"copy"),(2,"paste")
print(myTuple2)
t1,t2,t3,t4,t5 = myTuple2;
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

print("=============== Dictionary and sets: an unorder collection =====================")

fruit = {"orenge": " A sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "A sour,yellow citrus fruit",
         "grape": "A small,sweet fruit growing in bunches",
         "lime" : "A sour,green citrus fruit"}
print(fruit)
print(fruit["lemon"])
fruit["mango"]="A yellow fruit"
print(fruit)
fruit["lemon"] = "lemon update value"
print(fruit)
del fruit["lemon"]
print(fruit)
del fruit
print("deleted dictionary")
print(fruit)


