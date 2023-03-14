from textblob.classifiers import NaiveBayesClassifier
from os.path import exists
import nltk
import config

if not exists(config.CLASSIFIER_FILE_NAME):
    print('You need to train model first')
    quit()

nltk.download('punkt')
with open('test.json', 'r') as testFile:
    print('------ Accuracy test ------')
    classifier = config.getClassifier()
    print(f'{classifier.accuracy(testFile, format="json")}')
    testFile.close()
