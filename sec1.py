#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pyopenms')


# In[3]:


import pyopenms


# In[6]:


print ("number it's",pyopenms.Constants.AVOGADRO)


# In[11]:


from pyopenms import*
edb = ElementDB()
edb.hasElement("F")


# In[16]:


oxgyen=edb.getElement("O")
print(oxgyen.getName())
print(oxgyen.getSymbol())
print(oxgyen.getMonoWeight())
print(oxgyen.getAverageWeight())
print("One Mole Of Oxygen Wieght",2*oxgyen.getAverageWeight(),"Grams")


# In[24]:


ebd=ElementDB()
oxygen_isoDist={"Mass": [],"Abundance": []}
oxgyen=edb.getElement("O")
isotopes=oxgyen.getIsotopeDistribution()

for iso in isotopes.getContainer():
    print ("Oxygen Isotope", iso.getMZ(), "Has Abundance", iso.getIntensity()*100, "%")
    oxygen_isoDist["Mass"].append(iso.getMZ())
    oxygen_isoDist["Abundance"].append((iso.getIntensity() * 100))


# In[25]:


sulfur =edb.getElement("S")
print(sulfur.getName())
print(sulfur.getSymbol())
print(sulfur.getMonoWeight())
print(sulfur.getAverageWeight())
isotopes=sulfur.getIsotopeDistribution()
print("One Mole Of 1602 Weight",2*oxgyen.getMonoWeight(),"Grams")


# In[29]:


sulfur_isoDist = {"mass": [], "abundance": []}


sulfur = edb.getElement("S")


isotopes = sulfur.getIsotopeDistribution()


for iso in isotopes.getContainer():
    print ("Sulfur Isotope", iso.getMZ(), "Has Abundance", iso.getIntensity()*100, "%")
    sulfur_isoDist["mass"].append(iso.getMZ())
    sulfur_isoDist["abundance"].append((iso.getIntensity() * 100))


# In[30]:


methanol = EmpiricalFormula("CH3OH")


water = EmpiricalFormula("H2O")



ethanol = EmpiricalFormula("CH2") + methanol



print("Ethanol Chemical Formula:", ethanol.toString())


# In[31]:


lys=ResidueDB().getResidue("Lysine")

print(lys.getName())
print(lys.getThreeLetterCode())
print(lys.getOneLetterCode())
print(lys.getAverageWeight())
print(lys.getMonoWeight())
print(lys.getPka())
print(lys.getFormula().toString())


# In[32]:


ox = ModificationsDB().getModification("Oxidation")

print(ox.getUniModAccession())
print(ox.getUniModRecordId())
print(ox.getDiffMonoMass())
print(ox.getId())
print(ox.getFullId())
print(ox.getFullName())
print(ox.getDiffFormula())


# In[33]:


isotopes = ox.getDiffFormula().getIsotopeDistribution(CoarseIsotopePatternGenerator(5))
for iso in isotopes.getContainer():
    print (iso.getMZ(), ":", iso.getIntensity())


# In[34]:


uridine = RibonucleotideDB().getRibonucleotide(b"U")

print(uridine.getName())
print(uridine.getCode())
print(uridine.getAvgMass())
print(uridine.getMonoMass())
print(uridine.getFormula().toString())
print(uridine.isModified())


methyladenosine = RibonucleotideDB().getRibonucleotide(b"m1A")

print(methyladenosine.getName())
print(methyladenosine.isModified())


# In[ ]:




