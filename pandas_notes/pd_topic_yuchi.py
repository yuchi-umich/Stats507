# In[1]:
# ## Slide
# Name: Yu Chi
# UM email: yuchi@umich.edu
# In[2]
import pandas as pd
# Question 0

# ## Time Series
# - The topic I picked is Time Series in pandas, specifically about time zone
#  representation.
# - Pandas has simple functionality for performing resampling operations during
#  frequency conversion (e.g., converting secondly data into 5-minutely data).
# - This can be quite helpful in financial applications.
# 
# 
# - First we construct the range and how frequent we want to stamp the time.
# - `rng = pd.date_range("10/17/2021 00:00", periods=5, freq="D")`
# - In this example, the starting time is 00:00 on 10/17/2021, the frequency
#  is one day, and the period is 5 days long.
#  
# 
# - Now we can consstruct the time representation.
# - `ts = pd.Series(np.random.randn(len(rng)), rng)`
# - If we try printing out ts, it should look like the following:
# 
# 
# 

# In[3]:


rng = pd.date_range("10/17/2021 00:00", periods=5, freq="D")
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts)


# - Then we set up the time zone. In this example, I'll set it to UTC
#  (Coordinated Universal Time).
# - `ts_utc = ts.tz_localize("UTC")`
# - If we try printing out ts_utc, it should look like the following:

# In[4]:


ts_utc = ts.tz_localize("UTC")
print(ts_utc)


# - If we want to know what the time is in another time zone, it can easily
#  done as the following:
# - In this example, I want to convert the time to EDT (US Eastern time).
# - `ts_edt = ts_utc.tz_convert("US/Eastern")`
# - Let's try printing out ts_edt:

# In[5]:


ts_edt = ts_utc.tz_convert("US/Eastern")
print(ts_edt)