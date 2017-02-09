
# coding: utf-8

# # Pandas: Working with Data Frames - summarizing with groupby

# In[1]:

import numpy as np              #standard imports
import scipy as sc
import pandas as pd
import matplotlib as plt
get_ipython().magic('matplotlib inline')


# ## Read the Hall of Fame dataset from the Baseball-Databank

# In[2]:

hall = pd.read_csv("../../baseballdatabank/core/HallOfFame.csv")


# ## List the first 5 rows of the hall Data Frame

# In[3]:

hall.head()


# ## Show the column names of the hall Data Frame 

# In[4]:

hall.columns


# ## List the number of records for each cagegory

# In[5]:

hall.groupby('category').count()


# ## List the votedBy counts

# In[6]:

hall.groupby('votedBy').count()


# ## Two-level groupby

# In[7]:

hall.groupby(('category','votedBy')).count()


# In[8]:

hall.groupby(('votedBy','category')).count()


# ## Groupby with selection - groupby over a subset

# In[9]:

hall[hall.votedBy=='Veterans'].groupby('category').count()


# Note that there is no indication that the above list is only 'Veterans'.  We can use a two-level groupby in this case:

# In[10]:

hall[hall.votedBy=='Veterans'].groupby(('votedBy','category')).count()


# ## Read the master Data Frame and list the column names

# In[11]:

master = pd.read_csv("../../baseballdatabank/core/Master.csv")
master.columns


#    ## Show the column names of the master Data Fram

# In[12]:

master.columns


# ## List the columns of the master Data Frame

# In[13]:

master.columns


# ## Exercise: produce a list showing the counts of hall of fame inductees by year

# In[64]:

hall[['yearid','inducted']][hall.inducted=='Y'].groupby('yearid').count()


# ## Exercise: produce a list showing the counts of living hall of fame inductees by year

# In[57]:

pd.merge(hall[hall.inducted =='Y'],master[master.deathYear.isnull()],how='inner')


# ## Exercise: produce a list showing the number of times each player was voted on for induction into the hall of fame

# In[84]:

hall[['playerID','votes']].groupby('playerID').count()


# In[ ]:



