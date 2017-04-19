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


# Example of tokenizing
example_text = 'Hi there, how are you doing today. Python is awesome. The sky is blue.'
# print(sent_tokenize(example_text))


#Example of how to filter out stop words
example_sent = 'This is an example showing off stop word filtration.'
stop_words = set(stopwords.words('english'))

words = word_tokenize(example_sent)

# filtered_sentence  = []
# for w in words:
# 	if w not in stop_words:
# 		filtered_sentence.append(w)
filtered_sentence = [w for w in words if not w in stop_words]
# print(filtered_sentence)


#Stemming
ps = PorterStemmer()
# example_words = ['python', 'pythoner', 'pythoning', 'pythoned', 'pythonly']
new_text = 'It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once.'
# for w in example_words:
# 	print(ps.stem(w))
words = word_tokenize(new_text)
# for w in words:
# 	# print(ps.stem(w))


#Part of Speech Tagging, Chunking, Chinking
train_text = state_union.raw('2005-GWBush.txt')
sample_text = state_union.raw('2006-GWBush.txt')
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)
# def process_content():
# 	try:
# 		for i in tokenized:
# 			words = nltk.word_tokenize(i)
# 			tagged = nltk.pos_tag(words)
# 			chunkGram = '''Chunk: {<.*>+}
# 			}<VB.?|IN|DT>+{''' #regular expressions
# 			chunkParser = nltk.RegexpParser(chunkGram)
# 			chunked = chunkParser.parse(tagged)
# 			print(chunked)
# 	except Exception as e:
# 		print(str(e))
# process_content()


#Name Entity Recognition
train_text = state_union.raw('2005-GWBush.txt')
sample_text = state_union.raw('2006-GWBush.txt')
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)
# def process_content():
# 	try:
# 		for i in tokenized:
# 			words = nltk.word_tokenize(i)
# 			tagged = nltk.pos_tag(words)
# 			named_ent = nltk.ne_chunk(tagged)
# 	except Exception as e:
# 		print(str(e))
# process_content()



#Lemmatizing: liek stemming but return a real word, the default is pos='n' for noun
lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize('better'))
# print(lemmatizer.lemmatize('better', pos='a'))



#Corpora
sample = gutenberg.raw('bible-kjv.txt')
tok = sent_tokenize(sample)
# print(tok[5:15])



# WordNet
syns = wordnet.synsets('program') #gets syns
print(syns)
syns[0].definition() #prints the definition
syns[0].examples() #gives an example of the word used in sentence



# Text Classification
documents = [(list(movie_reviews.words(fileid)), category)
			for category in movie_reviews.categories()
			for fileid in movie_reviews.fileids(category)]

# random.shuffle(documents)
all_words = []
for w in movie_reviews.words():
	all_words.append(w.lower())

all_words = nltk.FreqDist(all_words) # gets the frequency of each word in all_words
# all_words.most_common(15): prints the 15 most common words

word_features = list(all_words.keys())[:3000]

def find_features(document):
	words = set(document)
	features = {}
	for w in word_features:
		features[w] = (w in words)
	return features
# print(find_features(movie_reviews.words('neg/cv000_29416.txt')))
featuresets = [(find_features(rev), category) for (rev, category) in documents]

#positive data 
training_set = featuresets[:1900]
testing_set = featuresets[1900:]
#negative data
training_set = featuresets[100:]
testing_set = featuresets[:100]

classifier = nltk.NaiveBayesClassifier.train(training_set)#training the algo
print(nltk.classify.accuracy(classifier, testing_set))#testing accuracy of algo
classifier.show_most_informative_features(15)

#Pickle
save_classifier = open('niavebayes.pickle', 'wb')
pickle.dump(classifier, save_classifier) #dumps the classifier to the file in bytes
save_classifier.close()


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

# SVC_classifier = SklearnClassifier(SVC())
# SVC_classifier.train(training_set)
# print(nltk.classify.accuracy(SVC_classifier, testing_set))


#Combining algos to vote
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
# print(nltk.classify.accuracy(voted_classifier, testing_set))
# print('Classification:', voted_classifier.classify(testing_set[0][0]), 'confidence:', voted_classifier.confidence(testing_set[0][0]))
# print('Classification:', voted_classifier.classify(testing_set[1][0]), 'confidence:', voted_classifier.confidence(testing_set[1][0]))
# print('Classification:', voted_classifier.classify(testing_set[2][0]), 'confidence:', voted_classifier.confidence(testing_set[2][0]))

