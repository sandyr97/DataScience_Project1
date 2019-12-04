# # Jimmy Wrangler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df_movies=pd.read_csv("../data/filmtv_movies.csv")
df_boxoffice=pd.read_csv("../data/boxoffice.csv")

df_movies.head(10)

df_boxoffice.head(10)
df3=pd.merge(df_movies, df_boxoffice, on="title")
df3.head(10)
df3['is_year_equal'] = np.where(df3['year_x']==df3['year_y'], 'yes', 'no')
df3.isnull().sum()
df3=df3.drop('description',1)
df3=df3.drop('notes',1)
df3=df3.drop('actors',1)

df3.isna().any()

df3.dropna(inplace=True)
df3.head(10)
df4=df3[df3.is_year_equal != 'no']
df4.head(10)

# ## Most of the data occurs within the 2000s
totalyear = df4.groupby(['year_y']).year_y.count()
totalyear.sort_values(ascending=False).head(11)

movies2013 = df4[df4.year_y == 2013]
movies2013.head()

movies2017 = df4[df4.year_y == 2017]
movies2016 = df4[df4.year_y == 2016]
movies2007 = df4[df4.year_y == 2007]
movies2006 = df4[df4.year_y == 2006]
movies2015 = df4[df4.year_y == 2015]
movies2008 = df4[df4.year_y == 2008]
movies2012 = df4[df4.year_y == 2012]
movies2004 = df4[df4.year_y == 2004]
movies2014 = df4[df4.year_y == 2014]

frames = [movies2013, movies2016, movies2007, movies2017, movies2014, movies2012, movies2006, movies2015, movies2004, movies2008, movies2006]

result = pd.concat(frames)
result.head(10)


# ## Feature Engineering
for i,row in result.iterrows():
    country=str(row['country'])
    if country!=('no genres listed'):
        country=country.split(',')
        for g in country:
            result.at[i,g]=1
result.head(10)

result.fillna(0)
result.head()


# ## Visualization

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid")
sns.lmplot(x='rank',y='lifetime_gross',data=result, fit_reg=False)

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="darkgrid")
sns.lmplot(x='avg_vote',y='lifetime_gross',data=result, fit_reg=False, hue='genre')
sPlot= sns.swarmplot(x='genre',y='lifetime_gross',data=result)
sPlot.set_xticklabels(sPlot.get_xticklabels(), rotation=90)

result.fillna(0, inplace=True)

fig, ax = plt.subplots(figsize=(10,10))
cl = result[['avg_vote','rank','lifetime_gross', 'duration']].corr()
sns.heatmap(cl, square = True, ax=ax)
result.rename(columns=lambda x: x.strip())
result = result.loc[:,~result.columns.duplicated()]

result.columns = result.columns.str.strip()
totalList=result.columns.tolist()
totalList

countryList=[]
for i in range(14,len(totalList)):
    countryList.append(totalList[i])

fig, ax = plt.subplots(figsize=(10,10))
cl = result[['United States',
 'Canada',
 'New Zealand',
 'Great Britain',
 'Germany',
 'Spain',
 'Malta',
 'France',
 'Denmark',
 'Indonesia',
 'China',
 'Belgium',
 'Australia',
 'Chile',
 'Afganistan',
 'Iraq',
 'Kenya',
 'Somalia',
 'Yemen',
 'South Korea',
 'Hong Kong',
 'Philippines',
 'India',
 'South Africa',
 'Ecuador',
 'Polinesia Francese',
 'Netherlands',
 'Netherlands Antilles',
 'Panamá',
 'Ukraine',
 'Japan',
 'Turkey',
 'Ireland',
 'Czech Republic',
 'Jordan',
 'Argentina',
 'Peru',
 'Thailand',
 'Hungary',
 'Austria',
 'Brazil',
 'Croatia',
 'Russia',
 'Italy',
 'Romania',
 'Sweden',
 'Poland',
 'American Samoa',
 'Norway',
 'Finland',
 'Singapore',
 'Syria',
 'Luxembourg',
 'Iceland',
 'Mexico',
 'Israel',
 'Portugal',
 'Morocco',
 'Taiwan',
 'Switzerland',
 'Lithuania']].corr()
sns.heatmap(cl, square = True, ax=ax)
