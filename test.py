#!/usr/bin/env python
# coding: utf-8

# In[ ]:


####  sar_net_output    #######


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


for i in data['sar_net_output']:
    data_list.insert(pos, i)
    pos = pos + 1


# In[6]:


sar_net_output = {}


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
                    list_test = []
                    list_test2 = []
        
                    val2 = test[5]
                    val3 = test[6]
                    
                    list_test.append(val1)
                    list_test2.append(val2)
                    list_test2.append(val3)
                    
                    listFinal = []
                    listFinal.append(list_test)
                    listFinal.append(list_test2)
                    
                    list_final.append(listFinal)
                    
    sar_net_output[key] = list_final  
    
                    
            


# In[8]:


pprint.pprint(sar_net_output)


# In[9]:


####  sar_swap_output    #######


# In[10]:


data_list_1 = []
pos_1 = 0


# In[11]:


for i in data['sar_swap_output']:
    data_list_1.insert(pos_1, i)
    pos_1 = pos_1 + 1


# In[12]:


sar_swap_output = {}


# In[13]:


for i in data_list_1:
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
                    val2 = test[2]
                    val3 = test[3]
                    list_test = []
                    list_test2 = []
                    listFinal = []
                    
                    list_test.append(val1)
                    list_test2.append(val2)
                    list_test2.append(val3)
                    
                    listFinal.append(list_test)
                    listFinal.append(list_test2)
                    
                    list_final.append(listFinal)
                    
    sar_swap_output[key] = list_final  
    
                    
            


# In[14]:


pprint.pprint(sar_swap_output)


# In[ ]:




