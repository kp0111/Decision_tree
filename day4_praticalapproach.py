#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from sklearn.datasets import load_iris


# In[3]:


iris=load_iris()


# In[4]:


iris


# In[5]:


iris.data


# In[18]:


from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt


# In[19]:


classifier = DecisionTreeClassifier()
classifier.fit(iris.data,iris.target)


# In[24]:


#  from sklearn import Tree
# # plt.figure(figsize=(15,10))
# # tree.plot_tree(classifier,filled =True)
# # plt.show()# Assuming 'classifier' is your DecisionTreeClassifier object
# plt.figure(figsize=(15, 10))
# tree.plot_tree(classifier, filled=True)
# plt.show()


from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Assuming 'classifier' is your DecisionTreeClassifier object
plt.figure(figsize=(15, 10))
plot_tree(classifier, filled=True)
plt.show()


# In[ ]:




