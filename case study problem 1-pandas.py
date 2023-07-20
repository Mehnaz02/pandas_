#!/usr/bin/env python
# coding: utf-8

# Q 1 Write a function that takes start and end of a range returns a Pandas series object containing
# numbers within that range.
# In case the user does not pass start or end or both they should default to 1 and 10 respectively.
# e.g. ->
# range_series() -> Should Return a pandas series from 1 to 10
# range_series(5) -> Should Return a pandas series from 5 to 10
# range_series(5, 10) -> Should Return a pandas series from 5 to 15Create a method that takes n
# numpy arrays of same dimensions sums them and return the answer.
# 

# In[13]:


import pandas as pd
data=pd.Series(range(1,11))


# In[14]:


print(data)


# In[12]:


data1=pd.Series(range(5))


# In[9]:


print(data1)


# In[24]:


import pandas as ps
data2=pd.Series(range(5,11))
data3=pd.Series(range(11,16))


# In[25]:


con=pd.concat([data2,data3])
print(con)


# Q 2 Create a function that takes in two lists named keys and values as arguments.
# Keys would be strings and contain n string values.
# Values would be a list containing n lists.
# The methods should return a new pandas data frame with keys as column names and values as
# their corresponding values
# e.g. ->create_dataframe(["One", "Two"], [["X", "Y"], ["A", "B"]]) -> should return a data frame
# One Two
# 0 X A
# 1 Y B

# In[ ]:


keys={'One':['X','Y'],'Two':['A','B']}
c=pd.DataFrame(keys,index=[0,1])
c


# Create a function that concatenates two dataframes. Use previously created function to create
# two dataframes and pass them as parameters Make sure that the indexes are reset before
# returning

# In[52]:


df1={'One':['X','Y'],'Two':['A','B']}
d1=pd.DataFrame(df1,index=[0,1])
print(d1)
df2={'three':['M','N'],'Four':['O','p']}
d2=pd.DataFrame(df2,index=[0,1,])
print(d2)


# In[54]:


pd.concat([d1,d2])


# Write code to load data from cars.csv into a dataframe and print it's details. Details like: 'count',
# 'mean', 'std', 'min', '25%', '50%', '75%', 'max'

# In[57]:


import pandas as pd

v1=pd.read_csv('/home/mehnaz/Downloads/customer_churn-1.csv')


# In[58]:


print(v1)


# In[60]:


count=v1.count()
print(count)


# In[62]:


mean=v1.mean()
print(mean)


# In[70]:


v1.std()


# In[71]:


minimum=v1.min()
print(minimum)


# In[72]:


v1.describe()


# In[73]:


v1.max()


# Write a method that will take a column name as argument and return the name of the column
# with which the
# given column has the highest correlation.
# The data to be used is the cars dataset.
# The returned value should not the column named that was passed as the parameters.
# E.G: get_max_correlated_column('mpg') -> should return 'drat'

# In[2]:


import pandas as pd
cars=pd.read_csv('/home/mehnaz/Downloads/cars.csv')


# In[3]:


print(cars)


# In[7]:


cars.head()


# In[9]:


cars.info()


# In[11]:


cars2 = cars.drop("model", axis=1)


# In[12]:


cars2.head()


# In[26]:


c = cars2.corr().abs()
s = c.unstack()
print(s)
so = s.sort_values(kind='quicksort')
print(so)


# In[25]:


import numpy as np
cars2['carb'].corr(cars2['drat'])


# In[24]:


cars2.corr()


# In[ ]:





# In[ ]:




