import seaborn as sns
df = sns.load_dataset('titanic')
print(df.head())
print(df.isnull().sum())