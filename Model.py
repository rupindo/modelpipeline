#!/usr/bin/env python
# coding: utf-8

# In[2]:


import google.auth
from google.cloud import bigquery
client = bigquery.Client()


# In[14]:


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle


# In[3]:


credentials, project_id = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])


# In[4]:


bqclient = bigquery.Client(credentials=credentials,project=project_id)


# In[5]:


sql = "SELECT * FROM test_data.test"


# In[6]:


df = bqclient.query(sql)


# In[7]:


df = df.result().to_dataframe()


# In[9]:


x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])


# In[10]:


model = LinearRegression()


# In[11]:


model.fit(x, y)


# In[12]:


r_sq = model.score(x, y)


# In[ ]:


pickle.dump(model, open('model.sav', 'wb'))

