Movie Recommender
by Kevin Bichoupan

Purpose
========

This project is used to help recommend movies



Data
=======

The data for this project is sourced from grouplens (https://grouplens.org/datasets/movielens/)

Data contents include a list of movies, movie ratings, movie tags, and a relevance score for each movie for each tag.



Scripts
======

##movieDataStage.py

This file is meant for a one time run. It currently pivots the file genome-scores.csv to a structure in which:
	columns = genome tags
	rows = movies
	values = relevance score

New table structure is then written to the csv generatedGenomeMatrix.csv


-------------------------
movieGenomeSimilarity.py
-------------------------

This file identifies similar movies to an inputted movie.  Sklearn-cosine similarity is used 

Input: 
	(user input) movieId for a specific movie identified in the file movies.csv
	(file input) movies.csv
	(file input) generatedGenomeMatrix.csv

Execution: command line exection as follows 
	--> python movieGenomeSimilarity.py <movieId>

Methodology:
	Cosine Similarity algorithm is used in the sci-kit learn package to identify movies which are similar to the inputted movieId based on the genome tags and relevance scores found in the original file genome-scores.csv.  The input for this file is the generatedGenomeMatrix.csv file which is pre-generated using movieDataStage.py

Output: Top 20 movies similar to inputted movie







