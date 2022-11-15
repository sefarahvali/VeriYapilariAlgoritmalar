#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Dictionary : anahtar değer eşleşmesidir. fonsiyonlarınada bakacağız.

# liste gibi nested özelliği vardır.
# liste metotlarını kullanabiliriz.
# liste metotlarına ek olarak keys, items, values ve get metodunu kullanabiliriz.


# In[3]:


d = {"apple":100,"banana":200,"melon":300} #key - value tiplerini değiştirebiliriz.


# In[5]:


d["banana"] #sadece key yazacağız.


# In[6]:


d["banana"] = 400


# In[7]:


d["banana"]


# In[8]:


#items


# In[11]:


d.keys() #anahtarları verir


# In[13]:


d.items() #bütün içeriği verir.


# In[14]:


d.values() #değerleri verir.


# In[18]:


d.get("sefa",54) #sefa anahtarı yoksa 54 değerini döndür. Ekleme yapmaz.


# In[19]:


d


# In[ ]:




