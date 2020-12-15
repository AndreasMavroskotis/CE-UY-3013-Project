
# coding: utf-8

# In[32]:


#import the relevant libraries that will be used
import numpy as np
import pandas as pd
import os


# In[33]:


# --- Declare working directory --- #
path = os.getcwd() # not used but is a good practice

#import and read CSV file containing the Data

df=pd.read_csv('engineering_data.csv')

#Check if the data was imported correctly
#this command is to display the whole data frame
pd.set_option("display.max_rows", None, "display.max_columns", None)



#drop NAs from the data
df=df.dropna()
print(df)
#set variables with which total offer is calculated
overhead=0.1
profit=0.05
bonding=0.01


# In[34]:


#Model calculating the total cost of a high quality office of 30000sqft with 10 floors
#Sqft we can chnage these every time we calculate
X=30000
#floors we can chnage these every time we calculate
y=10
cost=X*227.15*y
print("Total cost=", cost,'$')
#model calculating total offer
offer=cost+(cost*overhead+cost*profit+cost*bonding)
print("Offer =",offer,'$')

# Here is a test class
cost Testclass:
  def __init__(self, number):
        self.number = number

#the end

