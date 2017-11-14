#!/usr/local/bin/python3

"""
main function for prediction task
"""
import argparse  
import numpy as np
from sklearn.svm import SVC
from headbytes import HeadBytes
from extpredict import SystemReader

def main():

    parser = argparse.ArgumentParser(description='Run file classification')
    parser.add_argument("dirname", type=str)
    args = parser.parse_args()
 
    features = HeadBytes() # the features for this test
    reader = SystemReader(args.dirname, features)
     
    reader.run()

    class_table = {}
    X_list = []
    Y_list = []

    for entry in reader.data:

        x = entry[2]
        X_list.append([int.from_bytes(c, byteorder="big") for c in x])

        try:
            y = class_table[entry[-1]]
        except KeyError:
            class_table[entry[-1]] = len(class_table)+1
            y = class_table[entry[-1]]
        Y_list.append(y)

    clf = SVC()
    clf.fit(np.array(X_list), np.array(Y_list))

    print(clf.score(X_list, Y_list))

if __name__ == '__main__':
    main()
