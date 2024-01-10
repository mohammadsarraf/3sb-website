#!/usr/bin/env python
# coding: utf-8

# # 3 Style Blind

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


DICT = \
{
    'A': 2, 'B': 3, 'C': 4, 'D': 5, 'E': 6, 'F': 7, 'G': 8, 'H': 9, 'I': 10, 
    'J': 11,'K': 12, 'L': 13, 'M': 14, 'N': 15, 'O': 16, 'P': 17, 'Q': 18, 
    'R': 19, 'S': 20, 'T': 21, 'U': 22, 'V': 23, 'W': 24, 'X': 25
}   

DICT_key = \
{
    2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E', 7: 'F', 8: 'G', 9: 'H', 10: 'I', 
    11: 'J', 12: 'K', 13: 'L', 14: 'M', 15: 'N', 16: 'O', 17: 'P', 18: 'Q', 
    19: 'R', 20: 'S', 21: 'T', 22: 'U', 23: 'V', 24: 'W', 25: 'X'
}

values = "abcdefghijklmnopqrstuvwx".upper()
# values[23]


# In[7]:


path_data = './'

##UF Types
types = pd.DataFrame()
types = pd.read_csv("./UF Types.csv")

##UF Comms
comms = pd.DataFrame()
comms = pd.read_csv("./UF Comms.csv")


# 

# In[8]:


letter = 'J'.upper()
comms.at[DICT[letter] - 2, "F"]


# In[14]:


def get_cell_value(input_str, dataframeType, dataframeComms):
    result = []
    i = 0
    while i < len(input_str):
        result.append(f"{input_str[i]}{input_str[i+1]}:  {dataframeType.at[DICT[input_str[i+1].upper()] - 2, input_str[i].upper()]} {dataframeComms.at[DICT[input_str[i+1].upper()] - 2, input_str[i].upper()]}")
        i += 2
    return result[:len(result)]


input_str = 'mx xm npps'.replace(" ", "")
value = get_cell_value(input_str, types, comms)
value

