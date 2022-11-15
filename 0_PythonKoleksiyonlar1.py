#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Listeler


# In[2]:


eList = [1,2,3,4,5,6,7,8]


# In[3]:


type(list)


# In[4]:


eList2=list() #boş liste oluşturur


# In[5]:


#listeleme fonksiyonlarını deneyeceğiz.


# In[6]:


eList2.append("a")


# In[7]:


eList


# In[8]:


eList2


# In[9]:


mixList = [1,2,3,4,"a",True]


# In[12]:


nestedList = [1,2,3,["a","b","c"],[28,30]]


# In[15]:


nestedList[3]


# In[18]:


nestedList[4][1]


# In[19]:


nestedList[3][1]=2


# In[20]:


nestedList[3][1]


# In[21]:


nestedList


# In[24]:


#nestedList.append("54") # listenin sonuna ekleme yapabileceğimiz fonksiyondur.


# In[25]:


nestedList


# In[26]:


nestedList.insert(1,"34")


# In[28]:


nestedList


# In[31]:


nestedList.pop() #son elemanı sildi


# In[30]:


nestedList


# In[34]:


nestedList.pop(2) #2. indexi silmiş


# In[33]:


nestedList


# In[35]:


nl1 = [1,2,3,["a","b","c"],[24,28]]


# In[36]:


nl2 = [4,5,6,["d","e","f"],[28,32]]


# In[39]:


nl1.extend(nl2) # listeyi genişletelim, ancak sonunaekler


# In[38]:


nl1


# In[40]:


n3 = [1,4,6,3,2,5,7,11,9]


# In[41]:


n3.sort()


# In[42]:


n3


# In[48]:


n4 = ["veli","ahmet","mehmet"] #turkce karakter olmayacak sekilde siralar.


# In[44]:


n4.sort()


# In[45]:


n4


# In[46]:


n4.reverse() # listeyi baştan sona ters çevirir.


# In[47]:


n4


# In[49]:


n4.append("mehmet")


# In[50]:


n4


# In[52]:


n4.count("mehmet") #n4 listesinde kaç adet mehmet var? Cevap : 2


# In[53]:


n5 = [18,23,24,28]


# In[60]:


n6 = n5.copy() #listeyi kopyaladik n6 değişkenine aktardik.


# n6

# In[61]:


print(n6)


# In[ ]:




