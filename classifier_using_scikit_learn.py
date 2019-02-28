from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.metrics import accuracy_score


#sample data for X and Y
#X [height, weight,shoe size]
#Y gender associated to it
X= [[181,80,44], [175,60,42], [160,45,40], [165,75,47], [165,75,54],[155,71,44],[161,72,50],[157,84,51],[165,77,51],[145,71,52],[166,85,44] ]
Y= ['male','female','female','male','male','male','female','male','male','female','female']

#declaring classifiers
clfr= tree.DecisionTreeClassifier()
clfr1= GaussianNB()
clfr2= svm.SVC()

#training model
clfr=clfr.fit(X,Y)
clfr1= clfr1.fit(X,Y)
clfr2= clfr2.fit(X,Y)


#Validation data
_X=[[184,84,44],[198,92,48],[183,83,44],[166,47,36],[170,60,38],[172,64,39],[182,80,42],[180,80,43]]
_Y=['male','male','male','female','female','female','male','male']


#prediction
prediction= clfr.predict(_X)
prediction1= clfr1.predict(_X)
prediction2= clfr2.predict(_X)

#results 
result1 = accuracy_score(_Y,prediction)
result2 = accuracy_score(_Y,prediction1)
result3 = accuracy_score(_Y,prediction2)

#print best result
if result1 > result2 and result1 > result3:
	print("Decision Tree : ",result1)
elif result2 > result3 and result2 > result1:
	print("Naive Bayes : ",result2)
else :
	print("SVM : ",result3)

