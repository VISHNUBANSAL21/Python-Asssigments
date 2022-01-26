print( '     ANSWER 1.    ')

given_string='Python is a case sensitive language'

print('a.')

#to find the  length of string

print('Length of the string is:',len(given_string))

#to reverse the string

print('b.')

print('The reverse order of the string is:',given_string[::-1])

# to store the part of string by using slice function

print('c.')

new_string=given_string[10:26]

print('New string will be:',new_string)

# repacing 'a case sensitive with 'object oriented'

print('d.')

print('Replaced string is:',given_string.replace('a case sensitive','object oriented') )

# to find the index of substring 'a'

print('e.')

print('The index of the substring \'a\' is ', given_string.find('a'))

# removing white spaces from the string

print('f.')

print('Sting without white spaces is :',given_string.replace(' ',''))

#to use sting formating 

print('...........')


print('     ANSWER 2.     ')

Name = input('Enter your Name: ')
SID = input('Enter your SID: ')
Department = input('Enter your Department Name:')
CGPA = input('Enter your CGPA: ')


print(''' Hey, %s Here!
My SID is %s
I am from %s department and my CGPA is %s ''' %(Name,SID,Department,CGPA))

print('........')

# using bitwise operators

print('     ANSWER 3.     ')

a=56
b=10

print('a.')

# operator is AND
print('a&b = %d'%(a&b))

print('b.')

# operator is OR
print('a | b = %d'%(a|b))

print('c.')

# operator is XOR
print('a ^ b = %d'%(a^b))

# sifting a abd b with two bits

print('d.')
print('Left shifting a and b with 2 bits: a = %d b = %d'%(a<<2,b<<2))

# shifting a with two bits and b with four bits

print('e.')
print('Right shifting a with 2 bits and b with 4 bits: a = %d b = %d'%(a>>2,b>>4))

# to find the greatest of three numbers entered by the user

print('......')

print('     ANSWER4.     ')

# any three numbers entered by the user

first_number=float(input('Give a number:'))
second_number=float(input('Give a number:'))
third_number=float(input('Give a number:'))

if(first_number>second_number):
    if(first_number>third_number):
        print('greatest number is',first_number)
    else:
        print('greatest number is',third_number)
else:
    if(second_number>third_number):
        print('greatest number is',second_number)
    else:
        print(' greatest number is',third_number)

# to find the word 'name' in the String

print('.......')

print('     ANSWER5.     ')

str=input(' Enter the word : ')
if 'name' in str:
    print('YES')
else:
    print('NO')


# check triangle is possible or not

print('........')

print('     ANSWER6.     ')

# sides of the triangle which are taken by the user

side_1=int(input('Enter the number of first side:'))
side_2=int(input('Enter the number of second side:'))
side_3=int(input('Enter the number of third side:'))


# Theorem says that a Triangle will be posiible only if the largest side is smaller than the sum of other two sides

if(side_1+side_2>side_3 and side_2+side_3>side_1 and side_1+side_3>side_2):
    print('The triangle is possible')
else:
    print('The triangle is not possible')


    









