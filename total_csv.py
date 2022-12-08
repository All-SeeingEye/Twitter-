import pandas as pd


dfkaty = pd.read_csv('Tweets_katyperry.csv')
dfelon = pd.read_csv('Tweets_elonmusk.csv')
dfnaren = pd.read_csv('Tweets_narendramodi.csv')
dftaylor = pd.read_csv('Tweets_taylorswift13.csv')
dfCrish = pd.read_csv('Tweets_Cristiano.csv',lineterminator='\n')

df = pd.concat([dfCrish, dfkaty,dfelon,dfnaren,dftaylor])
df.to_csv('Tweets_Overall.csv', index=False)