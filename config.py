import pickle

CLASSIFIER_FILE_NAME = "classifier_trained.pickle"


def getClassifier():
    f = open(CLASSIFIER_FILE_NAME, "rb")
    classifier = pickle.load(f)
    f.close()
    return classifier


def saveClassifier(classifier):
    f = open(CLASSIFIER_FILE_NAME, 'wb')
    pickle.dump(classifier, f)
    f.close()
