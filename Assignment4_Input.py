#Question 1

print("Answer1")

# Recursive Python function to solve the tower of hanoi
 
def Tower_Of_Hanoi(n , source, destination, auxiliary):
    if n==0:
        return
    
    Tower_Of_Hanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from ",source,"to ",destination)
    Tower_Of_Hanoi(n-1, auxiliary, destination, source)
         
#  Calling function for 3 disks and A,B,C  are the name of rods
Tower_Of_Hanoi(3,"A","C","B")

#Question2

print("\nAnswer2")
while True:                                                                                           
    n = int(input("Enter the number of rows in Pascal's Triangle: "))                                      
    if n >= 0:
        break
    else:
        print("The value of number of rows must be postive integer:")
        

#Using RECURSION Method
print("The Pascal's Triangle using recursion is:")
def pascal(n, originaln=n):
    if n == 0:
        return
    pascal(n-1,originaln)

#printing the spaces
    print(' '*(originaln-n), end='')

#first number is always start with 1
    entry = 1

    for i in range(1, n+1):
        print(entry, end =' ')

#using Binomial Coefficient
        entry = entry * (n - i) // i
    print()

pascal(n)        

# Using ITERATION Method

from math import comb

print("The Pascal's Triangle using iteration is:")
for i in range(n):                                                                                      
    print((n-i-1)*" ",end="")                                                               
    for j in range(n):                                                                                  
        if comb(i,j) != 0:                                                                          
            print(comb(i,j),end=" ")                                                                    
    print()                                                                                             


#Question3

print("\nAnswer3")

# taking two integer value from the user
int1 =int(input("Enter first number: "))
int2=int(input("Enter second number: "))

ans = divmod(int1,int2)

print( "\nthe quotient is %d and reminder is %d" % (ans[0],ans[1]) )

#Question 3.a

print("\nAnswer3.a Check whether it(function/values) is callable or not :")                                 
a_part = callable(divmod)
print(a_part, end="")
if a_part == True:
    print(" it is callable")
else:
    print("it is not callable")

#Question3.b    

print("\nAnswer3.b Check whether all the values are zero or not:")                                             
if all(i != 0 for i in ans):
    print("All values are non-zero.")
else:
    print("All values are not non-zero")

#Question3.c

print("\nAnswer3.c ")                           
c_list = ans + (4,5,6)
c_part = sorted(list((i for i in c_list if i>4)))
print("Values greater than 4 are:", c_part)

#Question3.d

print("\nAnswer3.d")                                          
set_result = set(c_part)
print("Converting the above result into set datatype:", set_result)

#Question3.e

print("\nAnswer3.e Make the set immutable:")                                                                   
set_frozen = frozenset(set_result)
print("The immutable set would be:",set_frozen)

#Question3.f

print("\nAnser3.f")                      
f_part = max(set_frozen)
print("The maximum value from the set is:", f_part)
print("Hash value of the max value from the above set:", hash(max(set_frozen)))


#QUESTION 4

print("\nAnswer4")


# Creating a class

class Student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
        print("Object created")
    def __del__(self):
        print("Object destroyed")


#Creating object
Student1 = Student("Vishnu Bansal",21104042)

#print the assigned values
print("The name of the student is %s and  roll number is %d" % (Student1.name,Student1.roll_number))

#Deleting object

del Student1



#Question5

print("\nAnswer5")

#Creating class 
class Employee:                                         
    def __init__(self,name,salary):        
        self.name = name
        self.salary = salary
    def print_data(self):
        print("%s has a salary of %d rupees" % (self.name,self.salary))


# creating employee records
employee1 = Employee("Mehak",40000)             
employee2 = Employee("Ashok",50000)
employee3 = Employee("Viren",60000)

print("The record of employees is:")               
for i in [employee1,employee2,employee3]:
    i.print_data()
    
#Question5.a  Updating the salary of Mehak to 70000

print("\nAnswer 5.a")
print("The record of employees after updating the salary of %s from %d to " % (employee1.name,employee1.salary),end="")

employee1.salary = 70000
print(employee1.salary)

for i in [employee1,employee2,employee3]:
    i.print_data()

    
#Question5.b To delete the record of employee Viren

print("\nAnswer5.b")
print("The record of employees after deleting the record of %s " % (employee3.name))

del employee3

for i in [employee1,employee2]:
    i.print_data()

#Question 6

print("\nAnswer6")

#inputting a word from the first friend
random_word =input("Enter any word: ")
random_word=random_word.lower()

#inputting a meaningful word with the exact same letters
test_word = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
test_word=test_word.lower()

#defining dictionary
def count_in_dict(random_word):
    count = {}
    list1 = list(random_word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

#shopkeeper's input to verify the word's meaning
def userinput():
    if count_in_dict(random_word) != count_in_dict(test_word):
        print("The letters aren't exact, friendship is fake")
        return
    ans = input("Does the word makes sense?(y or n )")

    if ans == 'y':
        print("The friends passes the friendship test")
    elif ans == 'n':
        print("The word doesn't have any meaning, friendship is fake")
    else:
        print("Invalid input,try again with y or n ")
        userinput()
userinput()



