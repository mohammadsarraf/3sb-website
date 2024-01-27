#!/usr/bin/env python
# coding: utf-8

# # 3 Style Blind

# In[6]:


import pandas as pd
import numpy as np


# In[7]:


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


# In[14]:


path_data = './'

##UF Types
UFtypes = pd.DataFrame()
UFtypes = pd.read_csv("./UF Types.csv")

##UF Comms
UFcomms = pd.DataFrame()
UFcomms = pd.read_csv("./UF Comms.csv")

##UF Types
UFRtypes = pd.DataFrame()
UFRtypes = pd.read_csv("./UFR Types.csv")

##UF Comms
UFRcomms = pd.DataFrame()
UFRcomms = pd.read_csv("./UFR Comms.csv")


# 

# In[16]:


letter = 'I'.upper()
UFRcomms.at[DICT[letter] - 2, "G"]


# In[10]:


def UF_get_cell_value(input_str, dataframeType, dataframeComms):
    result = []
    i = 0
    while i < len(input_str):
        result.append(f"{input_str[i]}{input_str[i+1]}:  {dataframeType.at[DICT[input_str[i+1].upper()] - 2, input_str[i].upper()]} {dataframeComms.at[DICT[input_str[i+1].upper()] - 2, input_str[i].upper()]}")
        i += 2
    return result[:len(result)]


input_str = 'lb xm npps'.replace(" ", "")
value = UF_get_cell_value(input_str, UFtypes, UFcomms)
value


# In[11]:


def UFR_get_cell_value(input_str, dataframeType, dataframeComms):
    result = []
    i = 0
    while i < len(input_str):
        result.append(f"{input_str[i]}{input_str[i+1]}:  {dataframeType.at[DICT[input_str[i+1].upper()] - 2, input_str[i].upper()]} {dataframeComms.at[DICT[input_str[i+1].upper()] - 2, input_str[i].upper()]}")
        i += 2
    return result[:len(result)]


input_str = 'lb'.replace(" ", "")
value = UFR_get_cell_value(input_str, UFRtypes, UFRcomms)
value

