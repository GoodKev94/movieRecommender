import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity as sklearn_cosine_similarity
import sys

def getGenomeRelevanceSimilars(movieId):

	movieData = pd.read_csv('data/movies.csv')
	genomeMatrixdf = pd.read_csv('data/generatedGenomeMatrix.csv')


	genomeMatrixRelevanceScores = genomeMatrixdf.drop('movieId', axis = 1)
	genomeMatrixMovieIds = genomeMatrixdf['movieId']

	movieIdIndex = genomeMatrixMovieIds[genomeMatrixMovieIds == movieId].index[0]

	genomeCosineSimilarity = pd.DataFrame(sklearn_cosine_similarity(genomeMatrixRelevanceScores))

	similarMovieIndicies = genomeCosineSimilarity[movieIdIndex].sort_values(axis = 0, ascending = False).head(20).index
	similarMovieIds = genomeMatrixMovieIds.iloc[similarMovieIndicies]


	print(movieData.loc[movieData['movieId'].isin(similarMovieIds)])


if __name__ == '__main__':
	getGenomeRelevanceSimilars(int(sys.argv[1]))










