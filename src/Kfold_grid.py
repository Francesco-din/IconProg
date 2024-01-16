import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import (AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier)
from sklearn.metrics import (precision_score, recall_score, f1_score, classification_report, confusion_matrix, fbeta_score)
from sklearn.model_selection import GridSearchCV, KFold

# Funzione per caricare e pre-processare i dati
def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)

    # Trasformazione delle colonne contenenti valori non numerici
    labEn = LabelEncoder()    
    df['TypeName'] = labEn.fit_transform(df['TypeName'])
    df['Company'] = labEn.fit_transform(df['Company'])
    df['Product'] = labEn.fit_transform(df['Product'])
    df['Cpu'] = labEn.fit_transform(df['Cpu'])
    df['ScreenResolution'] = labEn.fit_transform(df['ScreenResolution'])
    df['Memory'] = labEn.fit_transform(df['Memory'])
    df['Gpu'] = labEn.fit_transform(df['Gpu'])

    # Divisione dei dati nel training set e nel test set
    X = df.drop('TypeName', axis=1)
    y = df['TypeName']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

    return X_train, X_test, y_train, y_test

# Funzione per eseguire la cross-validation
def kfold_f(model, X_train, y_train):
    k_fold = 5
    kf = KFold(n_splits=k_fold, shuffle=True, random_state=42)
    cross_val_results =  cross_val_score(model, X_train, y_train, cv=kf, scoring='accuracy')

# Funzione per eseguire la grid search
def grid_search_f(model, param_grid, X_train, y_train, X_test, y_test):
    cv1 = 5
    scor = 'accuracy'
    grid_search = GridSearchCV(model, param_grid, cv=cv1, scoring=scor)
    grid_search.fit(X_train, y_train)
    # Stampa i migliori parametri trovati durante la grid search
    print("Best Parameters:", grid_search.best_params_)
    return grid_search

# Carica e pre-processa i dati
X_train, X_test, y_train, y_test = load_and_preprocess_data('./filecsv/newLaptopPrice.csv')
print('-' * 50 + '\n'+ "decison tree"+"\n")
# Decision Tree
decision_tree = DecisionTreeClassifier()
# Addestramento del modello
decision_tree.fit(X_train, y_train)
# Cross-Validation
cv_scores = kfold_f(decision_tree, X_train, y_train)
#           print("Cross-Validation Scores:", cv_scores)
# Definisci i parametri da esplorare per il decision tree
param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [None, 5, 10, 15],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
# Grid Search
grid_search = grid_search_f(decision_tree, param_grid, X_train, y_train, X_test, y_test)
# Valutazione del modello con i migliori parametri sul set di test
y_pred_grid = grid_search.predict(X_test)
print("\nGrid Search Classification Report dt:")
print(classification_report(y_test, y_pred_grid))
f2_grid = fbeta_score(y_test, y_pred_grid, beta=2, average='micro')
print(f"F2 Score: {f2_grid}\n")
conf_grid = confusion_matrix(y_test, y_pred_grid)
print(f"Confusion Matrix:\n{conf_grid}")

print('-' * 50 + '\n'+ "knn"+"\n")
#knn
knn=KNeighborsClassifier()
# Addestramento del modello
knn.fit(X_train, y_train)
# Cross-Validation
cv_scores = kfold_f(knn, X_train, y_train)
#           print("Cross-Validation Scores:", cv_scores)
# Definisci i parametri da esplorare per il knn
param_grid = {
    'n_neighbors': [3, 4, 5, 6],
    'metric': ['euclidean', 'manhattan', 'minkowski']
}
# Grid Search
grid_search1 = grid_search_f(knn, param_grid, X_train, y_train, X_test, y_test)
# Valutazione del modello con i migliori parametri sul set di test
y_pred_grid1 = grid_search1.predict(X_test)
print("\nGrid Search Classification Report knn:")
print(classification_report(y_test, y_pred_grid1))
f2_grid = fbeta_score(y_test, y_pred_grid1, beta=2, average='micro')
print(f"F2 Score: {f2_grid}\n")
conf_grid = confusion_matrix(y_test, y_pred_grid1)
print(f"Confusion Matrix:\n{conf_grid}")

print('-' * 50 + '\n'+ "random forest"+"\n")
#random forest
rdc=RandomForestClassifier(random_state=42)
# Addestramento del modello
rdc.fit(X_train, y_train)
# Cross-Validation
cv_scores = kfold_f(rdc, X_train, y_train)
#           print("Cross-Validation Scores:", cv_scores)
# Definisci i parametri da esplorare per il random tree
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'criterion': ['gini', 'entropy'],
    'max_features': ['sqrt', 'log2', None]
}
# Grid Search
grid_search2 = grid_search_f(rdc, param_grid, X_train, y_train, X_test, y_test)
# Valutazione del modello con i migliori parametri sul set di test
y_pred_grid2 = grid_search2.predict(X_test)
print("\nGrid Search Classification Report knn:")
print(classification_report(y_test, y_pred_grid2))
f2_grid = fbeta_score(y_test, y_pred_grid2, beta=2, average='micro')
print(f"F2 Score: {f2_grid}\n")
conf_grid = confusion_matrix(y_test, y_pred_grid2)
print(f"Confusion Matrix:\n{conf_grid}")


print('-' * 50 + '\n'+ "ada"+"\n")
#ada
ada=AdaBoostClassifier()
# Addestramento del modello
ada.fit(X_train, y_train)
# Cross-Validation
cv_scores = kfold_f(ada, X_train, y_train)
#           print("Cross-Validation Scores:", cv_scores)
# Definisci i parametri da esplorare per il ada
param_grid = {
    'n_estimators': [50, 100, 200],
    'learning_rate': [0.1, 0.5, 1.0], 
    'algorithm': ['SAMME', 'SAMME.R'], 
    'estimator': [DecisionTreeClassifier(max_depth=4), DecisionTreeClassifier(max_depth=5),DecisionTreeClassifier(max_depth=6), DecisionTreeClassifier(max_depth=7)],
    'random_state': [42]
}
# Grid Search
grid_search1 = grid_search_f(ada, param_grid, X_train, y_train, X_test, y_test)
# Valutazione del modello con i migliori parametri sul set di test
y_pred_grid1 = grid_search1.predict(X_test)
print("\nGrid Search Classification Report ada:")
print(classification_report(y_test, y_pred_grid1))
f2_grid = fbeta_score(y_test, y_pred_grid1, beta=2, average='micro')
print(f"F2 Score: {f2_grid}\n")
conf_grid = confusion_matrix(y_test, y_pred_grid1)
print(f"Confusion Matrix:\n{conf_grid}")


print('-' * 50 + '\n'+ "gradB"+"\n")
#gradB
gradB=GradientBoostingClassifier()
# Addestramento del modello
gradB.fit(X_train, y_train)
# Cross-Validation
cv_scores = kfold_f(gradB, X_train, y_train)
#           print("Cross-Validation Scores:", cv_scores)
# Definisci i parametri da esplorare per il gradB
param_grid = {
    'n_estimators': [50, 100, 150],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 4, 5],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
# Grid Search
grid_search1 = grid_search_f(gradB, param_grid, X_train, y_train, X_test, y_test)
# Valutazione del modello con i migliori parametri sul set di test
y_pred_grid1 = grid_search1.predict(X_test)
print("\nGrid Search Classification Report gradB:")
print(classification_report(y_test, y_pred_grid1))
f2_grid = fbeta_score(y_test, y_pred_grid1, beta=2, average='micro')
print(f"F2 Score: {f2_grid}\n")
conf_grid = confusion_matrix(y_test, y_pred_grid1)
print(f"Confusion Matrix:\n{conf_grid}")