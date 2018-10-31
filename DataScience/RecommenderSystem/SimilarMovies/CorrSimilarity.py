import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('C:/Users/xh0728/Desktop/DataScience/DataScience-Python3/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('C:/Users/xh0728/Desktop/DataScience/DataScience-Python3/ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)   #it will auto-detect the movie_id
ratings.head()

movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
print(movieRatings.shape)
movieRatings.head()

similarMovies = movieRatings.corrwith(movieRatings['Star Wars (1977)'])
#print(similarMovies)
similarMovies = similarMovies.dropna()
#print(similarMovies)
df = pd.DataFrame(similarMovies)
#print(df)
df.head(10)

similarMovies.sort_values(ascending=False)

import numpy as np
movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
movieStats.head()

popularMovies = movieStats['rating']['size'] >= 100
movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15]

df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity'])) #columns is assign name to column of df similarmovices. this is also how panda dataframe add the colum name.

df.head()

df.sort_values(['similarity'], ascending=False)[:15]




