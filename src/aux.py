""" Some auxiliary functions put in here reduce clutter in Classifier and Filter. """

import pickle
from nltk import word_tokenize, NaiveBayesClassifier, classify, WordNetLemmatizer
from nltk.corpus import stopwords

# Lemmatization of the words reduces complexity while retaining meaning
wordLemmatizer = WordNetLemmatizer()
commonWords = stopwords.words('english')

# Save the classifier for later use - pass in the classifier and the name to be saved as
def saveClassifier(model, name):
   writeFile = open(name, 'wb')
   pickle.dump(model, writeFile)
   writeFile.close()

# Load a previously saved classifer - pass in name
def loadClassifier(name):
	loadFile = open(name, 'rb')
	model = pickle.load(loadFile)
	loadFile.close()

	return model

# Returns features for an email - a dict of all tokens
def emailFeatures(email):
	featureDict = {}

	for token in word_tokenize(email):
		lemma = wordLemmatizer.lemmatize(token.lower())
		if lemma not in commonWords:
			featureDict[lemma] = True

	return featureDict