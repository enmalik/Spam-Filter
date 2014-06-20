from nltk import NaiveBayesClassifier, classify
import os, glob, re
from aux import emailFeatures, loadClassifier
import sys

emailDir = os.path.abspath("../files/emails")

def filterEmail():
	classifier = loadClassifier("updated-classifier.pickle")

	allEmails = []
	classifications = []

	for email in glob.glob('../files/spam_filter_test/*'):
		fin = open(email)
		allEmails.append(fin.read())
		fin.close()

	for email in allEmails:
		classification = classifier.classify(emailFeatures(email))
		classifications.append(classification)

	print classifications

def filterEmail(path):
	emailPath = emailDir + "/" + emailID
	print emailPath

	if not os.path.exists(emailPath):
		print "Email does not exist."
		return

	classifier = loadClassifier("updated-classifier.pickle")

	allEmails = []
	classifications = []

	fin = open(emailPath)
	allEmails.append(fin.read())
	fin.close()

	for email in allEmails:
		classification = classifier.classify(emailFeatures(email))
		classifications.append((emailID, classification))

	print classifications

def filterRange(emailID, num):
	pass

def filterIndies(emailIDs):
	print len(emailIDs)
	print emailIDs

	for i in range(len(emailIDs)):
		emailIDs[i] = emailDir + "/" + emailIDs[i]
		emailPath = emailIDs[i]

		if not os.path.exists(emailPath):
			print "Email '%s' does not exist." %emailPath.rsplit('/')[-1]
			continue



	# for emailID in emailIDs:
	# 	emailID = emailDir + "/" + emailID

	# for email in emailIDs:
	# 	print email.rsplit('/')[-1]



if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Please indicate indie or range along with the emails."
	elif sys.argv[1] == "indie" and len(sys.argv) >= 3:
		print "Indie email!"
		filterIndies(sys.argv[2:])
	elif sys.argv[1] == "range" and len(sys.argv) == 4:
		print "Range email!"
	else:
		print "Please enter the corrent parameters"

	# filterEmail()