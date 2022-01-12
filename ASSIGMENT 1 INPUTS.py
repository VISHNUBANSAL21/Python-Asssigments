# QUES 1. To find the average of the three number entered by the user

print('ANSWER 1')

# Inputs
number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))
number3 = float(input('Enter third number: '))

# Calculate Avearge
average = (number1 + number2+ number3)/3

# Result
print('Avearge of numbers: ',average)

print('.......')

print('ANSWER 2')


# QUES 2. To compute a person's income tax

# Enter your gross income
GROSS_INCOME = int(input('Enter the  gross income in dollar : '))

# These are given constants to calculate INCOME TAX and all these amounts are in dollar currency
Standard_deduction = 10000

Dependent_deduction= 3000

Tax_rate= 0.02

# Enter the number of dependents
DEPENDENTS = int(input('Enter the number of dependents: '))

# Calculate Taxable income 
TAXABLE_INCOME = GROSS_INCOME - Standard_deduction- (Dependent_deduction * DEPENDENTS)

# Calculate Income tax 
TAX = TAXABLE_INCOME * Tax_rate

# RESULT
print('Person Income Tax is',TAX)

print('.......')

print('ANSWER 3')


# QUES 3. To store different data type into a list


# INPUTS

# Enter your SID
Student_ID= int(input('Enter SID: '))

# Enter your name
NAME  = str(input('Enter Student Name: '))

print('Type M for male , F for female,U for others')

# Enter your gender
GENDER= str(input( 'Enter Gender: '))         

# Enter your course name
COURSE_NAME = (input('Enter Course Name: ' ))  

# Enter your CGPA 
CGPA    =  float(input('Enter CGPA: '))      

# RESULT

print('Student',[Student_ID,NAME,GENDER,COURSE_NAME,CGPA])

print('.......')

print('ANSWER 4')


# QUES 4 Enter marks of 5 students into a list and display them in sorted manner

# x,y,z,w,a are students names

x= float(input('Marks of 1st student: '))
y= float(input('Marks of 2nd student: '))
z= float(input('Marks of 3rd student: '))
w= float(input('Marks of 4th student: '))
a= float(input('Marks of 5th student: '))

SortedMarks= [x,y,z,w,a]

SortedMarks.sort()

# Result

print(SortedMarks)

print('.......')

print('ANSWER 5.A')

# QUES 5.A Print a specified list after removing 4th element

# Inputs
list= ['Red','Green','White','Black','Pink','Yellow']

# Remove the 4th index from the list
list.pop(4)

# Result

print ('color',list)

print('.......')

print('ANSWER 5.B')

# QUES 5.B Remove black and pink from the list and replace them with purple

# Inputs
list= ['Red','Green','White','Black','Pink','Yellow']

# Replacing fouth and fifth value with purple

list[3:5] = ['purple']

# Result

print('color',list)






