#!/usr/bin/env python
# coding: utf-8

# In[44]:


# Program 32 :- Alphabet "K"
for row in range(7):
    for col in range(5):
        if col == 0 or (row == 2 and col == 2 or row == 1 and col == 3 or row == 0 and col == 4) or (row == 4 and col == 2 or row == 5 and col == 3 or row == 6 and col == 4) or row == 3 and col == 1:
            print("*", end = "")
        else:
            print(end =" ")
    print("\r")

