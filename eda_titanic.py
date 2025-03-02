#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


import pandas as pd


# In[5]:


import seaborn as sns


# In[7]:


import matplotlib.pyplot as plt


# In[9]:


titanic= sns.load_dataset('titanic')


# In[11]:


titanic.head()


# In[13]:


titanic.isnull().sum()


# In[15]:


titanic['age'].fillna(titanic['age'].median(), inplace=True)


# In[19]:


titanic.drop(columns=['deck'], inplace=True)


# In[21]:


titanic.head()


# In[29]:


sns.countplot(x='alive' ,data =titanic, palette='coolwarm')
plt.title("count of survived")
plt.show()


# In[31]:


sns.barplot(x='sex', y='alive', data=titanic, palette='pastel')
plt.title("Survival Rate by Gender")
plt.show()


# In[45]:


sns.barplot(x='class', y='alive', data=titanic, palette='pastel')
plt.title("Survival Rate by class")
plt.show()


# In[37]:


sns.histplot(titanic['age'], bins=30, kde=True)
plt.title("Age Distribution")
plt.show()


# In[43]:


plt.figure(figsize=(10, 6))
sns.heatmap(titanic.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()


# In[ ]:




