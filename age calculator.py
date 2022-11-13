#!/usr/bin/env python
# coding: utf-8

# In[4]:


def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)
ageCalculator(2001, 9, 3)


# In[ ]:





# In[ ]:




