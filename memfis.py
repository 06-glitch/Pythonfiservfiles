#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pprint
import docx


# In[2]:


doc = docx.Document("memfis.docx")


# In[3]:


# with open("memfis.docx", "r") as filestream:
#         for line in filestream:
#             currentline = line.split(",")


# In[4]:


fullText = []
for para in doc.paragraphs:
        fullText.append(para.text)


# In[5]:


for line in fullText:
    currentline = line.split(",")


# In[6]:


# currentline


# In[7]:


currentline.pop(0)


# In[8]:


currentline.pop(0)


# In[9]:


currentline.pop(0)


# In[10]:


finalDic = {}


# In[11]:


for i in currentline:
    test = i.split()
    if test[2] == "lo":
        continue
    else:
        time = test[0]
        time = time[1:]
        key = time +" "+test[1]
        
        list_1 = test[2:len(test)]
        list_2 = test[len(test)-1]
        size = len(list_2)
        list_2 = list_2[:size - 1]
        list_1.append(list_2)
        val = list_1
        finalDic[key] = val


# In[12]:


pprint.pprint(finalDic)


# In[ ]:




