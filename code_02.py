#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install numpy


# In[4]:


pip install pandas


# In[5]:


pip install seaborn


# In[6]:


import sklearn


# In[7]:


pip install sklearn


# In[8]:


pip install scikit-learn


# In[9]:


import sklearn


# In[10]:


from sklearn import tree 


# In[11]:


feature =[[140,14],[130,1],[150,0],[170,0]]


# In[12]:


labels=[0,0,1,1]


# In[13]:


clf =tree.DecisionTreeClassifier()


# In[14]:


clf=clf.fit(feature,labels)


# In[15]:


print(clf.predict([[150,0]]))


# 1 means orange and 0 means apple

# In[ ]:
//enter




