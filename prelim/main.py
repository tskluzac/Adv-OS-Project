#!/usr/local/bin/python3

"""
main function for prediction task
"""
import argparse  
import numpy as np

from sklearn.svm import SVC
from headbytes import HeadBytes
from extpredict import SystemReader
from classify import ClassifierBuilder

def main():

    parser = argparse.ArgumentParser(description='Run file classification')
    parser.add_argument("dirname", type=str)
    args = parser.parse_args()
 
    features = HeadBytes() # the features for this test
    reader = SystemReader(args.dirname, features)
     
    reader.run()
    print("Directory scanned, found %i samples" % len(reader.data))
    classifier = ClassifierBuilder(reader, classifier="svc",split=0.5)
    print("Training classifier on %i samples with %i classes" % 
           (classifier.X_train.shape[0], len(features.class_table)))
    classifier.train()
    print("SVC classification using %s is %f" % (features.name, classifier.test()))

if __name__ == '__main__':
    main()
