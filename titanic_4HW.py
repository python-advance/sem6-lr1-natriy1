import pandas as pd

def perc (x):
    a=0
    for summ in x:
        a = a + summ
    for cnt in x:
        print ("%.2f" % (cnt/a), end = ' ')

df = pd.read_csv('train.csv')

cnt = list((df.groupby(['Pclass'])['PassengerId'].count()))
perc (cnt)
