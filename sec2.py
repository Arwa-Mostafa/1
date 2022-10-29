#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open('note.xml') as f:
    for line in f:
        print(line.strip())


# In[3]:


import xml.etree.ElementTree as ET
tree = ET.parse('note.xml')
root = tree.getroot()
print(root.tag)


# In[4]:


import xml.etree.ElementTree as ET
tree = ET.parse('note.xml')
root = tree.getroot()
print(root.tag)


# In[5]:


for child in root:
    print(child.tag, child.attrib)


# In[6]:


print(root[3][1].text)


# In[7]:


print(root[0][3].text)


# In[8]:


print(root[0].text)


# In[9]:


for title in root.iter('from'):
    print(title.attrib)


# In[12]:


file=open("tet.txt","w")
file.write("MMMMMMMMMMMMMMMMMMMM")
file.close()


# In[13]:


f = open("tet.txt", "r")  

print(f.read())  

f.close()


# In[14]:


f = open("tet.txt", "r") 

print(f.read())   
f.close()


# In[15]:


file = open("sample.bin", "wb")

file.write(b"sample.bin")

file.close()


# In[16]:


file = open("sample.bin", "rb")  

print(file.read())

file.close()


# In[20]:


file=open("arr.bin","wb")
num1=[10,44,60,18,10]
arr=bytearray(num1)
file.write(arr)
file.close()


# In[21]:


f=open("arr.bin","rb")
num=list(f.read())
print(num1)
f.close()


# In[ ]:




