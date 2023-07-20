#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[9]:


#type the following code to create a pandas dataframe using an array
import numpy as np

arr=np.array([1,2,3,4,5])
df1=pd.DataFrame(arr)
df1


# In[7]:


#Type the following code to create a pandas dataframe using an 2d array.

df2=pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10]])
df2


# In[11]:


#type the following code to create a pandas dataframe using a dictionary.

dfd=pd.DataFrame({"Fruits":['apple','banana','mango','grapes'],'Cost':[100,200,320,145]})
dfd


# #type the following code to create a pandas dataframe by importing data from a csv file.
# 
# dfim=pd.read_csv('home/mehnaz/Desktop/intellipaat/python/module5')
# dfim
