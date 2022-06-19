# Write a Python program to calculate the length of a string.
def word(word):
    x=len(word)
    print(x)
word("nopshacom")  

# Write a Python program to count the number of characters (character frequency) in a string
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('twitter.com'))    
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string

def str_mode(name):
    if len(name) < 2:
        return ""
    return  name[0:2] + name[-2:]
       
        
print(str_mode("friends"))
        
#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself      
def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restartringr'))

#  Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string
# def str_name():
#     a="liz"
#     c="beth"
#     d=a+ " " +c
#     y=   a[:2]+ a[2:]
#     return d
# print(str_name())  
def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))   
# print the first element in list 2
def nesting():
    my_list=["mango",[2,3,4,6,8],[8,8,5,6]]
    
    print(my_list[1][3])
nesting()
# remove the last element in the list and return the list
def numbers():
    x=[1,2,3,4,5]  
    x.remove(x[4])
    print(x)
numbers()  
def num(numbers):
    numbers.remove(numbers[6]) 
    print(numbers) 
num([1,2,3,4,5,6,7])  
# count the number monday appears
def days():
    mylist=["monday","tuesday","wednesday","thursday","monday"]
    y=  mylist.count("monday")
    print(y)
days()  
# return the smallest
def smallest():
    small=[3,6,8,2,4,1,5,7]
    y=min(small)
    print(y)
smallest()
# return the divisibles of seven from 100,200
def divisable_byseven():
    x=[]
    for a in range(100,200):
        
        if a%7==0:
            x.append(a)
            print(x)
divisable_byseven()   
def divisibles():
    for n in range(100,200):
        if n%7==0:
            print(n)   
divisibles()
# check the number if its less than 10 or greator than 10
def inputsin():
    num1=int(input("enter number1:"))   
    num2=int(input("enter number2:"))
    sum=num1+num2
    if sum>10:
        print("the sum is greater than 10")
    else:
        sum<=10
        print("the sum is lessthan or equal 10 " )
inputsin()    
# checks if 4 is in a list
def thelist():
    a=[1,2,3,43,5]
    if 4 in a:
        print(True)
    else:
        print(False)
thelist()   

def find(a):
    if 4 in a:
        print(True)
    else:
        print(False) 
find([1,2,3,4,5])  
# removes the last fruit
def fruits(fruit):
    fruit.remove(fruit[2])
    print(fruit)
fruits(["pineapple","grapes","orange"]) 

def cars(car):
    car.sort()
    print(car)
cars(["Ford","BMW","Volvo"])    
     
  
      
       
         
        
                    

  
  
            
        