import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (accuracy_score, classification_report, confusion_matrix, fbeta_score)
from sklearn.ensemble import (AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier)
from sklearn.tree import DecisionTreeClassifier


df = pd.read_csv('./filecsv/newLaptopPrice.csv')

#trasformazione delle colonne contenenti valori non numerici
labEn = LabelEncoder()    
df['TypeName'] = labEn.fit_transform(df['TypeName'])
df['Company'] = labEn.fit_transform(df['Company'])
df['Product'] = labEn.fit_transform(df['Product'])
df['Cpu'] = labEn.fit_transform(df['Cpu'])
df['ScreenResolution'] = labEn.fit_transform(df['ScreenResolution'])
df['Memory'] = labEn.fit_transform(df['Memory'])
df['Gpu'] = labEn.fit_transform(df['Gpu'])


#divisione dei dati nel training set e nel test set
X=df.drop('TypeName', axis=1)
y=df['TypeName']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

#knn
knn = KNeighborsClassifier(metric='manhattan', n_neighbors= 5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

print()
print("KNN Classification Report:")
print(classification_report(y_test, y_pred_knn))
f2_knn = fbeta_score(y_test, y_pred_knn, beta=2, average='micro')
print(f"F2 Score: {f2_knn}\n")

conf = confusion_matrix(y_test, y_pred_knn)
print(f"Confusion Matrix : \n{conf}")

#Decision Tree
dtc = DecisionTreeClassifier(criterion= 'gini', max_depth= 10, min_samples_leaf= 4, min_samples_split= 2, random_state=42)
dtc.fit(X_train, y_train)
y_pred_dtc = dtc.predict(X_test)

print()
print("Decision Tree Classification Report:")
print(classification_report(y_test, y_pred_dtc))
f2_dtc = fbeta_score(y_test, y_pred_dtc, beta=2, average='micro')
print(f"F2 Score: {f2_dtc}\n")

conf = confusion_matrix(y_test, y_pred_dtc)
print(f"Confusion Matrix : \n{conf}")

#random forest classifier
rd_clf = RandomForestClassifier(criterion = 'entropy', max_depth = None, max_features = 'sqrt', min_samples_leaf = 1, min_samples_split = 2, n_estimators = 50, random_state=42)
rd_clf.fit(X_train, y_train)
y_pred_rd_clf = rd_clf.predict(X_test)

print()
print("Random Forest Classification Report:")
print(classification_report(y_test, y_pred_rd_clf))
f2_rd_clf = fbeta_score(y_test, y_pred_rd_clf, beta=2, average='micro')
print(f"F2 Score: {f2_rd_clf}")

conf = confusion_matrix(y_test, y_pred_rd_clf)
print(f"Confusion Matrix : \n{conf}")


# ADA BOOST CLASSIFIER
dtc1 = DecisionTreeClassifier(max_depth = 7)
ada = AdaBoostClassifier(estimator = dtc1,algorithm ='SAMME',learning_rate = 1.0, n_estimators = 100, random_state = 42)
ada.fit(X_train, y_train)
y_pred_ada = ada.predict(X_test)

print()
print("Ada Boost Classifier Classification Report:")
print(classification_report(y_test, y_pred_ada))
f2_ada = fbeta_score(y_test, y_pred_ada, beta=2, average='micro')
print(f"F2 Score: {f2_ada}")

conf = confusion_matrix(y_test, y_pred_ada)
print(f"Confusion Matrix : \n{conf}")


# GRADIENT BOOSTING CLASSIFIER
gb = GradientBoostingClassifier(learning_rate = 0.1, max_depth = 5, min_samples_leaf = 4, min_samples_split = 5, n_estimators = 100)
gb.fit(X_train, y_train)
y_pred_gb = gb.predict(X_test)

print()
print("Gradient Boosting Classifier Classification Report:")
print(classification_report(y_test, y_pred_gb))
f2_gb = fbeta_score(y_test, y_pred_gb, beta=2, average='micro')
print(f"F2 Score: {f2_gb}")

conf = confusion_matrix(y_test, y_pred_gb)
print(f"Confusion Matrix : \n{conf}")
