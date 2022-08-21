#!/usr/bin/env python
# coding: utf-8

# In[1]:


####  sar_net_output    #######


# In[2]:


####  eth0    #######


# In[3]:


import ast
import pprint
import json


# In[4]:


f = open('sar_json-l3pvir1000 (1).json')


# In[5]:


data = json.load(f)


# In[6]:


data_list = []
pos = 0


# In[7]:


for i in data['sar_net_output']:
    data_list.insert(pos, i)
    pos = pos + 1


# In[8]:


sar_net_output = {}
sar_net_output_2 = {}


# In[9]:


for i in data_list:
    list_final = []
    list_final_2 = []
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
                elif(test[2] == 'IFACE'):
                    continue 
                elif(test[2] == 'eth0'):
                    time = test[0]
                    val1 = time +" "+test[1]
                    list_test = []
                    list_test_2 = []
        
                    val2 = test[5]
                    val3 = test[6]
                    
                    list_test.append(val1)
                    list_test.append(val2)
                    
                    list_test_2.append(val1)
                    list_test_2.append(val3)
                    
                    list_final.append(list_test)
                    list_final_2.append(list_test_2)
                    
    sar_net_output[key] = list_final  
    sar_net_output_2[key] = list_final_2  
    
                    
            


# In[10]:


pprint.pprint(sar_net_output)


# In[11]:


pprint.pprint(sar_net_output_2)


# In[12]:


# *************** eht1 *********************


# In[13]:


sar_net_output_eht1 = {}
sar_net_output_eht1_2 = {}


# In[14]:


for i in data_list:
    list_final = []
    list_final_2 = []
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
                elif(test[2] == 'IFACE'):
                    continue 
                elif(test[2] == 'eth1'):
                    time = test[0]
                    val1 = time +" "+test[1]
                    list_test = []
                    list_test_2 = []
        
                    val2 = test[5]
                    val3 = test[6]
                    
                    list_test.append(val1)
                    list_test.append(val2)
                    
                    list_test_2.append(val1)
                    list_test_2.append(val3)
                    
                    list_final.append(list_test)
                    list_final_2.append(list_test_2)
                    
    sar_net_output_eht1[key] = list_final  
    sar_net_output_eht1_2[key] = list_final_2  
    
                    
            


# In[15]:


pprint.pprint(sar_net_output_eht1)


# In[16]:


pprint.pprint(sar_net_output_eht1_2)


# In[ ]:




