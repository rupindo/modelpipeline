#!/usr/bin/env python
# coding: utf-8

# In[1]:


import google.auth
from google.cloud import bigquery
client = bigquery.Client()


# In[2]:


import pandas as pd


# In[7]:


credentials, project_id = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])


# In[8]:


bqclient = bigquery.Client(credentials=credentials,project=project_id)


# In[9]:


credentials


# In[10]:


sql = "SELECT * FROM test_data.test"


# In[11]:


df = bqclient.query(sql)


# In[13]:


df = df.result().to_dataframe()


# In[14]:


print(df)

