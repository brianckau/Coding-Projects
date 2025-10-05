#Dataset from Kaggle
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn import preprocessing
import warnings
from sklearn import tree
import matplotlib.pyplot as plt


warnings.filterwarnings('ignore')

data = pd.read_csv('/content/StudentPerformanceFactors.csv')

#Data Processing
data = pd.get_dummies(data,columns=['Parental_Involvement', 'Access_to_Resources', 'Extracurricular_Activities', 'Motivation_Level', 'Internet_Access','Family_Income', 'Teacher_Quality', 'School_Type',
                                    'Peer_Influence','Learning_Disabilities','Learning_Disabilities', 'Parental_Education_Level',
                                    'Distance_from_Home', 'Gender'])

X = data.columns[data.columns != 'Exam_Score']
Y = ['Exam_Score']

features = data[X]
target = data[Y]

#Split the data
xtrain,xtest,ytrain,ytest = train_test_split(features,target,test_size=0.3,random_state=20)

#Search for best hyperparameters
min_samples_split = np.arange(10,300,20)
max_depth = np.arange(2,12,1)
try_grid = [{"min_samples_split":min_samples_split,"max_depth":max_depth}]

trial = GridSearchCV(DecisionTreeRegressor(),param_grid=try_grid)
trial.fit(xtrain,ytrain)
trial.best_params_

decisiontree = DecisionTreeRegressor(min_samples_split = int(trial.best_params_["min_samples_split"]),
                                     max_depth = int(trial.best_params_['min_samples_split']))
decisiontree.fit(xtrain,ytrain)

#Tree Plotting
plt.figure(figsize=(100,200))
_ = tree.plot_tree(decisiontree,feature_names=xtrain.columns,filled=True)

#Evaluate Performance of the model
from sklearn.model_selection import cross_val_score
from tabulate import tabulate

cv_r2 = cross_val_score(decisiontree, xtrain, ytrain, cv=10, scoring = 'r2').mean()
cv_mse = cross_val_score(decisiontree, xtrain, ytrain, cv=10, scoring = 'neg_mean_squared_error').mean()

rows = [
    ["Cross-Validation Scorings", f"{cv_r2:.4f}", f"{-cv_mse:.4f}"]
]

print(tabulate(rows,headers=['R-Square','MSE']))

#Important Features driving exam scores
feature_importances = pd.Series(decisiontree.feature_importances_,index=xtrain.columns).sort_values(ascending=False).iloc[0:10]
feature_importances

#Prediction
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae

prediction = decisiontree.predict(xtest)
rmse = np.sqrt(mse(prediction,ytest))
mae = mae(prediction,ytest)

print(f'RMSE for the decision tree regressor is {rmse:.3f} for the testing data.')
print(f'MAE for the decision tree regressor is {mae:.3f} for the testing data.')

