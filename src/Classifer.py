from nltk import NaiveBayesClassifier, classify
import random, os, glob, re
from aux import emailFeatures, saveClassifier

# print commonWords

# MAKE ALL THE ONE LINER FOR LOOPS INTO ACTUAL LOOPS

def buildClassifier():
	spamEmails = []
	hamEmails = []
	allEmails = []
	features = []

	for email in glob.glob('../files/spam/*'):
		fin = open(email)
		spamEmails.append(fin.read())
		fin.close()

	for email in glob.glob('../files/ham/*'):
		fin = open(email)
		hamEmails.append(fin.read())
		fin.close()

	for email in spamEmails:
		allEmails.append((email, 'spam'))

	for email in hamEmails:
		allEmails.append((email, 'ham'))

	random.shuffle(allEmails)

	for (email, label) in allEmails:
		features.append((emailFeatures(email), label))

	# 70:30 ratio for training:testing
	print "Using a 70:30 ratio for training:testing, the accuracy is as follows: "
	totalSize = int(len(features) * 0.7)
	trainingEmails, testingEmails = features[:totalSize], features[totalSize:]

	print "train size: %d; testing size: %d" %(len(trainingEmails), len(testingEmails))
	classifier = NaiveBayesClassifier.train(trainingEmails)
	print classify.accuracy(classifier, testingEmails)

	print "Now creating and saving a full size classifier made up of %d emails..." %len(features)
	classifier = NaiveBayesClassifier.train(features)

	saveClassifier(classifier, "updated-classifier.pickle")


	# features = emailFeatures(hamTexts[0])
	# print features





if __name__ == "__main__":
	buildClassifier()