"""
filter.py has several functionalities: all, indie or range.

all: the filter returns a list of tuples containing the email id (email name) 
as well as its classification (ham or spam) for all emails in the files/emails directory.

indie: the filter returns a list of tuples containing the email id (email name) 
as well as its classification (ham or spam) for the specified emails.

range: the filter returns a list of tuples containing the email id (email name) 
as well as its classification (ham or spam) for the specified email and the number of emails after it as specified. 
For example, if the arguments are <email1> and <3>, the classifications for <email1> as well as <email2> and <email3> 
as is present in the files/emails directory will be returned.

For all emails:
python filter.py all

For individual emails:
python filter.py indie <email1> <email2> <email3> ...
The <email> refer to the file names in files/email/*

For a range of emails:
python filter.py range <email> <number>
"""

from nltk import NaiveBayesClassifier, classify
import os, glob
from aux import emailFeatures, loadClassifier
import sys

# Set the email directory.
emailDir = os.path.abspath("../files/emails")

# Classify all emails in the email directory.
def filterEmailAll():
	classifier = loadClassifier("full-classifier.pickle")

	allEmails = []
	classifications = []

	emailList = glob.glob(emailDir + '/*')

	for i in range(len(emailList)):
		emailPath = emailList[i]
		classifications.append(filterEmail(classifier, emailPath))

	return classifications

# Classification of a single email, called by both filterIndies and filterRange.
def filterEmail(classifier, path):
	f = open(path)
	email = f.read()
	f.close()

	return (path.rsplit('/')[-1], classifier.classify(emailFeatures(email)))

# Classifies individual emails. Can classify as many emails as specified.
def filterIndies(emailIDs):
	global emailDir

	classifier = loadClassifier("full-classifier.pickle")
	classifications = []

	for i in range(len(emailIDs)):
		emailIDs[i] = emailDir + "/" + emailIDs[i]
		emailPath = emailIDs[i]

		if not os.path.exists(emailPath):
			print "Email '%s' does not exist." %emailPath.rsplit('/')[-1]
			continue

		classifications.append(filterEmail(classifier, emailPath))

	return classifications

# Classifies a range of emails following the specified email.
def filterRange(emailID, num):
	global emailDir
	emailList = os.listdir(emailDir)
	emailIndex = emailList.index(emailID)
	emailRange = emailList[emailIndex : emailIndex + int(num)]

	classifier = loadClassifier("full-classifier.pickle")
	classifications = []

	for i in range(len(emailRange)):
		emailRange[i] = emailDir + "/" + emailRange[i]
		emailPath = emailRange[i]

		if not os.path.exists(emailPath):
			print "Email '%s' does not exist." %emailPath.rsplit('/')[-1]
			continue

		classifications.append(filterEmail(classifier, emailPath))

	return classifications

if __name__ == "__main__":
	if sys.argv[1] == "all":
		print "All emails!"
		print filterEmailAll()
	elif len(sys.argv) < 2:
		print "Please indicate indie or range along with the emails."
	elif sys.argv[1] == "indie" and len(sys.argv) >= 3:
		print "Individual emails!"
		print filterIndies(sys.argv[2:])
	elif sys.argv[1] == "range" and len(sys.argv) == 4:
		print "Range of emails!"
		print filterRange(sys.argv[2], sys.argv[3])
	else:
		print "Please enter the corrent arguments."