import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

#Load data and preprocessing it
'''
The dataset contains cases  from a study that was 
conducted between 1958 and 1970 at the University 
of Chicago's Billings Hospital on the survival of 
patients who had undergone surgery for cancer

1. Age of patient at time of operation (numerical) 
2. Patient's year of operation (year - 1900, numerical) 
3. Number of positive axillary nodes detected (numerical) 
4. Survival status (class attribute) 
-- 1 = the patient survived 5 years or longer 
-- 2 = the patient died within 5 year
'''
c1,c2,c3,c4 = np.loadtxt('data.csv',unpack=True,delimiter = ',')
x= np.column_stack((c1,c3))
y= c4
#Create NaiveBayes Classifier
clf = GaussianNB()
#fit the mode
clf.fit(x,y)
#make predictions
predictions = clf.predict(x)

#calculate accuracy
print(accuracy_score(y,predictions))