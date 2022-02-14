#Question1 To count the number of occurrences of each word or character in the string entered by the user

print('Answer 1')

input_value = input("Enter the strings: ").lower().replace("."," ").replace(","," ").split()

if len(input_value)==1:
    input_value = input_value[0]
occurences ={}
for i in input_value:
    if i in occurences:
        occurences[i] +=1
    else:
        occurences[i]=1
for i in occurences:
    print('%s occurence is %d '% (i,occurences[i]))

# question2 to get next date

print('Answer2. ')

def  is_leap_year(year:int):
    
    if year % 400 == 0:
        leap_year = 1
    elif year % 100 == 0:
        leap_year = 0
    elif year % 4 ==0:
        leap_year = 1
    else:
        leap_year = 0



while True:
    
    date = int(input("Day - "))
    month = int(input("Month - "))
    year = int(input("Year - "))

    if date<1 or date>31 or month<1 or month>12 or year<1800 or year>2025:
       print('Use the given conditions to get the next date\nC1 : 1<=month<=12\nC2 : 1<=day<=31\nC3 : 1800<=year<=2025')
       continue
    
    if month in (4,6,9,11) and date == 31:
        print("This  month have only 30 days")
        continue

    elif month == 2 and date >= 29:
        if  is_leap_year(year) and date != 29:
            print("This month have only 29 days")
            continue

        elif not is_leap_year(year):
            print("This month have only 28 days")
            continue
    break       

if month in (1, 3, 5, 7, 8, 10, 12):
   month_length = 31

elif month in (4,6,9,11):
         month_length=30
     
elif month == 2:
        if is_leap_year(year):
            month_length = 29
            
        else:
            month_length = 28
            
if date<month_length:
    date += 1
                
else:
    date = 1
if month == 12:
   month = 1
   year += 1
            
else:
   month += 1
            
print('Next Date is: %d/%d/%d' % (date,month,year))



# Question3 To create a list of tuples with the first element as the number and Second element as the square of the number 

print('Answer3. ')

input_list = eval(input('Enter the list: '))

# list of tuples
output_list = []

for i in input_list :
    output_list.append((i, i**2))
    
print('Output:', output_list)

#Question4

print('Answer4.')

Grade_Points=int(input("Enter  the grade points ; "))

if Grade_Points==10:
    print("Your Grade is 'A+' and Outsatanding Performance")
elif Grade_Points==9:
    print("Your Grade is 'A'  and Excelent Performance")
elif Grade_Points==8:
    print("Your Grade is 'B+' and Very Good Performance")
elif Grade_Points==7:
    print("Your Grade is 'B'  and Good Performance")

elif Grade_Points==6:
    print("Your Grade is 'C+' and Average Performance")

elif Grade_Points==5:
    print("Your Grade is 'C'  and Below Average Performance")
elif Grade_Points==4:
    print("Your Grade is 'D'  and Poor Performance")
else:
    print("error")

#Question5 To print the given pattern
    
print('Answer5. \n ')

given_string = 'ABCDEFGHIJK'
j= 0

while len(given_string)-j*2>= 1:
    print(' '*j+ given_string[0: len(given_string)-j*2])
    j+= 1

# Question6 

print('\n Answer6 :\n')

first_dict = {}

#  Using loops to repeatedly ask user to enter name and SID of students

while True:                                                           
    name = input('Enter the name of the student: ')
    SID = int(input('Enter the SID of %s :'  % name))
    first_dict[SID] = name
    print('\nUse Y or N to enter more data ')
    while True:
        adding_data = input('\nDo you want to enter another SID and Name of students : ')
        if adding_data in ('N'):
            adding_data = 0
            break
        elif adding_data in ('Y'):
            adding_data = 1
            break
        else:
            print('\n Use Y or N ')
            continue
    if adding_data == 0:
        break

# question 6.a
print('\nAnswer6.a \n')                                                                                     

# to print the student details stored in dictionary

for i in first_dict:
    print('The SID of %s  is %d' % (first_dict[i],i))

# question 6.b

print('\nAnswer6.b ')
second_dict = {}

#Sorting the dictionary using student names

for sorted_value in sorted(first_dict.values()):            
    for key,value in first_dict.items():
        if value == sorted_value:
            second_dict[key] = value
                                                      
for i in second_dict:
    print('The SID of %s is %d' % (second_dict[i],i))
# question 6.c

print('\nAnswer6.c \n')
third_dict = {}

#Sorting the dictionary using SID

for sorted_key in sorted(first_dict):                                    
    for key,value in first_dict.items():
        if key == sorted_key:
            third_dict[key] = value
                                                     
for i in third_dict:
    print('The SID of %s is %d' % (third_dict[i],i))
    
# question 6.d

print('\nAnswer6.d \n  ')

# Searching a student details with SID and printing the name of that student

while True:
    search_SID = int(input('Enter the SID of the student you want to search : '))
    if search_SID in first_dict:
        print('The name of student is %s ' % (first_dict[search_SID]))
        break
    else:
        print('\nEnter a valid SID to be searched\nList of valid SID is : %s\n' % list((first_dict.keys())))
        continue


# Question7.  To print Fibonacci series and  find the average of the resultant  Fibonacci series

print('Answer7 ')

# x,y are first and second number respectively 

x = 0
y = 1
sum= 0

while True:

# checking if number of terms are valid or not for fibonacci series

    number = int(input('Enter the number of terms of the fibonacci series: '))
    if number <= 0:
        print('Enter the positive integer  ')
        continue
        
    else:
        print('The Fibonacci series is : ')
        print(x,end=' ')
        for i in range(1,number):
            sum += y
            print(y, end=' ')

# z is used for adding and reassigning the values            

            z = x + y
            x = y
            y = z

 
# Finding the average of fibonacci series

        print('\nThe average of the resultant Fibonacci series is %0.2f\n ' % (sum/number))
        break


# Question 8 Using sets 

# Given data

set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}

print('\nAnswer 8.a')

# To Create a new set of all elements that are in Set1 and Set2 but not both

set4 = set1^set2
print(set4)

print('\nAnswer 8.b')

# To Create a new set of all elements that are in only one of the three sets Set1, Set2 and Set3

set5 = set1^set2^set3
print(set5)


print('\nAnswer 8.c')

# To Create a new set of elements that are exactly two of the sets Set1, Set2 and Set3

set6 = (set1|set2|set3) - (set1^set2^set3) - (set1&set2&set3)
print(set6)

print('\nAnswer 8.d')

# To Create a new set of all integers in the range 1 to 10 that are not in Set1

set7 = set(range(1,11)) - (set1)
print(set7)

print('\nAnswer 8.e')

# To Create a new set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3

set8 = set(range(1,11)) - (set1|set2|set3)
print(set8)   
