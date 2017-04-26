# http://www.nltk.org/howto/sentiment.html
# Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import csv
import glob
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# nltk.download()

n_instances = 100
subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]
len(subj_docs), len(obj_docs)

subj_docs[0]

train_subj_docs = subj_docs[:80]
test_subj_docs = subj_docs[80:100]
train_obj_docs = obj_docs[:80]
test_obj_docs = obj_docs[80:100]
training_docs = train_subj_docs+train_obj_docs
testing_docs = test_subj_docs+test_obj_docs

sentim_analyzer = SentimentAnalyzer()
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])

unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
# len(unigram_feats)
sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)

training_set = sentim_analyzer.apply_features(training_docs)
# print ("Training Set = ", training_set)
test_set = sentim_analyzer.apply_features(testing_docs)

trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)
# for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
# 	print('{0}: {1}'.format(key, value))


# print ("Fields = ", subjectivity.fileids())
# # ['plot.tok.gt9.5000', 'quote.tok.gt9.5000']
# print ("\n\nNumber of words = ", len(subjectivity.words()))
# # Number of words =  240576
# print ("Categories = ", subjectivity.categories())
# # Categories =  ['obj', 'subj']


def sentiment():
	path = "*.csv"
	daily_sentiment = ['AAPL Sentiment']

	for file_name in glob.glob(path):
		tweets = []
		with open(file_name, 'r', encoding="ISO-8859-1") as f:
			spamreader = csv.reader(f)
			for row in spamreader:
				tweets.append(row[1][:-1])
		# sentences.extend(tricky_sentences)
		def calc_daily_score():
			sid = SentimentIntensityAnalyzer()
			counter = 0
			compound_total = 0
			for sentence in tweets:
				ss = sid.polarity_scores(sentence)
				counter += 1
				compound_total += ss["compound"]
			daily_score = compound_total / counter
			return daily_score

		daily_sentiment.append(calc_daily_score())

	return daily_sentiment


# print ("\nDaily Sentiment = ", sentiment())
sentiment()








