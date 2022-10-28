#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq
trends=TrendReq()


# In[2]:


get_ipython().system('pip install pytrends')


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq
trends=TrendReq()


# In[4]:


#create a DataFrame of the top 10 countries which search for “Machine Learning” on Google
trends.build_payload(kw_list=["Machine Learning"])
data=trends.interest_by_region()
data=data.sort_values(by='Machine Learning',ascending=False)
data=data.head(10)
data


# In[5]:


data.reset_index().plot(x='geoName', y='Machine Learning', figsize=(20,15),kind='bar')
plt.style.use('fivethirtyeight')
plt.show()


# In[8]:


data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=['Machine Learning'])
data=data.interest_over_time()
fig, ax=plt.subplots(figsize=(20,15))
data['Machine Learning'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches for Machine Learning', fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()


# In[ ]:




