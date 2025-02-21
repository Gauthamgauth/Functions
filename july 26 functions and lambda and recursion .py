#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("hello world")


# In[1]:


total_num = lambda x , y : x + y 
print(total_num(10,20))


# In[7]:


total_num = lambda x , y : x if x > y  else "no" 
print(total_num(10,20))


# In[17]:


total_numbers = lambda number : number ** 2 
print(total_numbers(9))


# In[21]:


number = lambda x : x * x 
num = int(input("enter your number"))
print(number(num))


# In[22]:


add = lambda x,y,z: x + y + z
print(add(10,20,30))


# In[23]:


add_numbers = lambda x , y : x + y 
num1 = int(input("add first number"))
num2 = int(input("add second number"))
print(add_numbers(num1,num2))


# In[36]:


numbers = lambda x : [i ** 2 for i in x] 
print(numbers([2,3,4,5,6,7]))


# In[65]:


products = [{"name": "mobile","price":"12000"},
            {"name": "computer","price":"100"},
            {'name':"laptop","price":"50000"},
            {"name":"fridge","price":"4000"},]
sorted_products = sorted(products, key = lambda x : x ["price"])
for products in sorted_products:
    print(products)


# In[117]:


def prime_num():
    num = []
    for i in range(2,50):
            if i % 2 == 0 :
                num.append(i)
    return num 


# In[118]:


prime_num()


# In[134]:


# prime numbers = divisible by 1 and itself
def prime_num():
    num = []
    for i in range(1,50):
        if i % 2 == 1 and i % 2 == 0 :
            num.append(i)
    return num 


# In[135]:


prime_num()


# In[163]:


# leap years from 1400,2500
def leap_years():
    num = []
    for i in range(1400 ,2500):
        if i % 100 == 0:
            num.append(i)
    return num
leap_years()


# In[172]:


def leap_years():
    num = []
    for i in range(1400,2500):
        if i % 4  == 0:    
            num.append(i)
    return num
leap_years()


# In[2]:


def leap_years():
    return [i for i in range(1400, 2500) if (i % 4 == 0 and (i % 100 != 0 or i % 400 == 0))]

print(leap_years())


# #Recursion

# In[23]:


def rec_sum(n):
    if n == 1:
        return n 
    else :
        return n + rec_sum(n-1)
print(rec_sum(5))


# In[24]:


def rec_sum(n):
    if n == 1:
        return n
    else :
        return n - rec_sum(n-1)
print(rec_sum(5))


# In[4]:


#1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a 
#lambda function that multiplies argument x with argument y and prints the result.
#Sample Output:
#25
#48
add_num = lambda x,y:x*y
print(add_num(5,5))


# In[7]:


add_num = lambda x,y : x*y
print(add_num(6,8))


# In[9]:


add_num = lambda x,y : x+y
print(add_num(10,5))


# In[11]:


add_num = lambda x,y : x*y
print(add_num(3,5))


# In[12]:


add_num = lambda x : x + 15
print(add_num(10))
mul_num = lambda x, y : x * y 
print(mul_num(6,8))


# In[13]:


#2. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown
#given number.
#Sample Output:
#Double the number of 15 = 30
#Triple the number of 15 = 45
#Quadruple the number of 15 = 60
#Quintuple the number 15 = 75

num = lambda x : x *15
print(num(2))

num = lambda x : x * 15
print(num(3))

num = lambda x : x * 15
print(num(4))

num = lambda x : x * 15
print(num(5))


# In[15]:


def multiple(n):
    return lambda x : x * n 
double = multiple(2)
triple = multiple(3)
quadruple = multiple(4)
quintuple = multiple(5)

n = 15
print(double(n))
print(triple(n))
print(quadruple(n))
print(quintuple(n))


# In[41]:


#3. Write a Python program to sort a list of tuples using Lambda.
#Original list of tuples:
#[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
#Sorting the List of Tuples:
#[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97mar


marks_scored = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_marks = sorted (marks_scored, key = lambda x : x [1])
for marks_scored in sorted_marks:
    print(marks_scored)


# In[57]:


phone_brands = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
                {'make': 'Mi Max', 'model': 2 , 'color': 'Gold'}, 
                {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sorted_phones = sorted (phone_brands, key = lambda x : x ['model'])

print(sorted_phones)





# In[71]:


#Write a Python program to filter a list of integers using Lambda.
#Original list7, 8, 9, 10]
#Even numbers from the said list:
#[2, 4, 6, 8, 10]
#Odd numbers from the said list:
#[1, 3, 5, 7, 9] of integers:
#[1, 2, 3, 4, 5, 6, 
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = list(filter(lambda x : x % 2 == 0,num))
print(even_num)


# In[90]:


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = lambda x : x ** 2,num
print(square)


# In[ ]:





# In[ ]:





# In[ ]:





# In[148]:


class Person:
    def __init__(self,name1,last_name1):
        self.name=name1
        self.last_name=last_name1
    def __str__(self):
        return f"the name is {self.name} and last name is {self.last_name}"
    


# In[149]:


person1=Person("Gauthma","Krishna")
print(person1)


# In[152]:


class Account:
    def __init__(self,first_name1,last_name1,number1):
        self.holder=first_name1
        self.holder_last_name=last_name1
        self.number=number1
    def __str__(self):
        return f"the name holder{self.holder},last name is{self.holder_last_name},account number is {self.number}"


# In[ ]:





# In[ ]:





# In[ ]:


class BankAccount:
    def __init__(self,account_number,account_holder,balance=0):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




