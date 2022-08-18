#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open("sar_swap..txt", "r") as filestream:
        for line in filestream:
            currentline = line.split(",")


# In[2]:


currentline


# In[3]:


currentline.pop(0)


# In[4]:


currentline.pop(0)


# In[5]:


currentline.pop(0)


# In[6]:


finalDic = {}


# In[7]:


for i in currentline:
    test = i.split()
    if test[2] == "lo":
        continue 
    else:
        key = test[0] +" "+test[1]
        val = test[2:]
        finalDic[key] = val


# In[8]:


finalDic


# In[ ]:




