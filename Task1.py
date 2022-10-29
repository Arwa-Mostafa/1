#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyopenms import *


# In[6]:


seq = AASequence.fromString("UYKAVDC")  
mfull = seq.getMonoWeight()
print("Monoisotopic mass of peptide [M] is", mfull)


# In[7]:


seq = AASequence.fromString("UYKAVDC") 
print("The peptide", str(seq), "consists of the following amino acids:")
for aa in seq:
    print(aa.getName(), ":", aa.getMonoWeight())


# In[ ]:




