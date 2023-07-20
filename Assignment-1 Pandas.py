#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Start off by importing the customer_churn.csv file in the jupyter notebook and store that in churn data
frame


# In[3]:


import pandas as pd

v=pd.read_csv('/home/mehnaz/Downloads/customer_churn-1.csv')


# In[9]:


v


# In[12]:


# From the churn data frame, select only 3rd, 7th, 9th, and 20th columns and all the rows and store that in new
#data frame named newCols.
newCols=(v.iloc[:,2:3])&(v.iloc[:,6:7])&(v.iloc[:,8:9])&(v.iloc[:,20:])
print(newCols)


# In[16]:


#From the original data frame, select only the rows from 200th index till 1000th index(inclusive) column.

v.iloc[200:1001,:]


# In[19]:


# Now select the rows from 20th index till 200th index(exclusive),and columns from 2nd index till 15th index
#value.

v.iloc[20:200,2:15]


# In[21]:


# Display the top 100 records from the original data frame.

v.head(100)


# In[22]:


# Display the last 10 records from the data frame.

v.tail(10)


# In[24]:


# Now from the churn data frame, try to sort the data by the tenure column according to the descending
#order

v.sort_values(by='tenure', ascending=False)


# In[38]:


#Fetch all the records that are satisfying the following condition:
#a. Tenure>50 and the gender as ‘Female’.
#b. Gender as ‘Male’ and SeniorCitizen as 0.
#c. TechSupport as ‘Yes’ and Churn as ‘No’.
#d. Contract type as ‘Month-to-month’ and Churn as ‘Yes’.

(v.tenure>50)&(v.gender=='Female')


# In[37]:


(v.gender=='Male')&(v.SeniorCitizen ==0)


# In[40]:


#c. TechSupport as ‘Yes’ and Churn as ‘No’.

(v.TechSupport =='Yes')&(v.Churn=='No')


# In[41]:


#d. Contract type as ‘Month-to-month’ and Churn as ‘Yes’.

(v.Contract=='Month-to-month')&(v.Churn=='Yes')


# In[10]:


#Use a for loop to calculate the number of customers that are getting the tech support and are male senior citizen.



# In[17]:


import pandas as pd

v=pd.read_csv('/home/mehnaz/Downloads/customer_churn-1.csv')
cust=0
for i in range(7043):
    if (v.loc[i,'gender']=='Male' and v.loc[i,'SeniorCitizen']==1 and v.loc[i,'TechSupport']=='Yes'):
        cust=cust+1
print(cust)


# In[15]:


v

