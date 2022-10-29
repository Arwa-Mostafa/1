#!/usr/bin/env python
# coding: utf-8

# In[27]:


from pyopenms import *

seq = AASequence.fromString("DFPIANGER")    

prefix = seq.getPrefix(4)                   

suffix = seq.getSuffix(5)                   

concat = seq + seq                          

print("Sequence:", seq)
print("Prefix:", prefix)
print("Suffix:", suffix)
print("Concatenated:", concat)


# In[2]:


get_ipython().system('pip install pyopenms')


# In[10]:


from pyopenms import *

seq = AASequence.fromString("ARWA")  

prefix = seq.getPrefix(3)                   

print("Sequence:", seq)
print("Prefix:", prefix)


# In[11]:


suffix = seq.getSuffix(4)
print(suffix)


# In[12]:


concat = seq + seq
print(concat)


# In[13]:


mfull = seq.getMonoWeight()
print("Monoisotopic mass of peptide [M] is", mfull)


# In[15]:


seq = AASequence.fromString("ARWA") 
print("The peptide", str(seq), "consists of the following amino acids:")
for aa in seq:
    print(aa.getName(), ":", aa.getMonoWeight())


# In[16]:


seq = AASequence.fromString("ARWA")
seq_formula = seq.getFormula()
print("Peptide", seq, "has molecular formula", seq_formula)


# In[17]:


suffix = seq.getSuffix(2)                                       


print("y3 ion sequence:", suffix)

y3_formula = suffix.getFormula(Residue.ResidueType.YIon, 2)        

suffix.getMonoWeight(Residue.ResidueType.YIon, 2) / 2.0            

suffix.getMonoWeight(Residue.ResidueType.XIon, 2) / 2.0            



print("y3 mz:", suffix.getMonoWeight(Residue.ResidueType.YIon, 2) / 2.0 )

print("y3 molecular formula:", y3_formula)


# In[21]:


seq = AASequence.fromString("MOST(Oxidation)LA")
print(seq.toUnmodifiedString())
print(seq.toString())
print(seq.toUniModString())
print(seq.toBracketString())
print(seq.toBracketString(False))


# In[23]:


print(AASequence.fromString("MOST(UniMod:35)LA"))

print(AASequence.fromString("MOST[+16]LA"))

print(AASequence.fromString("MOST[+15.99]LA"))

print(AASequence.fromString("MOST[147]LA"))

print(AASequence.fromString("MOST[147.035405]GER"))


# In[25]:


bsa = FASTAEntry() 

bsa.sequence = "AM.MM"

bsa.description = "BSA (partial sequence)"

bsa.identifier = "BSA"

alb = FASTAEntry()

alb.sequence = "MMMMMMMMMMMMMMMMMMMMMMMMMMMMM"

alb.description = "ALB (partial sequence)"

alb.identifier = "ALB"


entries = [bsa, alb]

f = FASTAFile()

f.store("example.fasta", entries)


# In[26]:


entries = []

f = FASTAFile()

f.load("example.fasta", entries)

print( len(entries) )

for e in entries:
    print (e.identifier, e.sequence)


# In[ ]:




