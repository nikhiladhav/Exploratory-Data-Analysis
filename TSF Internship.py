#!/usr/bin/env python
# coding: utf-8

# # NIKHIL RAJU ADHAV 
# **Internship TSF GRIP**
# TASK 3 ,EDA : RETAIL
# DATA SCIENCE AND BUSINESS ANALYTICS
# 
# 

# In[37]:


# importing libraries

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# In[3]:


retail=pd.read_csv('SampleSuperstore.csv')


# # reading and understanding the dataset

# In[16]:


retail


# In[5]:


retail.shape


# In[14]:


retail.head()


# # Exploratory data analysis

# In[13]:


plt.figure(figsize=(16,10))
sns.barplot(x='Sub-Category',y='Sales',data=retail)


# In[14]:


#So,from the above bar graph,we can get to infer ,the sales of which product is low and what to focus on


# In[18]:


plt.figure(figsize=(16,10))
sns.lineplot(x='Sub-Category',y='Profit',data=retail)


# In[6]:


sns.pairplot(retail)


# In[8]:


retail.corr()


# In[11]:


plt.figure(figsize=(8,8))
sns.heatmap(retail.corr(),annot=True,cmap='coolwarm')


# In[31]:


plt.figure(figsize=(7,7))
textprops = {'fontsize':16}
plt.title('Category')
plt.pie(retail['Category'].value_counts(),labels=retail['Category'].value_counts().index,autopct='%1.1f%%',textprops=textprops)
plt.show()


# In[33]:


plt.figure(figsize=(5,5))
textprops = {'fontsize':16}
plt.title('Region')
plt.pie(retail['Region'].value_counts(),labels=retail['Region'].value_counts().index,autopct='%1.1f%%',textprops=textprops)
plt.show()


# In[42]:


retail.groupby('Category')['Profit','Sales'].agg([sum]).plot.bar()


# In[30]:


tcs=retail.groupby('Category').Sales.sum().nlargest(3)
tcp=retail.groupby('Category').Profit.sum().nlargest(3)


# In[31]:


tcs.plot(kind='bar')
tcp.plot(kind='bar',color='red')


# In[8]:


top_subcategory_s=retail.groupby('Sub-Category').Sales.sum()
top_subcategory_p=retail.groupby('Sub-Category').Profit.sum()
#plotting graph
plt.style.use('seaborn')
top_subcategory_s.plot(kind='bar')
top_subcategory_p.plot(kind='bar',color='red')


# In[23]:


statewise=retail.groupby(['Sub-Category'])['Profit'].sum().nlargest(20)
statewise.plot.barh()


# In[35]:


top_states_s=retail.groupby('State').Sales.sum().nlargest(10)
top_states_p=retail.groupby('State').Profit.sum().nlargest(10)
#plotting graph
plt.style.use('seaborn')
top_states_s.plot(kind='bar')
top_states_p.plot(kind='bar',color='red')
plt.xlabel('Top 10 states')
plt.ylabel('Sales/Profit')


# In[56]:


plt.style.use('seaborn')
retail.plot(kind='scatter',x='Sales',y='Profit',c='Discount',s=30,fontsize=15,cmap='viridis')


# With the help of above graphs,we can understand that,if we give more discounts,sales will increase but there is a fall in our profit.
# 

# # Some Conclusions we can draw 

# 1. We should limit sales of furniture and increase that of technology and office supplies as the profit in furniture is very less as compared to sales
# 
# 2.While taking consideration of sub-categories, the production of tables should be minimised
# 
# 3.Increase sales more in the east as profit is more
# 
# 4.We should concentrate on states like New York, California to make more profits.

# In[ ]:




