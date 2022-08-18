#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open("sar_net.txt", "r") as filestream:
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


currentline[1].split()


# In[7]:


finalDic = {}


# In[8]:


for i in currentline:
    test = i.split()
    print(test[2])
    if test[2] == "lo":
        continue 
    else:
        key = test[0] +" "+test[1]
        val = test[2:]
        finalDic[key] = val


# In[9]:


finalDic


# In[ ]:




