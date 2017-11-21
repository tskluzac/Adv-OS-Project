import numpy as np
from random import shuffle
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

class ClassifierBuilder(object):

    """
    Classifier builder takes a system reader, and uses that
    to build a cross-validated classifier. We use the feature
    makers' to_np method to convert the list rows to an acceptable
    numpy array based format
    """

    def __init__(self, reader, classifier="svc",split=0.8):
        """
        reader - the system reader object, must have data already
                 loaded into it (though we could change later)
        classifier - the classifier type to be used, options are 
                        "svc" - support vector classifier
                        "logit" - logistic regression
                        "rf" - random forest 
        split - a decimal between 0 and 1 which indicates how much
                of the data should be used as training. The rest is used
                as a testing set.
        """
        self.classifier_type = classifier
        self.model = None

        # randomly partition data, add method to shuffle w/in classifier
        # so we don't need to translate multiple times after this.

        data = [line for line in reader.data]
        shuffle(data)

        split_index = int(split*len(data))
        
        train_data = data[:split_index]
        test_data = data[split_index:]

        self.X_train = np.zeros((len(train_data), reader.feature.nfeatures))
        self.Y_train = np.zeros(len(train_data))

        self.X_test = np.zeros((len(test_data), reader.feature.nfeatures))
        self.Y_test = np.zeros(len(test_data))

        groups = [[train_data, self.X_train, self.Y_train],
                  [test_data, self.X_test, self.Y_test]]

        for group in groups:
            raw_data,X,Y = group
            for i in range(len(raw_data)):
                x,y = reader.feature.translate(raw_data[i])
                X[i] = x
                Y[i] = y

    def train(self):

        # TODO: as we fiddle with these, should add options to adjust classifier parameters

        if self.classifier_type == "svc":
            self.model = SVC()
        elif self.classifier_type == "logit":
            self.model = LogisticRegression()
        elif self.classifier_type == "rf":
            self.model = RandomForestClassifier()

        self.model.fit(self.X_train, self.Y_train)

    def test(self):
       
        """
        evaluate the model on the testing set
        """

        return self.model.score(self.X_test, self.Y_test)
