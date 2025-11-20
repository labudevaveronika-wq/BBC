# kaggle

#CSV and json

#Pandas: 1) Series 2) DataFrame


#pip install pandas
#pip install numpy

#import pandas as pd
#import numpy as np


import pandas as pd
import numpy
df = pd.read_csv('tested.csv')

print("Кол-во пропусков: ", df.isna().sum().sum())
#print(df.describe()) # характеристики
#print(df.tail(6))
#print(df.info()) # какая инфомрмация в каком столбце
#print(df.head(6))
#print(df.shape) '''(418, 12)'''
#print(df.columns) '''Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'], dtype='object')'''
#print(df.iloc[0])  '''первая строка'''
#df.iloc[1:3] '''строки с 1 по 2 (как срез)'''
#df.loc[0]  '''строка с индексом 0'''
#df.loc[1:2]  '''cтроки с индексом 1 и 2 (в отличие от среза!)'''
#print(df.isnull()) '''возвращает DataFrame с булевыми значениями (True, где пропуск).'''
#print(df.dropna()) ''' удаляет строки или столбцы с пропущенными значениями'''
#print(df.fillna(0)) '''заполняет пропущенные значения указанным значением'''

import pandas as pd
import numpy as np

# 1
d = pd.read_csv("tested.csv")
print(d.describe())
print(d.isnull().sum())
print(d.info())
print(f"{len(d)} - колличество строк, {len(d.columns)} - колличество столбцов")
# sred = d["Age"].sum() / len(d["Age"])
print(d["Age"].mean(), "- средний возраст")
d.fillna({"Age": d["Age"].mean()}, inplace=True)  # пересоздание и сохранение ланных в таблице df
print(d["Age"]) # вывели посмотреть что стало
d = d.dropna(subset=["Embarked"])  # удаляет строки в кторых нет пункта назначения гостя

# 2

print(d["Survived"].mean() * 100) # % выживших
