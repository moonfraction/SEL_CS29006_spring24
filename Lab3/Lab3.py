# ofc i typed this all by myself ;)


#Write a program which will merge the words “Welcome”, “to”, “Python”, “Programming” into a single string “Welcome to Python Programming”
words = ["Welcome", "to", "Python", "Programming"]
merged_string = " ".join(words)
print(merged_string)
print('---------------------------------------------------')

# tuple of a student is (<name>, <marks>, <deptt>). For example, (‘Debasis’, 98.5, “CS”) is a tuple. Create a list which contains 3 different tuples in it. Print the list.
student = [("Debasis", 98.5, "CS"), ("Rahul", 99.5, "CS"), ("Raj", 96.5, "CS")]
print(student)
print('---------------------------------------------------')

# Python program to demonstrate the use of update() method
list1 = [2, 3]
list2 = [5, 7, 6 ,1]
list3 = [10, 11, 12,-1]
# Lists converted to sets
set1 = set(list2)
set2 = set(list1)
# Update method
set1.update(set2)
# Print the updated set
print(set1)
# List is passed as an parameter which gets automatically converted to a set
set1.update(list3)
print(set1)
print('---------------------------------------------------')

#Write a program which will take the following lists and set to create a larger list, which should include all the elements in the list. Also, find the union, intersection and difference of the sets obtained from the list List1 and List2. Print all the sets you have obtained.
List1 = [1, 2, 3, 4]
List2 = [1, 4, 2, 3, 5]
Set3 = {'a', 'b', 'c'}

combined_list = List1 + List2
print(combined_list)
combine_list_and_set = List1 + List2 + list(Set3)
print(combine_list_and_set)

# Convert list to set
Set1 = set(List1)
Set2 = set(List2)
# Union of two sets
Set4 = Set1.union(Set2)
print(Set4)
# Intersection of two sets
Set5 = Set1.intersection(Set2)
print(Set5)
# Difference of two sets
Set6 = Set1.difference(Set2)
print(Set6)
print('---------------------------------------------------')


#Given a set and a dictionary as below. Write a program which will include all the elements from the dictionary to set.
Set1 = {1, 2, 3, 4, 5}
myDict = {6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten'}
#Hint:
#Set1.update(myDict)
#Print the updated set
Set1.update(myDict)
print(Set1)
print('---------------------------------------------------')


# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
# Adding elements one at a time
Dict[0] = 'Apple'
Dict[1] = 'Banana'
Dict[2] = 'Mango'
print("\nDictionary after adding 3 elements: ")
print(Dict)
# Adding set of values to a single Key
Dict[3] = 'Orange', 'Cherry', 'Guava'
print("\nDictionary after adding 3 elements: ")
print(Dict)
# Updating existing Key's Value
Dict[2] = 'Water Mellon'
print("\nUpdated key value: ")
print(Dict)
print('---------------------------------------------------')

a = 33
b = 200
if b > a:
    print("b is greater than a") # you will get an error
print('---------------------------------------------------')

#Generate n random numbers and print whether the sum of all the prime numbers is a prime
import random
import math
# n = int(input("Enter the number of random numbers to be generated: "))
n = 10
sum = 0
for i in range(n):
    x = random.randint(1, 100)
    print(x)
    #if it is prime then add to sum
    if x > 1:
        for i in range(2, int(math.sqrt(x)) + 1):
            if (x % i) == 0:
                print(x, "is not a prime number")
                break
        else:
            print(x, "is a prime number")
            sum = sum + x
print("Sum of the primes in random numbers is: ", sum)
if sum > 1:
    for i in range(2, int(math.sqrt(sum)) + 1):
        if (sum % i) == 0:
            print(sum, "is not a prime number")
            break
    else:
        print(sum, "is a prime number")
else:
    print(sum, "is not a prime number")
print('---------------------------------------------------')

#Write a function to calculate the factorial value of any integer number n. Call the function for the different values of n
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
# n = int(input("Enter the number: "))
n =6
if n < 0:
    print("Factorial of negative numbers does not exist")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", n, "is", factorial(n))
print('---------------------------------------------------')

#Write a function which will take any two values of any type and swap the values.
def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y
# x = input("Enter the first value: ")
# y = input("Enter the second value: ")
x, y = 2, 3
print("Before swapping: ")
print("x =", x)
print("y =", y)
x, y = swap(x, y)
print("After swapping: ")
print("x =", x)
print("y =", y)
print('---------------------------------------------------')


#Write a function which will take any three integer values as the arguments and return a list in ascending order
def ascending_order(a, b, c):
    list = [a, b, c]
    list.sort()
    return list
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
a, b, c = 3, 2, 1
list = ascending_order(a, b, c)
print(list)
print('---------------------------------------------------')

#28. Write a recursive function to calculate the following:
#(a) Factorial value of a positive integer passed as an argument.
#(b)Greatest common divisor (GCD) of two positive integer values. 
#(c) The n-th Fibonacci number.
#(d) The sum of first n-harmonic numbers in a harmonic series.
#(e) Searching an element in a list of elements.

#(a) Factorial value of a positive integer passed as an argument.
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
# n = int(input("Enter the number: "))
n = 6
if n < 0:
    print("Factorial of negative numbers does not exist")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", n, "is", factorial(n))
print('---------------------------------------------------')

#(b)Greatest common divisor (GCD) of two positive integer values.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
a, b = 60, 48
print("GCD of", a, "and", b, "is", gcd(a, b))
print('---------------------------------------------------')

#(c) The n-th Fibonacci number.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# n = int(input("Enter the number: "))
n = 10
if n <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i))
print('---------------------------------------------------')

#(d) The sum of first n-harmonic numbers in a harmonic series.
def harmonic(n):
    if n == 1:
        return n
    else:
        return (1 / n) + harmonic(n-1)
# n = int(input("Enter the number: "))
n = 5
if n < 0:
    print("Please enter a positive integer")
else:
    print("Sum of first", n, "harmonic numbers is", harmonic(n))
print('---------------------------------------------------')

#(e) Searching an element in a list of elements.
def search(list, n):
    if len(list) == 0:
        return False
    else:
        if list[0] == n:
            return True
        else:
            return search(list[1:], n)
list = [1, 2, 3, 4, 5]
# n = int(input("Enter the number to be searched: "))
n = 5
if search(list, n):
    print("Found")
else:
    print("Not found")
print('---------------------------------------------------')

#Write a function to return the number of characters in a string. The string value should be passed as an argument to the function.
def string_length(str):
    count = 0
    for char in str:
        count += 1
    return count
# str = input("Enter the string: ")
str = "Hello World"
print("The length of the string is:", string_length(str))
print('---------------------------------------------------')

#30. Write a program which will read a character and then it will print as a consonant or vowel.

# ch = input("Enter the character: ")
ch = "a"
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print(ch, "is a vowel")
else:
    print(ch, "is a consonant") 
print('---------------------------------------------------')

#Write a program which will read two numbers from the user and check if they are co-prime numbers
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
a, b = 3, 4
if a > b:
    smaller = b
else:
    smaller = a
for i in range(1, smaller + 1):
    if ((a % i == 0) and (b % i == 0)):
        hcf = i
if hcf == 1:
    print(a, "and", b, "are co-prime numbers")
else:
    print(a, "and", b, "are not co-prime numbers")
print('---------------------------------------------------')


#Write a function to read a list of numbers, store them in a list and use the list to find the following. 
#Write iterative and recursive functions.
#(a) Sum of the numbers
#(b) Mean of the number
#(c) Rang of the numbers
#(d) Standard deviation of the numbers
list = [1, 2, 3, 4, 5]

#(a) Sum of the numbers
def sum(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum
print("Sum of the numbers is:", sum(list))

#(b) Mean of the number
def mean(list):
    mean = sum(list) / len(list)
    return mean
print("Mean of the numbers is:", mean(list))

#(c) Rang of the numbers
def rang(list):
    rang = max(list) - min(list)
    return rang
print("Rang of the numbers is:", rang(list))

#(d) Standard deviation of the numbers
def standard_deviation(list):
    mean1 = mean(list)
    sum = 0
    for i in list:
        sum = sum + (i - mean1) ** 2
    standard_deviation = (sum / len(list)) ** 0.5
    return standard_deviation
print("Standard deviation of the numbers is:", standard_deviation(list))
print('---------------------------------------------------')


student={'Archana':28,'krishna':25,'Ramesh':32,'vineeth':25}
def test(student):
    new={'alok':30,'Nevadan':28}
    student.update(new)
    print("Inside the function",student)
    return
test(student)
print("outside the function:",student)
print('---------------------------------------------------')

#Write a Python function to count the occurrences of each word in a given sentence
def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts
str = "the quick brown fox jumps over the lazy dog."
print(word_count(str))
print('---------------------------------------------------')

#Create a function that returns the sum of digits in a given integer.
def sum_of_digits(n):
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n // 10
    return sum
# n = int(input("Enter the number: "))
n = 123
print("Sum of digits in", n, "is", sum_of_digits(n))
print('---------------------------------------------------')


#Write a Python function to find the common elements between two lists and print common elements
def common_elements(list1, list2):
    list = []
    for x in list1:
        for y in list2:
            if x == y:
                list.append(x)
    return list
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
list = common_elements(list1, list2)
if(len(list)):
    print(list)
else:
    print("No common elements")
print('---------------------------------------------------')

#Write a function to reverse a string without using slicing
def reverse(str):
    str1 = ""
    for i in str:
        str1 = i + str1
    return str1
# str = input("Enter the string: ")
str = "Hello World"
print("The original string is:", str)
print("The reversed string is:", reverse(str))
print('---------------------------------------------------')

#Develop a function to check if a given number, is a palindrome
def palindrome(n):
    temp = n
    rev = 0
    while(n > 0):
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if(temp == rev):
        return True
    else:
        return False
# n = int(input("Enter the number: "))
n = 121
if(palindrome(n)):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
print('---------------------------------------------------')


#Create a function that checks if a given string is a valid email address
def check_email(str):
    if '@' not in str:
        return False
    else:
        return True
# str = input("Enter the email address: ")
str = "hehe@kyahua"
if(check_email(str)):
    print("Valid email address")
else:
    print("Invalid email address")
print('---------------------------------------------------')

#Write a function that will print any non-max number in a list
def non_max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    list.remove(max)
    return max
list = [1, 2, 3, 4, 5]
print("The list is:", list)
maxi = non_max(list)
randi = random.randint(0, len(list) - 1)
print("The non-max number is:", list[randi])
print('---------------------------------------------------')



# 41: Creating a file to write some text into it
# Python code to create a file
file = open('test.txt','w') # Opening the file in write mode
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close() # Closing the file
# Alternative method: with-write()
# Python code to illustrate with() along with write()
with open("test2.txt", "w") as f:
    f.write("Hello World!!!")
print('---------------------------------------------------')    

    
# 42: Opening an existing file

# a file named "test.txt" is already available in your machine
# This program will open the file in reading mode.
file1 = open('test.txt') # Default is read and text mode
file2 = open('test.txt', 'r')
file3 = open('test.txt', 'rt')
# This will print every line one by one in the file
for each in file1:
    print (each)

# Python code to illustrate with()
# along with open() function
with open("test.txt", "r") as file1:
    # Reading data line by line
    for line in file1:
        print(line)
        
# Python code to illustrate split() function
with open("test.txt", "r") as file:
    data = file.readlines()
for line in data:
    word = line.split()
    print (word)
print('---------------------------------------------------')

# 43: Opening a file in append mode
# Python code to illustrate append() mode
file = open('test.txt', 'a')
file.write("\nThis will add at the end of the file.\n hehe hehe\nkya kya\nhua\nhua")
file.close()
file1 = open('test.txt') 
for each in file1:
    print (each)
print('---------------------------------------------------')

# 44: Exercising the important file handling functions
import os
def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('Hello, world!\n')
        print("File " + filename + " created successfully.")
    except IOError:
        print("Error: could not create file " + filename)
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
        print(contents)
    except IOError:
        print("Error: could not read file " + filename)
def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)
def rename_file(filename, new_filename):
    try:   
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " + new_filename + " successfully.")
    except IOError:
        print("Error: could not rename file " + filename)
def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)
if __name__ == '__main__':
    filename = "example.txt"
    new_filename = "new_example.txt"
    create_file(filename)
    read_file(filename)
    append_file(filename, "This is some additional text.\n")
    read_file(filename)
    rename_file(filename, new_filename)
    read_file(new_filename)
    delete_file(new_filename)
print('---------------------------------------------------')

#Create a program that counts the number of vowels in a text file.
hehefile = open("test.txt", "r")
count = 0
for line in hehefile:
    for ch in line:
        if ch in "aeiouAEIOU":
            count += 1
hehefile.close()
print("Number of vowels in the file are:", count)
print('---------------------------------------------------')

#search a word in text file
file = open("test.txt", "r")
count = 0
# word = input("Enter the word to be searched: ")
word = "This"
for line in file:
    words = line.split()
    for i in words:
        if i == word:
            count += 1
print("Occurrences of the word:", count)
file.close()
print('---------------------------------------------------')

#remove duplicate words from test.txt file
def search(word, file_name):
    file = open(file_name, "r")
    for line in file:
        words = line.split()
        for i in words:
            if i == word:
                return True
    file.close()
    return False

file = open("test.txt", "r")
for line in file:
    words = line.split()
    for word in words:
        if not search(word, "test2.txt"):
            open ("test2.txt", "a").write(word + " ")
file.close()
print('---------------------------------------------------')


#Write a Python program that reads the contents of a text file named "data.txt" and prints them
with open ("test.txt", "r") as f:
    print(f.read())
print('---------------------------------------------------')

#Write a Python script to count the number of words in a text file
file = open("test.txt", "r")
count = 0
for line in file:
    words = line.split()
    count = count + len(words)
print("Number of words in the file:", count)
file.close()
print('---------------------------------------------------')


#Implement a program that searches for a specific word in a text file and prints its occurrences.
file = open("test.txt", "r")
count = 0
# word = input("Enter the word to be searched: ")
word = "This"
for line in file:
    words = line.split()
    for i in words:
        if i == word:
            count += 1
print("Occurrences of the word:", count)
file.close()
print('---------------------------------------------------')

#Write a program which will invert a file. Don’t use any extra file other than the input file for this

#i will just copy my original file to a dummy file, then i will reverse the dummy file
#just dont want to mess with my original file
import shutil
shutil.copyfile('test.txt', 'destination.txt')
shutil.copyfile('test.txt', 'destination2.txt')

#below inverts the file, but not reverses the words
with open("destination.txt", "r+") as file:
    lines = file.readlines()
    file.seek(0)
    file.truncate()
    file.writelines(reversed(lines))
    
#this also reverses the words
with open("destination2.txt", "r+") as file:
    lines = file.readlines()
    file.seek(0)
    file.truncate()
    for line in reversed(lines):
        words = line.split()
        for word in reversed(words):
            word = reverse(word)
            file.write(word)
            file.write(" ")
        file.write("\n")
print('---------------------------------------------------')

