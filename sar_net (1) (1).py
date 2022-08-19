#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pprint


# In[2]:


with open("sar_net.txt", "r") as filestream:
        for line in filestream:
            currentline = line.split(",")


# In[3]:


# currentline


# In[4]:


test = currentline[0].split()
date = test[3]
date = date[2:]


# In[5]:


currentline.pop(0)


# In[6]:


currentline.pop(0)


# In[7]:


currentline.pop(0)


# In[8]:


finalDic = {}


# In[9]:


list_final = []


# In[10]:


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


# In[11]:


key = date
val = list_final


# In[12]:


finalDic[key] = val


# In[13]:


pprint.pprint(finalDic)


# In[ ]:




