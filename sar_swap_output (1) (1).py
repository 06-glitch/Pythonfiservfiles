#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ast
import pprint
import json


# In[2]:


f = open('sar_json-l3pvir1000 (1).json')
data = json.load(f)


# In[3]:


data_list_1 = []
pos_1 = 0


# In[4]:


for i in data['sar_swap_output']:
    data_list_1.insert(pos_1, i)
    pos_1 = pos_1 + 1


# In[5]:


###########   kbswpfree  #####################


# In[6]:


sar_swap_output = {}


# In[7]:


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
                elif(test[2] == 'kbswpfree'):
                    continue
                elif(test[0].find('Average') >= 0):
                    continue 
                else:
                    time = test[0]
                    val1 = time +" "+test[1]  
                    val2 = test[2]
                    val3 = test[3]
                    list_test = []
                    
                    list_test.append(val1)
                    list_test.append(val2)
#                     list_test.append(val3)
                    
                    list_final.append(list_test)
                    
    sar_swap_output[key] = list_final  
    
                    
            


# In[8]:


pprint.pprint(sar_swap_output)


# In[9]:


###########   kbswpused  #####################


# In[10]:


sar_swap_output_2 = {}


# In[11]:


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
                elif(test[3] == 'kbswpused'):
                    continue 
                elif(test[0].find('Average') >= 0):
                    continue 
                else:
                    time = test[0]
                    val1 = time +" "+test[1]  
                    val2 = test[2]
                    val3 = test[3]
                    list_test = []
                    
                    list_test.append(val1)
#                     list_test.append(val2)
                    list_test.append(val3)
                    
                    list_final.append(list_test)
                    
    sar_swap_output_2[key] = list_final  
    
                    
            


# In[12]:


pprint.pprint(sar_swap_output_2)

