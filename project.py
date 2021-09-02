#!/usr/bin/env python
# coding: utf-8

# <img src="http://cfs22.simplicdn.net/ice9/new_logo.svgz "/>
# 
# # Project 04: Movielens Dataset Analysis
# 
# You don't need to limit yourself to the number of rows/cells provided. You can add additional rows in each section to add more lines of code.
# 
# **Happy coding!**

# In[1]:


import pandas as pd
import numpy as np
#import skkit as sk


# In[40]:


#	Data acquisition of the movielens dataset     •	users dataset •	rating dataset *	movies datase
users=pd.read_table("E:\\project-movies\\users.dat",engine='python',sep='::')
ratings=pd.read_table("E:\project-movies\\ratings.dat",engine='python',sep='::')
movies=pd.read_csv("E:\project-movies\\movies.dat",sep='::', engine='python')


# In[3]:



users.head() #UserID::Gender::Age::Occupation::Zip-code


# In[4]:


ratings.head() #UserID::MovieID::Rating::Timestamp


# In[41]:


movies.head()  #MovieID::Title::Genres


# In[66]:


#UserID::Gender::Age::Occupation::Zip-code
#Frame=pd.DataFrame([Cov], columns = ["Sequence", "Start", "End", "Coverage"])

users1=pd.DataFrame(data=users,columns=['UserID','Gender','Age','Occupation','Zip-code'])
users1


# In[31]:


d={'col1':[1,2,3,4] ,'col2':['a','s','c','d']}
df=pd.DataFrame(data=d)
df


# In[ ]:





# In[ ]:





# In[ ]:


#	Perform the Exploratory Data Analysis (EDA) for the users dataset
#•	Visualize user age distribution


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




