import csv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
tweets = []
with open('tweets/jpm/jpm_11-12_clean.csv', 'r', encoding="ISO-8859-1") as f:
	spamreader = csv.reader(f)
	for row in spamreader:
		for i in row:
		print("new row: ", word_tokenize(row[1]))
		# tweets.append(row)
# print(tweets)