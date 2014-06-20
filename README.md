Spam-filter
===========

Basics
----------

Uses NLTK for natural language operations such as tokenizing and lemmatizing. Naive Bayes classification is used to classify emails into ham or spam based on training data from SpamAssassin's public corpus.

The features are tokens of whole emails. The Naive Bayes classification works well with the raw emails. The emails could obviously be parsed further, e.g. languages, HTML, URL's, headers, etc.

The filter returns the email name and its classification.


Files
----------

Create directories files/ham-training-data and files/spam-training-data
Place ham and spam emails in the respective directories. Currently, training data is present.

Also, create the directory files/emails and place emails to be filtered in it. Currently, test emails are present.

The data are taken from SpamAssassin's public corpus.

files/ham-training-data contains all email files from 20021010_hard_ham.tar, 20030228_easy_ham_2.tar, 20030228_easy_ham.tar, 20030228_hard_ham.tar

files/spam-training-data contains all email files from 20030228_spam_2.tar, 20030228_spam.tar, 20050311_spam_2.tar

files/emails contains emails from the files/ham-test and files/spam-test directories.
Files 0010 to 0020 are ham emails and files 0030 to 0040 are spam emails. Only a small number of files are in files/emails for easier testing.

The files can of course be switched around.

Usage:

1) Run classifier.py
2) Run filter.py

classifier.py
----------

classifier.py creates and saves the classifier for later usage by filter.py

python classifier.py <ham-training-directory> <spam-training-directory>

ex. python classifier.py ../files/ham-training-directory ../files/spam-training-directory

Directories files/ham-training-data and files/spam-training-data have already been created with respective ham and spam emails in them.
The directory for emails to be classified/filtered is files/emails and it has emails to be filtered in it.

The classifier is created using the ham and spam email data. To check accuracy, a 70:30 training:testing ratio is used. The classifier is then saved in the src directory.


filter.py
----------

filter.py has several functionalities: all, indie or range.

all: the filter returns a list of tuples containing the email id (email name) as well as its classification (ham or spam) for all emails in the files/emails directory.

indie: the filter returns a list of tuples containing the email id (email name) as well as its classification (ham or spam) for the specified emails.

range: the filter returns a list of tuples containing the email id (email name) as well as its classification (ham or spam) for the specified email and the number of emails after it as specified. For example, if the inputs are <email1> and <3>, the classifications for <email1> as well as <email2> and <email3> as is present in the files/emails directory will be returned.

For all emails:
python filter.py all

For individual emails:
python filter.py indie <email1> <email2> <email3> ...
The <email> refer to the file names in files/email/*

ex. python filter.py indie 0013.ff597adee000d073ae72200b0af00cd1 0017.d81093a2182fc9135df6d9158a8ebfd6

For a range of emails:
python filter.py range <email> <number>

ex. python filter.py range 0032.081c3615bc9b91d09b6cbb9239ba8c99 4