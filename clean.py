import csv
from nltk.tokenize import word_tokenize
from nltk.corpus import twitter_samples
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords, state_union, gutenberg, wordnet, movie_reviews
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
import random
import pickle


print(twitter_samples.fileids())
a = twitter_samples.strings('negative_tweets.json')
b = []
for i in a:
	b.append(('neg', i))

print(b[1])
all_words = set(word.lower() for passage in b for word in word_tokenize(passage[0]))
t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in b]
# print(t)

# documents = [(list(twitter_samples.words(fileid)), category)
# 			for category in twitter_samples.categories()
# 			for fileid in twitter_samples.fileids(category)]
# print(documents)

tweets = []
with open('tweets/jpm/jpm_11-12_clean.csv', 'r', encoding="ISO-8859-1") as f:
	spamreader = csv.reader(f)
	for row in spamreader:
		tweets.append(row[1][:-1])




training_set = t
testing_set = tweets
classifier = nltk.NaiveBayesClassifier.train(training_set)#training the algo
print(nltk.classify.accuracy(classifier, testing_set))#testing accuracy of algo
classifier.show_most_informative_features(15)

#Pickle
# save_classifier = open('niavebayes.pickle', 'wb')
# pickle.dump(classifier, save_classifier) #dumps the classifier to the file in bytes
# save_classifier.close()


# scikit-Learn
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print(nltk.classify.accuracy(MNB_classifier, testing_set))

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print(nltk.classify.accuracy(BernoulliNB_classifier, testing_set))

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print(nltk.classify.accuracy(SGDClassifier_classifier, testing_set))

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print(nltk.classify.accuracy(NuSVC_classifier, testing_set))

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print(nltk.classify.accuracy(LogisticRegression_classifier, testing_set))

class VoteClassifier(ClassifierI):
	def __init__(self, *classifiers):
		self._classifiers = classifiers

	def classify(self, features):
		votes = []
		for c in self._classifiers:
			v = c.classify(features)
			votes.append(v)
		return mode(votes)

	def confidence(self, features):
		votes = []
		for c in self._classifiers:
			v = c.classify(features)
			votes.append(v)
		choice_votes = votes.count(mode(votes))
		conf = choice_votes / len(votes)
		return conf

voted_classifier = VoteClassifier(MNB_classifier,
	BernoulliNB_classifier,
	SGDClassifier_classifier,
	NuSVC_classifier,
	LogisticRegression_classifier)
print(nltk.classify.accuracy(voted_classifier, testing_set))
print('Classification:', voted_classifier.classify(testing_set[0][0]), 'confidence:', voted_classifier.confidence(testing_set[0][0]))
print('Classification:', voted_classifier.classify(testing_set[1][0]), 'confidence:', voted_classifier.confidence(testing_set[1][0]))
print('Classification:', voted_classifier.classify(testing_set[2][0]), 'confidence:', voted_classifier.confidence(testing_set[2][0]))
