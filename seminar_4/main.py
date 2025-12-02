# kaggle
#CSV and json
#Pandas: 1) Series 2) DataFrame

#pip install pandas
#pip install numpy
#import pandas as pd
#import numpy as np

#pandas
#print(df.describe()) # характеристикa
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

# numpy
# print(np.array([1, 2, 3])) '''одномерный массив'''
# print(np.array([1, 2, 3], dtype='float32')) '''одномерный массив с указанным итпом ([1. 2. 3.])'''
# print(np.array([[1, 2, 3], [4, 5, 6]], dtype='int16').itemsize) #  какое количество байт в памяти занимает один элемент
# print(np.array([[1, 2, 3], [4, 5, 6]], dtype='int16').nbytes) # какое количество байт занимает весь массив
# Все математические функции вызываются по похожему шаблону: сначала пишем np.название_математической_функции
# print(a.sum()) # сумма всех элементов массива
# print(a.mean()) # Среднее арифметическое всех элементов массива
# min/max  аналогично

# a = np.array([[1, 5, 8], [3, 4, 2]])
# print(a > 5)
# Out:
# [[False False  True]
#  [False False False]]




import pandas as pd
import numpy as np

# 1 Часть
# 1)
df = pd.read_csv('tested.csv')

# 2)
# а)
print(df.isnull().sum()) # пропущенные значения по столбцам

print(df.isnull().sum().sum()) # все пропущенные значения
# b)
print(df.info()) # # какая инфомрмация в каком столбце

print(df.describe())

print("Sex:", df['Sex'].unique())
print("Pclass:", df['Pclass'].unique())
print("Embarked:", df['Embarked'].unique())

# 3)
print(df.head(6)) # выведет первые 6 строк

# 4)
print(df['Age'].describe()) # статистика по столбцу Age

# 5)
print(f"{len(df)} - колличество строк, {len(df.columns)} - колличество столбцов")

# 6)
age_nulls = df['Age'].isnull().sum()
print(f"Пропусков в Age: {age_nulls}")

age_median = df['Age'].median()
df['Age'] = df['Age'].fillna(age_median)

null_index = df[df.isnull().any(axis=1)]
if len(null_index) >= 20:
    # Берем первые 20 строк с пропусками
    rows_to_drop = null_index.index[:20]
    df = df.drop(rows_to_drop)
    print(f"Удалено 20 строк с индексами: {list(rows_to_drop)}")

# 2 Част
# 1)
# для того, чтобы выполнчть вторую часть нам надо из пандас перейти в нампи, это осуществляется таким способом
age_array = df['Age'].to_numpy()
survived_array = df['Survived'].to_numpy()
sex_array = df['Sex'].to_numpy()
pclass_array = df['Pclass'].to_numpy()
fare_array = df['Fare'].to_numpy()

# для удобноой фильтрации созданим фильры:
mask_male = sex_array == 'male'
#ghbfth
# sex_array = ['male', 'female', 'male', 'female']
# mask_male = sex_array == 'male'
# Результат: [True, False, True, False]
mask_female = sex_array == 'female'
mask_survived = survived_array == 1
mask_died = survived_array == 0



# a) Процент выживших
male_survival_rate = np.mean(survived_array[mask_male]) * 100 # значения выживания для мужчин,
female_survival_rate = np.mean(survived_array[mask_female]) * 100 # то же самое для женскоого пола
print(f"   Мужчины: {male_survival_rate:.2f}%")
print(f"   Женщины: {female_survival_rate:.2f}%")

# b) cредний возраст
male_mean_age = np.mean(age_array[mask_male]) # возрасты только мужчин, считает среднее,
female_mean_age = np.mean(age_array[mask_female])
print(f"   Мужчины: {male_mean_age:.2f} лет")
print(f"   Женщины: {female_mean_age:.2f} лет")

# c) cредний возраст выживших и погибших
male_survived_age = np.mean(age_array[mask_male & mask_survived])
male_died_age = np.mean(age_array[mask_male & mask_died])
female_survived_age = np.mean(age_array[mask_female & mask_survived])
female_died_age = np.mean(age_array[mask_female & mask_died])


# 2)
# а)
mask_2a = (age_array > 30) & (sex_array == 'male') & (pclass_array == 1)
print(df[mask_2a].head())

# b) Моложе 18 лет ИЛИ женщины, при этом выжили
mask_2b = ((age_array < 18) | (sex_array == 'female')) & (survived_array == 1)
print(df[mask_2b].head())

# 3) Группировка с использованием numpy

# Уникальные значения классов и пола
unique_classes = np.unique(pclass_array)
unique_sexes = np.unique(sex_array)

results = []
# двойной цикл для всевозможных комбинаций
for pclass in unique_classes:
    for sex in unique_sexes:
        mask = (pclass_array == pclass) & (sex_array == sex)
        if np.sum(mask) == 1:  # Если в группе есть хотя бы один человек
            mean_age = np.mean(age_array[mask])
            survival_rate = np.mean(survived_array[mask]) * 100
            mean_fare = np.mean(fare_array[mask])

            results.append({
                'Pclass': pclass,
                'Sex': sex,
                'Средний_возраст': mean_age,
                'Доля_выживших_%': survival_rate,
                'Средняя_цена_билета': mean_fare
            })

# Создаем DataFrame из результатов
results_df = pd.DataFrame(results)
print(results_df.to_string(index=False))










# # sred = d["Age"].sum() / len(d["Age"])
# print(d["Age"].mean(), "- средний возраст")
# d.fillna({"Age": d["Age"].mean()}, inplace=True)  # пересоздание и сохранение ланных в таблице df
# print(d["Age"]) # вывели посмотреть что стало
# d = d.dropna(subset=["Embarked"])  # удаляет строки в кторых нет пункта назначения гостя
#
# # 2
#
# print(d["Survived"].mean() * 100) # % выживших
