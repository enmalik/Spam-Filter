"""
classifier.py creates and saves the classifier for later usage by filter.py

python classifier.py <ham-training-directory> <spam-training-directory>

Directories files/ham-training-data and files/spam-training-data have already been created with respective ham and smap emails in them.
The directory for emails to be classified/filtered is files/emails and it has emails to be filtered in it.

The classifier is created using the ham and spam email data. 
To check accuracy, a 70:30 training:testing ratio is used. 
The classifier is then saved in the src directory.
"""

from nltk import NaiveBayesClassifier, classify
import sys, random, os, glob
from aux import emailFeatures, saveClassifier

# Function to build classifier - inputs: ham-training-directory, spam-training-directory, classifier-name to save

def buildClassifier(hamDir, spamDir):
	spamEmails = []
	hamEmails = []
	allEmails = []
	features = []

	# Using glob instead of os.listdir to ignore hidden files

	for email in glob.glob(spamDir + "/*"):
		f = open(email)
		spamEmails.append(f.read())
		f.close()

	for email in glob.glob(hamDir + "/*"):
		f = open(email)
		hamEmails.append(f.read())
		f.close()

	for email in spamEmails:
		allEmails.append((email, 'spam'))

	for email in hamEmails:
		allEmails.append((email, 'ham'))

	# Shuffle to get the accuracy of the 70:30 ratio. Otherwise, if no check were to be done, would not need to shuffle.
	random.shuffle(allEmails)

	# Make a list of feature per email
	for (email, label) in allEmails:
		features.append((emailFeatures(email), label))

	# 70:30 ratio for training:testing
	print "Using a 70:30 ratio for training:testing, the accuracy is as follows: "
	totalSize = int(len(features) * 0.7)
	trainingEmails, testingEmails = features[:totalSize], features[totalSize:]

	print "training size: %d; testing size: %d" %(len(trainingEmails), len(testingEmails))
	classifier = NaiveBayesClassifier.train(trainingEmails)
	print classify.accuracy(classifier, testingEmails)

	print "Now creating and saving a full size classifier made up of %d emails..." %len(features)
	classifier = NaiveBayesClassifier.train(features)

	saveClassifier(classifier, "full-classifier.pickle")

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print "Please enter the correct arguments: python Classifier.py <ham-training-directory> <spam-training-directory>"
	elif os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2]):
		buildClassifier(os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]))
	else:
		print "Directories don't exist."