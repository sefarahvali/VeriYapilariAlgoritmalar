#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello")


# In[2]:


x = "Sefa"
y = "Rahvalı"
print(x+y)


# In[3]:


type(x)


# In[4]:


bl = True


# In[5]:


type(bl)


# In[6]:


st = "sefarahvalı"


# In[7]:


st[3]


# st içerisindeki elemanlar diziler gibi indexleme yapar. 0 dan başlarayak her bir harf elemanmış gibi davranır 
# yukarıdaki st[3] 3. indexdeki elemanı okumak için yazılır.

# In[17]:


len(st)


# In[18]:


st[len(st)-1]


# In[20]:


st[-2]


# In[21]:


st * 2


# In[29]:


st


# In[25]:


st.find("a")


# In[27]:


st.capitalize()


# In[30]:


st2 = "sefarahvali"


# In[32]:


st2[3:] #başlamaindexidir.


# 3: 3. indexten başla

# In[33]:


st2[:3] #sadece 012 - 3. indexte durur.


# In[34]:


st2[4:8] #4. indexten başlar 8.indexe kadar yazar (8.indexi dahil etmez.)


# In[36]:


st2[::3] #üçer üçer atlayarak gider.


# In[37]:


st2[::-1] # tersten yazdırma işlemi 


# In[ ]:




