#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df = pd.read_excel(r'G:\notes\SEM_7\DeepLearning\project\dataset\isro_20.xlsx')
df.sample(5)


# In[6]:


df.describe()


# In[7]:


df.info(verbose=True)


# In[8]:


import missingno as msno
null_count_plot = msno.bar(df)

# as per initial analysis we did not find any null value, except for column_29 where there is no data entry


# In[66]:


distribution_plot = df.hist(figsize = (20,20))


# In[9]:


df1 = df.loc[:, df.columns != 'Column29']
df1.sample(5)


# In[32]:


help(plt.boxplot)


# In[69]:


# The difference between Q3 and Q1 is called the Inter-Quartile Range or IQR.
# q1 - 1st quartile
# q3 - 3rd quartile


for i in range(1,19):
    plt.boxplot(df['Column'+str(i)])
    plt.xlabel('Column'+str(i))
    plt.show()


# In[70]:


for i in range(1,19):
    plt.boxplot(df['Column'+str(i)], notch=False, sym='+', vert=False, whis=1.5,positions=None, widths=None, patch_artist=False,bootstrap=None, usermedians=None, conf_intervals=None)
    plt.xlabel('Column'+str(i))
    plt.show()


# In[ ]:


# based on  above box_plot we have found that Column7, Column10, Column11, Cloumn14 have anamoly behaviour


# In[12]:


# column 20 - 28 have object type of data let us convert to numberical value using 

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
df1['Column20_endc'] = le.fit_transform(df1['Column20'])

le.classes_

# le.transform([0])

# le.inverse_transform([0, 0, 1, 2])


# In[13]:


for i in range (21,28):
    df1['Column'+str(i)+'_endc'] = le.fit_transform(df1['Column'+str(i)])


# In[14]:


df1.sample(5)


# In[15]:


df1.describe()


# In[16]:


distribution_plot = df1.hist(figsize = (20,20))


# In[80]:


for i in range(20,27):
    plt.boxplot(df1['Column'+str(i)+'_endc'], notch=False, sym='+', vert=False, whis=1.5,positions=None, widths=None, patch_artist=False,bootstrap=None, usermedians=None, conf_intervals=None)
    plt.xlabel('Column'+str(i)+'_endc')
    plt.show()


# In[ ]:


# there is no anamoly detected by object values so far


# In[79]:


for i in range(20,27):
    sns.kdeplot(df1['Column'+str(i)+'_endc'],warn_singular=False)
    plt.show()


# In[89]:


# finding outlier using simple math

low = .05
high = .95
quant_df = df1.quantile([low, high])
quant_df


# In[103]:


# Printing outlier in each column based on above technique
final_anml_df = pd.DataFrame()

for i in list(quant_df.columns.values):
    low = quant_df[i].iloc[0]
    high = quant_df[i].iloc[1]
    print("This is anamoly in " + i  + "\n")
    
    print("This is anamoly in df having high outliers")
    rslt_df = df1[df1[i] > high]
    print(rslt_df)
    
    print("This is anamoly in df having low outliers")
    rslt_df1 = df1[df1[i] > high]
    print(rslt_df1)
    
    final_anml_df = final_anml_df.append(rslt_df)
    final_anml_df = final_anml_df.append(rslt_df1)


#     for j in df1[i]:
#         if(j<low or j>high):
#             print(j)
            
    print("\n")
#     print(i)
    
# quant_df['Column25_endc'].iloc[1]


# In[106]:


final_anml_df.to_excel('anamoly.xlsx')
final_anml_df1 = final_anml_df.drop_duplicates()
final_anml_df1.to_excel('anamoly_no_dupl.xlsx')


# In[18]:


from sklearn.neighbors import KernelDensity
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
kde.score_samples(X)


# In[23]:


for i in range(1,19):
    sns.kdeplot(df['Column'+str(i)])
    plt.show()


# In[33]:


fig, ax = plt.subplots(figsize=(20,10)) 
ax = sns.heatmap(df.corr(), cmap="YlGnBu", annot=True)
# displaying heatmap
plt.show()


# In[34]:


fig, ax = plt.subplots(figsize=(35,15)) 
ax = sns.heatmap(df1.corr(), cmap="YlGnBu", annot=True)
# displaying heatmap
plt.show()


# In[37]:


from sklearn import preprocessing
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
df1_copy = df1.select_dtypes(include=numerics)
df1_copy = preprocessing.normalize(df1_copy,axis=0)
scaled_df = pd.DataFrame(df1_copy)
scaled_df.sample(n=5)


# In[38]:


from sklearn.neighbors import LocalOutlierFactor
help(LocalOutlierFactor)


# In[64]:


import numpy as np
from sklearn.neighbors import LocalOutlierFactor
X = df['Column7'].to_numpy().reshape(-1,1)
clf = LocalOutlierFactor(n_neighbors=2)
clf.fit_predict(X)
y_pred = clf.fit_predict(X)
np.unique(y_pred)


# In[65]:


from sklearn.ensemble import IsolationForest
X = df['Column7'].to_numpy().reshape(-1,1)
clf = IsolationForest(random_state=0).fit(X)
y_pred = clf.predict(X)
np.unique(y_pred)


# In[55]:


help(LocalOutlierFactor)


# In[ ]:




