# Dictionary 
# Create a dictionary to store a student's name, age, and grade. Print all information.
# students = {
#     "s1" : {"name" : "sara","age":19,"grade":"A"},
#     "s2" : {"name":"ali","age":20,"grade":"B"},
#     "s3" : {"name":"sana","age":21,"grade":"C"}
# }
# print(students)
# for key,values in students.items():
#     print(key,values)
# for key in students.keys():
#     print(key)
 
# Add a new key-value pair to an existing dictionary.
# students = {
#     "s1" : {"name" : "sara","age":19,"grade":"A"},
#     "s2" : {"name":"ali","age":20,"grade":"B"},
#     "s3" : {"name":"sana","age":21,"grade":"C"}
# }
# students["s4"] = {"name":"ahmad","age":18,"grade":"A+"}
# print(students)

# Update the value of an existing key in a dictionary.
# students = {
#     "s1" : {"name" : "sara","age":19,"grade":"A"},
#     "s2" : {"name":"ali","age":20,"grade":"B"},
#     "s3" : {"name":"sana","age":21,"grade":"C"}
# }
# students["s2"]["age"] = 21
# print(students)

# Delete a specific key from a dictionary.
# students = {
#     "s1" : {"name" : "sara","age":19,"grade":"A"},
#     "s2" : {"name":"ali","age":20,"grade":"B"},
#     "s3" : {"name":"sana","age":21,"grade":"C"}
# }

# del students["s2"]["age"]
# print(students)

# Check whether a given key exists in a dictionary.
# students = {
#     "s1" : {"name" : "sara","age":19,"grade":"A"},
#     "s2" : {"name":"ali","age":20,"grade":"B"},
#     "s3" : {"name":"sana","age":21,"grade":"C"}
# }
# if "s4" in students:
#     print("present")
# else:
#     print("not present")

# Count the total number of keys in a dictionary.
# count = 0
# students = {
#     "s1" : {"name" : "sara","age":19,"grade":"A"},
#     "s2" : {"name":"ali","age":20,"grade":"B"},
#     "s3" : {"name":"sana","age":21,"grade":"C"}
# }
# for key in students.keys():
#     count += 1
# print(count)

 #----------------tuple------------------
# Create a tuple containing 5 student names and print all names using a loop.
# student = ("ali","sara","ahmad","sana","amjad")
# # for name in student:
#     print(name)
# new = list(student)
# new.append("zara")
# student = tuple(new)
# print(student)

# reate a tuple of numbers and find the largest number.
# numbers = (1,2,3,4,5,6,7)
# largest = numbers[0]
# for num in numbers:
#     if num>largest:
#         largest = num
# print(largest)

# Create a tuple of numbers and find the smallest number.
# numbers = (1,2,3,4,5,6,7)
# smallest = numbers[0]
# for num in numbers:
#     if num<smallest:
#         smallest = num
# print(smallest)

# Count how many times a specific value appears in a tuple.
# numbers = (1,1,1,2,2,4,5,6,7,8,6)
# frequency = {}
# for num in numbers:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1
# print(frequency)

# Find the sum and average of all elements in a tuple.
# numbers = (1,2,3,4,5)
# sum = 0
# for i in numbers:
#     sum = sum+i
# print("sum is : ",sum)
# print("average is :",sum/len(numbers))

#--------------------SET----------------
# Create a set of numbers and print all elements using a loop.
# number = {1,2,3,4,5,6}
# for i in number:
#     print(i)

# Add a new element to a set and print the updated set.
# number = {1,2,3,4,5,6}
# number.add(7)
# print(number)
# fruits = {"apple","banana"}
# fruits.add("kiwi")
# print(fruits)

# Remove an element from a set.
# fruits = {"apple","banana","kiwi"}
# fruits.remove("kiwi")
# print(fruits)

# Given a list containing duplicate values, convert it into a set and print only unique values.
# numbers = {1,2,3,3,4,4,5,6}
# new_set = set(numbers)
# print(new_set)

# ------------------fibonacci serirs-----------
# num = int(input("enter num : "))
# a = 0
# b = 1
# print("fibonacci numbers")
# for  i in range(num):
#     print(a,end=" ")
#     c = a+b
#     a = b
#     b = c
# --------------prime numbers-----------
num = int(input("enter num : "))
if num<=1:
    print("not prime")
else:
    for i in range(2,num):
       if num%i == 0:
          print("not prime")
    else:
        print("prime")
