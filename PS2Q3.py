# Question 3

# a.

# In[32]:


'''Imports the data from the website.'''
df_demo_11_12 = pd.read_sas(
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DEMO_G.XPT", format='xport')
df_demo_13_14 = pd.read_sas(
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DEMO_H.XPT", format='xport')
df_demo_15_16 = pd.read_sas(
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.XPT", format='xport')
df_demo_17_18 = pd.read_sas(
    "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.XPT", format='xport')


# In[33]:


'''Extracts the columns from the data.'''
df_demo_11_12_extracted = df_demo_11_12[['SEQN', 'RIDAGEYR', 'RIDRETH3', 
    'DMDEDUC2', 'DMDMARTL', 'RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR',
    'WTINT2YR']]
df_demo_13_14_extracted = df_demo_13_14[['SEQN', 'RIDAGEYR', 'RIDRETH3',
    'DMDEDUC2', 'DMDMARTL', 'RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR',
    'WTINT2YR']]
df_demo_15_16_extracted = df_demo_15_16[['SEQN', 'RIDAGEYR', 'RIDRETH3',
    'DMDEDUC2', 'DMDMARTL', 'RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR',
    'WTINT2YR']]
df_demo_17_18_extracted = df_demo_17_18[['SEQN', 'RIDAGEYR', 'RIDRETH3',
    'DMDEDUC2', 'DMDMARTL', 'RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR',
    'WTINT2YR']]


# In[34]:


'''Inserts the column indicating the corresponding cohort.'''
df_demo_11_12_extracted.insert(0, 'cohort', '2011-2012')
df_demo_13_14_extracted.insert(0, 'cohort', '2013-2014')
df_demo_15_16_extracted.insert(0, 'cohort', '2015-2016')
df_demo_17_18_extracted.insert(0, 'cohort', '2017-2018')


# In[35]:


'''Combines the four dataframes.'''
df_demo = pd.concat([df_demo_11_12_extracted, df_demo_13_14_extracted, 
    df_demo_15_16_extracted, df_demo_17_18_extracted])


# In[36]:


'''Renames the columns into iterate variable names.'''
df_demo.rename(columns={'SEQN': 'unique ids', 'RIDAGEYR': 'age', 
    'RIDRETH3': 'race and ethnicity', 'DMDEDUC2': 'education', 
    'DMDMARTL': 'marital status', 'RIDSTATR': 'interview/examination status',
    'SDMVPSU': 'masked variance pseudo-psu',
    'SDMVSTRA': 'masked variance pseudo-stratum',
    'WTMEC2YR': 'full sample 2 year mec exam weight',
    'WTINT2YR': 'full sample 2 year interview weight'}, inplace=True)


# In[37]:


'''Converts each column to an appropriate type.'''
df_demo.astype({'unique ids': int, 'age': int})


# In[38]:


df_demo['race and ethnicity'].replace({1: 'Mexican American',
    2: 'Other Hispanic', 3: 'non-Hispanic white', 4: 'non-Hispanic black',
    6: 'non-Hispanic Asian', 7: 'other non-Hispanic races'}, inplace=True)
df_demo['education'].replace({1: 'less than 9th grade', 2: '9-11th grade',
    3: 'High school graduate/GED or equivalent',
    4: 'Some college or AA degree', 5: 'College graduate or above',
    7: 'Refused', 9: 'Dont know'}, inplace=True)
df_demo['marital status'].replace({1: 'Married', 2: 'Widowed', 3: 'Divorced',
    4: 'Separated', 5: 'Never married', 6: 'Living with partner',
    77: 'Refused', 99: 'Dont know'}, inplace=True)
df_demo['interview/examination status'].replace({1: 'Interviewed only',
    2: 'Both interviewed and MEC examined'}, inplace=True)
df_demo.replace({'NaN': -1}, inplace=True)
df_demo.reset_index(drop=True)


# In[39]:


'''Saves the dataframe to pickle format.'''
df_demo.to_pickle('df_demo.pkl')


# b.

# In[40]:


'''Imports the data from the website.'''
df_ohxden_11_12 = pd.read_sas(
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/OHXDEN_G.XPT",
    format='xport')
df_ohxden_13_14 = pd.read_sas(
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/OHXDEN_H.XPT",
    format='xport')
df_ohxden_15_16 = pd.read_sas(
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/OHXDEN_I.XPT",
    format='xport')
df_ohxden_17_18 = pd.read_sas(
    "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/OHXDEN_J.XPT",
    format='xport')


# In[41]:


'''Extracts the columns from the data.'''
df_ohxden_11_12_extracted = df_ohxden_11_12[['SEQN', 'OHDDESTS', 'OHX01TC',
    'OHX02TC', 'OHX03TC', 'OHX04TC', 'OHX05TC', 'OHX06TC', 'OHX07TC',
    'OHX08TC', 'OHX09TC', 'OHX10TC', 'OHX11TC', 'OHX12TC', 'OHX13TC',
    'OHX14TC', 'OHX15TC', 'OHX16TC', 'OHX17TC', 'OHX18TC', 'OHX19TC',
    'OHX20TC', 'OHX21TC', 'OHX22TC', 'OHX23TC', 'OHX24TC', 'OHX25TC',
    'OHX26TC', 'OHX27TC', 'OHX28TC', 'OHX29TC', 'OHX30TC', 'OHX31TC', 
    'OHX32TC', 'OHX02CTC', 'OHX03CTC', 'OHX04CTC', 'OHX05CTC', 'OHX06CTC',
    'OHX07CTC', 'OHX08CTC', 'OHX09CTC', 'OHX10CTC', 'OHX11CTC', 'OHX12CTC',
    'OHX13CTC', 'OHX14CTC', 'OHX15CTC', 'OHX18CTC', 'OHX19CTC', 'OHX20CTC',
    'OHX21CTC', 'OHX22CTC', 'OHX23CTC', 'OHX24CTC', 'OHX25CTC', 'OHX26CTC',
    'OHX27CTC', 'OHX28CTC', 'OHX29CTC', 'OHX30CTC', 'OHX31CTC']]
df_ohxden_13_14_extracted = df_ohxden_13_14[['SEQN', 'OHDDESTS', 'OHX01TC',
    'OHX02TC', 'OHX03TC', 'OHX04TC', 'OHX05TC', 'OHX06TC', 'OHX07TC',
    'OHX08TC', 'OHX09TC', 'OHX10TC', 'OHX11TC', 'OHX12TC', 'OHX13TC',
    'OHX14TC', 'OHX15TC', 'OHX16TC', 'OHX17TC', 'OHX18TC', 'OHX19TC',
    'OHX20TC', 'OHX21TC', 'OHX22TC', 'OHX23TC', 'OHX24TC', 'OHX25TC',
    'OHX26TC', 'OHX27TC', 'OHX28TC', 'OHX29TC', 'OHX30TC', 'OHX31TC',
    'OHX32TC', 'OHX02CTC', 'OHX03CTC', 'OHX04CTC', 'OHX05CTC', 'OHX06CTC',
    'OHX07CTC', 'OHX08CTC', 'OHX09CTC', 'OHX10CTC', 'OHX11CTC', 'OHX12CTC',
    'OHX13CTC', 'OHX14CTC', 'OHX15CTC', 'OHX18CTC', 'OHX19CTC', 'OHX20CTC',
    'OHX21CTC', 'OHX22CTC', 'OHX23CTC', 'OHX24CTC', 'OHX25CTC', 'OHX26CTC',
    'OHX27CTC', 'OHX28CTC', 'OHX29CTC', 'OHX30CTC', 'OHX31CTC']]
df_ohxden_15_16_extracted = df_ohxden_15_16[['SEQN', 'OHDDESTS', 'OHX01TC',
    'OHX02TC', 'OHX03TC', 'OHX04TC', 'OHX05TC', 'OHX06TC', 'OHX07TC',
    'OHX08TC', 'OHX09TC', 'OHX10TC', 'OHX11TC', 'OHX12TC', 'OHX13TC',
    'OHX14TC', 'OHX15TC', 'OHX16TC', 'OHX17TC', 'OHX18TC', 'OHX19TC',
    'OHX20TC', 'OHX21TC', 'OHX22TC', 'OHX23TC', 'OHX24TC', 'OHX25TC',
    'OHX26TC', 'OHX27TC', 'OHX28TC', 'OHX29TC', 'OHX30TC', 'OHX31TC',
    'OHX32TC', 'OHX02CTC', 'OHX03CTC', 'OHX04CTC', 'OHX05CTC', 'OHX06CTC',
    'OHX07CTC', 'OHX08CTC', 'OHX09CTC', 'OHX10CTC', 'OHX11CTC', 'OHX12CTC',
    'OHX13CTC', 'OHX14CTC', 'OHX15CTC', 'OHX18CTC', 'OHX19CTC', 'OHX20CTC',
    'OHX21CTC', 'OHX22CTC', 'OHX23CTC', 'OHX24CTC', 'OHX25CTC', 'OHX26CTC',
    'OHX27CTC', 'OHX28CTC', 'OHX29CTC', 'OHX30CTC', 'OHX31CTC']]
df_ohxden_17_18_extracted = df_ohxden_17_18[['SEQN', 'OHDDESTS', 'OHX01TC',
    'OHX02TC', 'OHX03TC', 'OHX04TC', 'OHX05TC', 'OHX06TC', 'OHX07TC',
    'OHX08TC', 'OHX09TC', 'OHX10TC', 'OHX11TC', 'OHX12TC', 'OHX13TC',
    'OHX14TC', 'OHX15TC', 'OHX16TC', 'OHX17TC', 'OHX18TC', 'OHX19TC',
    'OHX20TC', 'OHX21TC', 'OHX22TC', 'OHX23TC', 'OHX24TC', 'OHX25TC',
    'OHX26TC', 'OHX27TC', 'OHX28TC', 'OHX29TC', 'OHX30TC', 'OHX31TC',
    'OHX32TC', 'OHX02CTC', 'OHX03CTC', 'OHX04CTC', 'OHX05CTC', 'OHX06CTC',
    'OHX07CTC', 'OHX08CTC', 'OHX09CTC', 'OHX10CTC', 'OHX11CTC', 'OHX12CTC',
    'OHX13CTC', 'OHX14CTC', 'OHX15CTC', 'OHX18CTC', 'OHX19CTC', 'OHX20CTC',
    'OHX21CTC', 'OHX22CTC', 'OHX23CTC', 'OHX24CTC', 'OHX25CTC', 'OHX26CTC',
    'OHX27CTC', 'OHX28CTC', 'OHX29CTC', 'OHX30CTC', 'OHX31CTC']]


# In[42]:


'''Inserts the column indicating the corresponding cohort.'''
df_ohxden_11_12_extracted.insert(0, 'cohort', '2011-2012')
df_ohxden_13_14_extracted.insert(0, 'cohort', '2013-2014')
df_ohxden_15_16_extracted.insert(0, 'cohort', '2015-2016')
df_ohxden_17_18_extracted.insert(0, 'cohort', '2017-2018')


# In[43]:


'''Combines the four dataframes.'''
df_ohxden = pd.concat([df_ohxden_11_12_extracted, df_ohxden_13_14_extracted,
    df_ohxden_15_16_extracted, df_ohxden_17_18_extracted])


# In[44]:


'''Renames the columns into iterate variable names.'''
df_ohxden.rename(columns={'SEQN': 'unique ids',
    'OHDDESTS': 'dentition status code', 'OHX01TC': 'tooth count #1',
    'OHX02TC': 'tooth count #2', 'OHX03TC': 'tooth count #3',
    'OHX04TC': 'tooth count #4', 'OHX05TC': 'tooth count #5',
    'OHX06TC': 'tooth count #6', 'OHX07TC': 'tooth count #7',
    'OHX08TC': 'tooth count #8', 'OHX09TC': 'tooth count #9',
    'OHX10TC': 'tooth count #10', 'OHX11TC': 'tooth count #11',
    'OHX12TC': 'tooth count #12', 'OHX13TC': 'tooth count #13',
    'OHX14TC': 'tooth count #14', 'OHX15TC': 'tooth count #15',
    'OHX16TC': 'tooth count #16', 'OHX17TC': 'tooth count #17',
    'OHX18TC': 'tooth count #18', 'OHX19TC': 'tooth count #19',
    'OHX20TC': 'tooth count #20', 'OHX21TC': 'tooth count #21',
    'OHX22TC': 'tooth count #22', 'OHX23TC': 'tooth count #23',
    'OHX24TC': 'tooth count #24', 'OHX25TC': 'tooth count #25',
    'OHX26TC': 'tooth count #26', 'OHX27TC': 'tooth count #27',
    'OHX28TC': 'tooth count #28', 'OHX29TC': 'tooth count #29',
    'OHX30TC': 'tooth count #30', 'OHX31TC': 'tooth count #31',
    'OHX32TC': 'tooth count #32', 'OHX02CTC': 'coronal caries tooth count #2',
    'OHX03CTC': 'coronal caries tooth count #3',
    'OHX04CTC': 'coronal caries tooth count #4',
    'OHX05CTC': 'coronal caries tooth count #5',
    'OHX06CTC': 'coronal caries tooth count #6',
    'OHX07CTC': 'coronal caries tooth count #7',
    'OHX08CTC': 'coronal caries tooth count #8',
    'OHX09CTC': 'coronal caries tooth count #9',
    'OHX10CTC': 'coronal caries tooth count #10',
    'OHX11CTC': 'coronal caries tooth count #11', 
    'OHX12CTC': 'coronal caries tooth count #12',
    'OHX13CTC': 'coronal caries tooth count #13',
    'OHX14CTC': 'coronal caries tooth count #14',
    'OHX15CTC': 'coronal caries tooth count #15',
    'OHX18CTC': 'coronal caries tooth count #18',
    'OHX19CTC': 'coronal caries tooth count #19',
    'OHX20CTC': 'coronal caries tooth count #20',
    'OHX21CTC': 'coronal caries tooth count #21',
    'OHX22CTC': 'coronal caries tooth count #22',
    'OHX23CTC': 'coronal caries tooth count #23',
    'OHX24CTC': 'coronal caries tooth count #24',
    'OHX25CTC': 'coronal caries tooth count #25',
    'OHX26CTC': 'coronal caries tooth count #26',
    'OHX27CTC': 'coronal caries tooth count #27',
    'OHX28CTC': 'coronal caries tooth count #28',
    'OHX29CTC': 'coronal caries tooth count #29',
    'OHX30CTC': 'coronal caries tooth count #30',
    'OHX31CTC': 'coronal caries tooth count #31'}, inplace=True)


# In[45]:


'''Converts each column to an appropriate type.'''
df_ohxden.astype({'unique ids': int})


# In[46]:


df_ohxden['dentition status code'].replace({1: 'complete', 2: 'partial',
    3: 'not done'}, inplace=True)
df_ohxden.replace({1: 'primary tooth (deciduous) present',
    2: 'permanent tooth present', 3: 'dental implant', 4: 'tooth not present',
    5: 'permanent dental root fragment present', 9: 'could not assess'},
    inplace=True)


# In[47]:


df_ohxden.replace({b'D': 'sound primary tooth',
    b'E': 'missing due to dental disease', b'J': 
    'permanent root tip is present but no restorative replacement is present',
    b'K': 'primary tooth with surface condition (s)',
    b'M': 'missing due to other causes', b'P': 
    'missing due to dental disease but replaced by a removable restoration',
    b'Q': 
    'missing due to other causes but replaced by a removable restoration',
    b'R':
    'missing due to dental disease, but replaced by a fixed restoration',
    b'S': 'sound permanent tooth',
    b'T': 
    'permanent root tip is present but a restorative replacement is present',
    b'U': 'unerupted',
    b'X': 'missing due to other causes, but replaced by a fixed restoration',
    b'Y': 'tooth present, condition cannot be assessed',
    b'Z': 'permanent tooth with surface condition (s)'}, inplace=True)
df_ohxden.replace({'NaN': -1}, inplace=True)
df_ohxden.reset_index(drop=True)


# In[48]:


'''Saves the dataframe to pickle format.'''
df_ohxden.to_pickle('dh_ohxden.pkl')


# c.

# In[49]:


f"There are {df_demo.shape[0]} cases in the demographic dataset."


# In[50]:


f"There are {df_ohxden.shape[0]}"    " cases in the oral health and dentition dataset."