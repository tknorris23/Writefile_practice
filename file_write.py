import string
import random

#######################################
##
## Thomas Kelly Norris
## CS344 OSU Winter 2020
## 2/9/2020
## Python Exploration Assignment
## Program that does some file writing
##  and printing to console.
##
#######################################

#initialize vars
string1 = ""
string2 = ""
string3 = ""

#open first file
file = open('string1', 'w')

#create 10 random characters and write to file
for i in range(10):
    randchar = random.choice(string.ascii_lowercase)
    string1 = string1 + randchar
    file.write(randchar)

#add newline and close file
file.write('\n')
file.close()

#open second file
file = open('string2', 'w')

#create 10 random characters and write to file
for i in range(10):
    randchar = random.choice(string.ascii_lowercase)
    string2 = string2 + randchar
    file.write(randchar)

#add newline and close file
file.write('\n')
file.close()

#open third file
file = open('string3', 'w')

#create 10 random characters and write to file
for i in range(10):
    randchar = random.choice(string.ascii_lowercase)
    string3 = string3 + randchar
    file.write(randchar)

#add newline and close file
file.write('\n')
file.close()

#print vars to screen
print(string1)
print(string2)
print(string3)

#Create random ints, then print them and their product
int1 = random.randint(1, 43)
print(int1)
int2 = random.randint(1, 43)
print(int2)
print(int1 * int2)