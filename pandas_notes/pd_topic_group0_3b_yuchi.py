#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---


# ## Topics in Pandas
# **Stats 507, Fall 2021**
# 
# 
# ## Contents
# Add a bullet for each topic and link to the level 2 title header using
# the exact title with spaces replaced by a dash.
# 
# + [Topic Title](#Topic-Title)
# + [Topic 2 Title](#Topic-2-Title)
# 
# ## Topic Title
# Include a title slide with a short title for your content.
# Write your name in *bold* on your title slide.
# 
# ## Pandas Topic- Windows operations.
# *Tiejin Chen*; **tiejin@umich.edu**
# Here we choose windows operations(```rolling```) as our topic.
# First, we import all the module we need

# In[1]:


import numpy as np
import pandas as pd


# ## Windows operation
# - In the region of data science, sometimes we need to manipulate
# one raw with two raws next to it for every raw.
# - this is one kind of windows operation.
# - We define windows operation as an operation that
# performs an aggregation over a sliding partition of values (from pandas' userguide)
# - Using ```df.rolling``` function to use the normal windows operation

# In[2]:


rng = np.random.default_rng(9 * 2021 * 20)
n=5
a = rng.binomial(n=1, p=0.5, size=n)
b = 1 - 0.5 * a + rng.normal(size=n)
c = 0.8 * a + rng.normal(size=n)
df = pd.DataFrame({'a': a, 'b': b, 'c': c})
print(df)
df['b'].rolling(window=2).sum()


# ## Rolling parameter
# In ```rolling``` method, we have some parameter to control the method, And we introduce two:
# - center: Type bool; if center is True, Then the result will move to the center in series.
# - window: decide the length of window or the customed window

# In[3]:


df['b'].rolling(window=3).sum()

df['b'].rolling(window=3,center=True).sum()

df['b'].rolling(window=2).sum()


# +
# example of customed window

# In[4]:


window_custom = [True,False,True,False,True]
from pandas.api.indexers import BaseIndexer
class CustomIndexer(BaseIndexer):
    def get_window_bounds(self, num_values, min_periods, center, closed):
        start = np.empty(num_values, dtype=np.int64)
        end = np.empty(num_values, dtype=np.int64)
        for i in range(num_values):
            if self.use_expanding[i]:
                start[i] = 0
                end[i] = i + 1
            else:
                start[i] = i
                end[i] = i + self.window_size
        return start, end
indexer1 = CustomIndexer(window_size=1, use_expanding=window_custom)
indexer2 = CustomIndexer(window_size=2, use_expanding=window_custom)

df['b'].rolling(window=indexer1).sum()
df['b'].rolling(window=indexer2).sum()


# ## Windows operation with groupby
# - ```pandas.groupby``` type also have windows operation method,
# Hence we can combine groupby and windows operation.
# - we can also use ```apply``` after we use ```rolling```

# In[5]:


df.groupby('a').rolling(window=2).sum()


def test_mean(x):
    return x.mean()
df['b'].rolling(window=2).apply(test_mean)


# In[ ]:


# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---


# Sean Kelly, seankell@umich.edu
# 
# ## Topics in Pandas
# **Stats 507, Fall 2021**   
# 
# ## Contents
# 
# + [Pandas Idiom: Splitting](#Pandas-Idiom:-Splitting) 
# + [Splitting to analyze data](#Splitting-to-analyze-data)
# + [Splitting to create new Series](#Splitting-to-create-new-Series)
# + [Takeaways](#Takeaways)
# 
# # Imports

# In[6]:


import numpy as np
import pandas as pd


# ## Pandas Idiom: Splitting
# 
# - A useful way to utilize data is by accessing individual rows or groups of 
# rows and operating only on those rows or groups.  
# - A common way to access rows is indexing using the `loc` or `iloc` methods 
# of the dataframe. This is useful when you know what row indices you'd like to
# access.  
# - However, it is often required to subset a given data set based on some 
# criteria that we want each row of the subset to meet.  
# - We will look at selecting subsets of rows by splitting data based on row 
# values and performing analysis or calculations after splitting.
# 
# ## Splitting to analyze data
# 
# - Using data splitting makes it simple to create new dataframes representing 
# subsets of the initial dataframes
# - Find the average of one column of a group defined by another column

# In[7]:


t_df = pd.DataFrame(
    {"col0":np.random.normal(size=10),
     "col1":np.random.normal(loc=10,scale=100,size=10),
     "col2":np.random.uniform(size=10)}
    )
t_below_average_col1 = t_df[t_df["col1"] < 10]
t_above_average_col1 = t_df[t_df["col1"] >= 10]
print([np.round(t_above_average_col1["col0"].mean(),4),
      np.round(t_below_average_col1["col0"].mean(),4)])


# ## Splitting to create new Series
# 
# - We can use this splitting method to convert columns to booleans based on 
# a criterion we want that column to meet, such as converting a continuous 
# random variable to a bernoulli outcome with some probability p.

# In[8]:


p = 0.4
t_df["col0_below_p"] = t_df["col2"] < p
t_df


# ## Takeaways
# 
# - Splitting is a powerful but simple idiom that allows easy grouping of data
# for analysis and further calculations.  
# - There are many ways to access specific rows of your data, but it is
# important to use the right tool for the job.  
# - More information on splitting can be found [here][splitting].  
# 
# [splitting]: https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#splitting

# In[ ]:


# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---


# ## Slide
# Name: Yu Chi
# UM email: yuchi@umich.edu

# In[9]:


import pandas as pd


# ## Time Series
# - The topic I picked is Time Series in pandas, specifically about time zone
#  representation.
# - Pandas has simple functionality for performing resampling operations during
#  frequency conversion (e.g., converting secondly data into 5-minutely data).
# - This can be quite helpful in financial applications.
# 
# - First we construct the range and how frequent we want to stamp the time.
# - `rng = pd.date_range("10/17/2021 00:00", periods=5, freq="D")`
# - In this example, the starting time is 00:00 on 10/17/2021, the frequency
#  is one day, and the period is 5 days long.
# - Now we can consstruct the time representation.
# - `ts = pd.Series(np.random.randn(len(rng)), rng)`
# - If we try printing out ts, it should look like the following:
# 

# In[10]:


rng = pd.date_range("10/17/2021 00:00", periods=5, freq="D")
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts)


# - Then we set up the time zone. In this example, I'll set it to UTC
#  (Coordinated Universal Time).
# - `ts_utc = ts.tz_localize("UTC")`
# - If we try printing out ts_utc, it should look like the following:

# In[11]:


ts_utc = ts.tz_localize("UTC")
print(ts_utc)


# - If we want to know what the time is in another time zone, it can easily
#  done as the following:
# - In this example, I want to convert the time to EDT (US Eastern time).
# - `ts_edt = ts_utc.tz_convert("US/Eastern")`
# - Let's try printing out ts_edt:

# In[12]:


ts_edt = ts_utc.tz_convert("US/Eastern")
print(ts_edt)

