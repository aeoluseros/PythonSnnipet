import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('C:/Users/xh0728/Desktop/DataScience/DataScience-Python3/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('C:/Users/xh0728/Desktop/DataScience/DataScience-Python3/ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(ratings, movies)
ratings.sort_values("user_id").head()  #user_id is a fake one created by myself; sort_values is not in-place sort

userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
userRatings.head()

corrMatrix = userRatings.corr()
corrMatrix.head()

# use the min_periods argument to throw out results where fewer than 100 users rated a given movie pair
corrMatrix = userRatings.corr(method='pearson', min_periods=100) #pearson is the default
    # pearson : standard correlation coefficient
    # kendall : Kendall Tau correlation coefficient
    # spearman : Spearman rank correlation
corrMatrix.head()

# movie recommendations for user ID 0
# use dropna() to get rid of missing data (leaving me only with a Series of the movies I actually rated:)
myRatings = userRatings.loc[0].dropna()
myRatings

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]], index=['cobra', 'viper', 'sidewinder'], columns=['max_speed', 'shield'])
df
# .loc[] is primarily label based, but may also be used with a boolean array.
df.loc[['cobra', 'viper', 'sidewinder']]
df.loc['cobra']
df.loc['cobra', 'shield']

# for each movie I (user_id = 0) rated, I'll retrieve the list of similar movies from our correlation matrix. I'll then scale those correlation scores by how well I rated the movie they are similar to, so movies similar to ones I liked count more than movies similar to ones I hated
simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    print ("Adding sims for " + myRatings.index[i] + "...")
    # Retrieve similar movies to this one that I rated
    sims = corrMatrix[myRatings.index[i]].dropna()
    # Now scale its similarity by how well I rated this movie
    sims = sims.map(lambda x: x * myRatings[i])
    # Add the score to the list of similarity candidates
    simCandidates = simCandidates.append(sims)
    
#Glance at our results so far:
print ("sorting...")
simCandidates.sort_values(inplace = True, ascending = False)
print (simCandidates.head(10))

# Note that some of the same movies came up more than once, because they were similar to more than one movie I rated. We'll use groupby() to add together the scores from movies that show up more than once, so they'll count more
simCandidates = simCandidates.groupby(simCandidates.index).sum()

# filter out movies I've already rated, as recommending a movie I've already watched isn't helpful
filteredSims = simCandidates.drop(myRatings.index)
filteredSims.head(10)

# It looks like some movies similar to Gone with the Wind - which I hated - made it through to the final list of recommendations. 
# Perhaps movies similar to ones the user rated poorly should actually be penalized, instead of just scaled down?
# For an even bigger project: we're evaluating the result qualitatively here, but we could actually apply train/test and measure our ability to predict user ratings for movies they've already watched. Whether that's actually a measure of a "good" recommendation is debatable, though!



