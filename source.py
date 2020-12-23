
# coding: utf-8

# In[57]:


#import relevant libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import seaborn as sns

#read data
df=pd.read_excel("Data_for_computing.xls")

#inspect whether data was imported correctly
df.head()
# Define Features (X's) and target variale (Y) to examine relationship
x=df.drop(columns=["Values (total offer)"])
y=df["Values (total offer)"]
X=sm.add_constant(x)
      
#check for shape of data to see everything was imported correctly 
x.shape ,y.shape
#fit model
lr = LinearRegression()
#make sure target and feature variables were defined correctly
print(x)
print("--------------------------------------------------------")

df.head()






# In[58]:


#Run ordinary least squares regression to examine y and x relationships
model=sm.OLS(y,X).fit()
#get statistical summary
model.summary()


# In[60]:


#plot target variable against a feature
sns.regplot(x="sqft (Area)", y="Values (total offer)",data=df)
#as we can logically infer total offer increases with square footage


#Test file
class versions:
  def_init_(self,Data_for_computing.xls,version) :
      
def main():      
  
print(pd.__version__)
print(np.__version__)
print(sns.__version__)

version=("pandas,numpy or seaborn")

version=Versions("Data_for_computing.xls",version)


main()

