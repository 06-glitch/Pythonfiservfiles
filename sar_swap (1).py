#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ast
import pprint


# In[2]:


with open("sar_swap..txt", "r") as filestream:
        for line in filestream:
            currentline = line.split(",")


# In[3]:


test = currentline[0].split()
date = test[3]
date = date[2:]


# In[4]:


currentline.pop(0)


# In[5]:


currentline.pop(0)


# In[6]:


currentline.pop(0)


# In[7]:


finalDic = {}


# In[8]:


list_final = []


# In[9]:


for i in currentline:
    test = i.split()
    list_test = []
    i = 0
    if test[2] == "lo":
        continue
    else:
        time = test[0]
        time = time[1:]
        key = time +" "+test[1]
        
        curr = test[len(test)-1]
        curr = curr[:len(curr)-1]
        
        list_test.append(key)
        list_test.append(curr)
        
        list_final.insert(i,list_test)
        i = i + 1


# In[10]:


key = date
val = list_final


# In[11]:


finalDic[key] = val


# In[12]:


pprint.pprint(finalDic)


# In[ ]:




