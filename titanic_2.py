import pandas as pd

df = pd.read_csv('train.csv')
cnt = (df.groupby(['Embarked'])['PassengerId'].count())

for summ in list(cnt):
    print (summ, end = ' ')
