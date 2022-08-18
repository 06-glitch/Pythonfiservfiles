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


currentline.pop(0)


# In[5]:


currentline.pop(0)


# In[6]:


currentline.pop(0)


# In[7]:


finalDic = {}


# In[8]:


for i in currentline:
    test = i.split()
    if test[2] == "lo":
        continue
    else:
        time = test[0]
        time = time[1:]
        key = time +" "+test[1]
        
        list_1 = test[2:9]
        list_2 = test[8]
        size = len(list_2)
        list_2 = list_2[:size - 1]
        list_1.append(list_2)
        val = list_1
        finalDic[key] = val


# In[9]:


pprint.pprint(finalDic)


# In[ ]:




