import os
import io
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def readFiles(path):
    for root, dirnames, filenames in os.walk(path):  
        for filename in filenames:
            path = os.path.join(root, filename)
            print(dirnames)
            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message


def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    return DataFrame(rows, index=index)

data = DataFrame({'message': [], 'class': []})

data = data.append(dataFrameFromDirectory('C:/Users/xh0728/Desktop/DataScience/DataScience-Python3/emails/spam', 'spam'))
data = data.append(dataFrameFromDirectory('C:/Users/xh0728/Desktop/DataScience/DataScience-Python3/emails/ham', 'ham'))

###
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)   #this vectorizer instance will be used for test data as well
print(counts)          #words are represented with numerical index
classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)   #create model on classifer

###
examples = ['Free Viagra now!!!', "Hi Bob, how about a game of golf tomorrow?"]   #two input messages
example_counts = vectorizer.transform(examples)     #convert the message to the same format with the same vectorizer
predictions = classifier.predict(example_counts)    #model.predict
print(example_counts)   #first one is categorized as spam, while the second one is ham.
print(predictions)
