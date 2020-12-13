#!/usr/bin/env python
# coding: utf-8

# Reverse Indexing in list

# In[1]:


i = [1,2,3,4,4,3]


# In[2]:


i[-1]


# Add something in list

# In[3]:


i.append('hi')


# In[4]:


i


# Array mst have homogenous element where as list hae hetrogenous elements

# In[5]:


l2 = ['áli','sara','kahn','muheeb']


# Mix to lists

# In[7]:


l2.extend(i)


# In[8]:


i


# In[10]:


l2


# Remove Specific Character but its first ocuurence only

# In[11]:


l2.remove(3)


# In[18]:


l2


# Remove from last or from any index

# In[19]:


l2.pop()


# list comprehention

# In[20]:


l1 = [1,1,2,4,3,9,7,5,1,11,2,44]


# In[33]:


def iseven(el):
    return el % 2 == 0
oddl1 = [el for el in l1 if el % 2 != 0]


# In[34]:


oddl1


# In[42]:


def square1(el):
    return el * el
oddl1sqaure = [square1(i) for i in oddl1]


# In[43]:


oddl1sqaure


# List are copy by refrence

# In[46]:


l1 = [1,2,3,4,5]
l2 = l1
print(l1)
l2.append(5)
print(l1)
print(l2)


# Solution of the problem

# In[48]:


l3 = l1.copy()


# In[49]:


l3


# Chunks slicing

# In[55]:


# refrence [initial : final-1 : steps]
l3[1:5]


# In[63]:


l3[0:4:1]


# In[65]:


l3[::2]


# Class activity <br>
# give last twoo elements <br> 
# write the function to skil  elements from start and end

# In[68]:


l = [2,2,3,4,5,6,3,42,53,542,22,22]
len(l)


# Tuples <br>
# Not mutable

# In[69]:


a = (1,2,3,5)
b = (5,3,2,4)


# In[70]:


a[1]


# In[71]:


a[1] = 34


# Remove white spaces

# In[74]:


st = "     \n\n\n\n shahab bukhari \n\n   "


# In[75]:


st


# In[76]:


print(st)


# In[79]:


st = st.replace("\n",'')


# In[80]:


st


# In[82]:


st.replace(' ','')


# In[84]:


st2 = "     \n\n\n\n shahab bukhari \n\n   "
st2


# In[86]:


st2.strip()


# In[87]:


'shahab' in st2


# <h3>Palindrom Example</h3>

# In[91]:


l1 = [5,4,3,2,1]


# In[93]:


l1[::-1]


# In[97]:


'madam' == 'madam'[::-1]


# dictionary

# In[103]:


dic = {
    'Islamabad': 'Nust',
    'karachi': 'NED',
    'lahore': 'Uet'
}
print(dic.keys())
print(dic.items())
print(dic.get('karachi','not found'))
print(dic.get('faislabad','not found'))
print(dic.get('lahore','not found'))


# In[ ]:




