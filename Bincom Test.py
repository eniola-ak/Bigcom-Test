#!/usr/bin/env python
# coding: utf-8

# In[49]:


#Fibonacci using defining a function 
def howmany(n):
    n1, n2 = 0, 1
    count = 0

    if n <= 0:
        print("Enter a positive integer")
    elif n == 1:
        print(n1)
    else:
        while count < n:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
print (howmany(50))


# In[57]:


#Created a List of all the colours 
import statistics
from statistics import mode
from statistics import mean
from statistics import median
bincomShirt=["GREEN","YELLOW","GREEN","BROWN","BLUE","PINK","BLUE","YELLOW","ORANGE","CREAM","ORANGE","RED","WHITE","BLUE","WHITE","BLUE","BLUE","BLUE","GREEN","ARSH","BROWN","GREEN","BROWN","BLUE","BLUE","BLEW","PINK","PINK","ORANGE","ORANGE","RED","WHITE","BLUE","WHITE","WHITE","BLUE","BLUE","BLUE","GREEN","YELLOW","GREEN","BROWN","BLUE","PINK","RED","YELLOW","ORANGE","RED","ORANGE","RED","BLUE","BLUE","WHITE","BLUE","BLUE","WHITE","WHITE","BLUE","BLUE","GREEN","WHITE","BLUE","BROWN","PINK","YELLOW","ORANGE","CREAM","ORANGE","RED","WHITE","BLUE","WHITE","BLUE","BLUE","BLUE","GREEN","GREEN","WHITE","GREEN","BROWN","BLUE","BLUE","BLACK","WHITE","ORANGE","RED","RED","RED","WHITE","BLUE","WHITE","BLUE","BLUE","BLUE","WHITE"]
statistics.mode(bincomShirt)


# In[58]:


statistics.median(bincomShirt)


# In[59]:


#probability of selecting red 
print("The probability of selecting red is",(bincomShirt.count("RED"))/len(bincomShirt))


# In[60]:


# Function to generate a random binary string of length N
import random
def findRandomB():
    num = random.randint(0, 1)
    return num
def generateBinaryString(N):
    S = ""
    for i in range(N):
        x = findRandomB()
        S += str(x)
    print(S,int(S,2))
 
# Driver Code
N = 4
generateBinaryString(N)


# In[61]:


def recSearch(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return recSearch(arr, low, mid - 1, x)
        else:
            return recSearch(arr, mid + 1, high, x)
    else:
        return -1
 
# Test array
arr = [ 56, 36, 47, 19, 90 ]
x = 47
result = recSearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


# In[ ]:




