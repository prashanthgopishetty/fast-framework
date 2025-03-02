import pandas as pd
import numpy as np

df = pd.read_csv('resources/data_banknote_authentication.csv')
#print(df.head(5))

X = df.iloc[:,:-1]
y = df.iloc[:,-1]
# print(X)
# print(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=0)

## Random forest classifier
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(X_train,y_train)

##prediction
y_pred = classifier.predict(X_test)

## accuracy check
from sklearn.metrics import accuracy_score
score = accuracy_score(y_test, y_pred)
print(score)
