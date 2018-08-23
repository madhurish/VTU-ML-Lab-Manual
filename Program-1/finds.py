
# coding: utf-8

# # Find-S Algorithm:
# ## Algorithm:
# 1. Initialize h to the most specific hypothesis in H
# 2. For each positive training instance x
#         i. For each attribute constraint a i in h :
#             a. If the constraint a i in h is satisfied by x Then do nothing
#             b. Else replace a i in h by the next more general constraint that is satisfied by x
# 3. Output hypothesis h
# 

# In[1]:


import csv


# ### Read File:
# Load the csv file and asign each row to a data frame
# Also print the row to see the dataset (optional)

# In[ ]:


a=[]
with open('finds.csv') as csfile:
    reader = csv.reader(csfile)
    for row in reader:
        a.append(row)
        print(row)
num_attributes=len(a[0])-1


# 1. The most general hypothesis is represented by:
#     ```['?', '?', '?', '?', '?', '?']```
# 2. The most specific hypothesis is represented by:
#     ```['0', '0', '0', '0', '0', '0']```

# In[ ]:


print("The most general hypothesis:",["?"]*num_attributes)
print("The most specific hypothesis:",["0"]*num_attributes)


# ### Algorithm Implementation:
# Implementation of the above algorithm by updaing the hypothesis at each iteration and output the final hypothesis.

# In[ ]:


hypothesis=a[0][:-1]
print("\n Find S: Finding a maximally specific hypothesis")
for i in range (len(a)):
    if a[i][num_attributes] == "Yes":
        for j in range(num_attributes):
            if a[i][j]!=hypothesis[j]:
                hypothesis[j]='?'
    print("The taining example no:",i+1," the hyposthesis is:",hypothesis)
print("\n The maximally specific hypohthesis for training set is")
print(hypothesis)

