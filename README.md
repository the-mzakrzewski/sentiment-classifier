# Sentiment Analysis with TextBlob

This project contains Python code for sentiment analysis using the TextBlob library. The code demonstrates how to train a naive Bayes classifier to classify text as positive or negative, and includes sample data for testing and accuracy evaluation. The project also includes examples of how to preprocess text data and perform basic exploratory data analysis.

## Getting Started

To run the project, you'll need to have Python installed on your machine. Clone the repository and navigate to the root directory:

````commandline
git clone https://github.com/the-mzakrzewski/sentiment-classifier
cd your-repository
````

## Train the Model

To train the model, run the `train_model.py` script:

````commandline
python train_model.py
````

This script trains a naive Bayes classifier on the sample data in `train.json` and saves the trained model to a file named `sentiment_classifier.pickle`.

## Test Accuracy

To test the accuracy of the trained model, run the `accuracy_test.py` script:

````commandline
python accuracy_test.py
````

This script evaluates the accuracy of the trained model on the sample test data in `test.json` and prints the accuracy score to the console.

**Note**: The datasets provided in this project are for demonstration purposes only and may not be representative of real-world data. It is recommended that you use your own datasets to train and test your sentiment analysis model.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- The TextBlob library for providing a simple and intuitive way to perform natural language processing in Python.
- The creators of the sample datasets used in this project for providing publicly available data for demonstration purposes.
