#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np # importando numpy
from scipy import stats # importando scipy.stats
import pandas as pd #
import matplotlib.pyplot as plt
from scipy.stats import kurtosis 
from scipy.stats import skew

calif=(0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6,
6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 10)


# In[ ]:





# In[8]:


np.mean(calif) #Media aritmetica


# In[10]:


# mediana
np.median(calif) 


# In[13]:


# Desviación típica
np.std(calif)


# In[14]:


# varianza
np.var(calif)


# In[15]:


# moda
stats.mode(calif)


# In[20]:


np.corrcoef(calif)


# In[ ]:





# In[26]:


datos_graf =(0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 10)


# In[27]:


bp = ax.boxplot(datos_graf)


# In[28]:


DataFrame.boxplot( column = calif, by = str, ax = None , fontsize = None , rot = 0 , grid = True , figsize = None , layout = None , return_type = None , backend = None , ** kwargs )[fuente]


# In[34]:


fig1, ax1 = plt.subplots()
ax1.set_title('Caja de brazos')
ax1.boxplot(calif)


# In[42]:


np.percentile(calif, 25) # percentil al 25


# In[43]:


np.percentile(calif, 75) # percentil 75


# In[9]:


# Histograma
plt.title('Histograma calificaciones')
plt.hist(calif, bins = 60, alpha=1, edgecolor = 'black',  linewidth=1)
plt.grid(True)
plt.show()
plt.clf()


# In[15]:


calif.skew()


# In[16]:


print("skew : ",skew(calif)) 
print("kurt : ",kurtosis(calif)) 


# In[ ]:




