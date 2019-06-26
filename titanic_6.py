import pandas as pd

df = pd.read_csv('train.csv')
sex = list(df['Sex'])
ln = len(sex)

for i in range(ln):
    if sex[i] == 'male':
        sex[i] = 1
    else:
        sex[i] = 0

sx = pd.DataFrame({'Sex':sex})

print(df['Age'].corr(df['Survived']))
print(sx['Sex'].corr(df['Survived']))
print(df['Pclass'].corr(df['Survived']))
