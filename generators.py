# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 21:29:50 2023

@author: sai
"""

#Generator 
#It is another way of creating iterator
#in a similar way where
#it uses the keyword "yield"
#instead of returning it in a defined function,
##Generators are implemented using function
#For tuple comprehension object is created.
#When you are going to use tuple comprehension one object 
#will be created. and you can access the values of that 
#object using for loop.

gen={x for x in range(3)}
print(gen)
for num in gen:     #gen=object
    print(num)
    
    
#Another method    
gen=(x for x in range(3))
next(gen)
next(gen)
next(gen)    #next is used to show the output step by step
 
#Function which returns multiple values

def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)
        
##################################################################   
#Now instead of using for loop we can write our own generators.

gen=range_even(6)
next(gen)
next(gen)
next(gen)

#Chaining generators

def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
passwords=["not good","give'm-pass","00100-100"]

for password in hide(lengths(passwords)):
    print(password)
        
#Enumerate
#printing list with index

lst=['Milk','Egg','Bread']
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')
    
#Using enumerate
lst=['Milk','Egg','Bread'] 
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
    
#############################################################






































    
    
    
    