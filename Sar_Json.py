#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ast
import pprint
import json


# In[2]:


f = open('sar_json-l3pvir1000 (1).json')


# In[3]:


data = json.load(f)


# In[4]:


data_list = []
pos = 0


# In[5]:


for i in data['sar_cpu_output']:
    data_list.insert(pos, i)
    pos = pos + 1


# In[6]:


finalDic = {}


# In[7]:


for i in data_list:
    list_final = []
    for j in i:
        currentline = j.split(",")
        for k in currentline:
            test = k.split()
            if (len(test) > 0):
#                 print(test)
                if(test[0] == 'Linux'):
                    key = test[3]
#                     print(test[3])
                elif(test[3] == "%user"):
                    continue 
                else:
                    time = test[0]
                    time = time[1:]
                    val1 = time +" "+test[1]  
                    val2 = test[len(test)-1]
                    list_test = []
                    
                    list_test.append(val1)
                    list_test.append(val2)
                    
                    list_final.append(list_test)
                    
    finalDic[key] = list_final  
    
                    
            


# In[9]:


pprint.pprint(finalDic)


# In[ ]:




