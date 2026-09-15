# # first_name = "Tony"
# # last_name = "Stark"
# # age = 53
# # height = 1.85

# # superhero_name = input("Enter Tony's superhero name: ")
# # print("Hello " + superhero_name)

# age = int(input("Enter your age: "))
# print("Your recent age is" , age) in cconcatenation only string is added with another string , not other data type
# print("After 5 years your age will be")
# new_age = (age + 5)
# print(new_age)

# a = float(input("Enter first num: "))
# b = float(input("Enter second num: "))
# sum = int(a +b)
# print(sum)
# print("The sum of both numbers is:" , sum)

#college_name = "Khatoon e Pakistan"
# print(college_name.lower())
# print(college_name.find("pak")) only find index number/position
# print(college_name.find("toon"))
#print("p" in college_name) # check if the string is present or not
#print(college_name.replace("Pakistan" , "Pakistan Karachi")) # replace the string with another string

# product_price1 = int(input("Enter price of product 1: "))
# product_price2 = int(input("Enter price of product 2: "))
# product_price3 = int(input("Enter price of product 3: "))
# total_bill_amount = (product_price1 + product_price2 + product_price3)
# avg_price = total_bill_amount / 3
# print("Your total amount is: " , total_bill_amount)
# print("Your average price is: " , avg_price)

# superhero_name = input("Enter any superhero name: ")
# if 'B' in superhero_name: 
#     print("Your superhero name does contain the letter.")
# else:
#     print("Your suprhero name does not contain the letter")

#print(4//2) rounded off division
#print(4/2) simple division

# num1 = 10>5
# num2 = 6<4
# print(num1 or num2)
# print(num1 and num2)
# print(not(num1))

# age = int(input("Enter your age: "))
# if age == 18:
#     print("You can vote") indentation means correct spacing in conditional statements
# elif age>=19:
#     print("You can drive")
# else:
#     print("Your age isn't valid yet")
# print("End of code")

# marks = int(input("Enter your marks: "))
# if marks>=90:
#     print("GRADE A")
# elif marks>=80:
#     print("GRADE B")
# elif marks>=70:
#     print("GRADE C")
# else:
#     print("FAIL")

# a = int(input("Enter the first num: "))
# b = int(input("Enter the second num: "))
# opr = input("Which opreation you wanna perform: ")
# if opr == '+':
#     print(a+b)
# elif opr == '-':
#     print(a-b)
# elif opr == '*':
#     print(a*b)
# elif opr == '/':
#     print(a/b)
# elif opr == '//':
#     print(a//b)
# elif opr == '**':
#     print(a**b)
# else:
#     print("Invalid num")
# print("End of code")

#num = range(8)
#print(num) prints from 0 to 8 but 8 is exceptional
#range(start, stop, step)

# i = 1
# while i <= 5 :
#     print("Nabeera Waheed")
#     i += 1
# j = 5
# while j >= 1 :
#     print(j * "*")
#     j -= 1

#nums = range(11) to print a series of numbers
#for n in nums:
#    print(n)
# nums = range(5) o is always included
# for n in nums:
#     print(n)

# nums = range(1,11) to print even numbers
# for n in nums:
#     if n%2 == 0:
#         print(n)
# for n in range(2, 11, 2):
#     print(n)

# nums = range(1, 51)
# for n in nums:
#     if (n==21):
#         break
#     elif (n%3 == 0):
#         print(n)
# nums = range(1, 41)
# for n in nums:
#     if (n%3 == 0):
#         print(n)
# nums = range(1, 51)
# for n in nums:
#     if (n==21):
#         continue
#     elif (n%3 == 0):
#         print(n)

#for n in range(1, 21, 2): odd numbers
#   print(n)
# i = 1
# while i <= 20:
#     print(i)
#     i+=2

# num = 57 table of 57
# i = 1
# while i <= 10:
#     print(num*i)
#     i += 1

# nums = range(1, 51)
# for n in nums:
#     if n == 15:
#         continue
#     elif n%3 ==0 :
#         print(n)
# print("End of code")

# nums = range(1, 1001)
# a = int(input("Enter num1: "))
# b = int(input("Enter num2: "))
# for n in nums:
#     if (n%a==0 and n%b==0):
#         print("First number that is divisible by both: " , n)
#         break

# marks = [45, 78, 45, 90, 'A', 'C'] #List: is like a container, contains collection of multiple values, can be changeable(muteable) and it stores different datatypes values.
# print(marks)
# print(type(marks))
# print(marks[0]) #write index to see the position of values
# print(marks[4])
# print(marks[-1]) #last value of list
# print(marks[-6]) #counting from last as -1
# print(len(marks)) #length of marks: how many values include in list  
# print(marks[0: 4]) #slicing a list: list starting and stop value declare by the user 
# print(marks[-2:]) #from index -2 to last index whixh is -1
# print(marks[ :-2]) #start from index 0 to end at before the index -2
# print(marks[:]) #print the entire list
# print(marks[:2])

# marks = [45, 67, 45, 56, 24]
# for value in marks:
#     print(value)
# marks.append(23) #to add more values at the end
# print(marks)
# marks.insert(0, 88) #add 88 at index 0
# print(marks)
 
