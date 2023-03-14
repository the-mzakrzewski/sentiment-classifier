from textblob.classifiers import NaiveBayesClassifier
import config
import nltk

nltk.download('punkt')

trainFile = open('train.json', 'r')
classifier = NaiveBayesClassifier(trainFile, format='json')
sentence = input("Enter sentence to check: ")

config.saveClassifier(classifier)

result = classifier.prob_classify(sentence)
print(f'This sentence is positive: {result.prob("pos")}')
print(f'This sentence is negative: {result.prob("neg")}')

trainFile.close()
