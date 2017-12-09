#!/usr/local/bin/python3

"""
main function for prediction task
"""
import argparse  
import csv
import time

from headbytes import HeadBytes
from extpredict import SystemReader
from extpredict import NaiveTruthReader
from classify import ClassifierBuilder
from randbytes import RandBytes
from randhead import RandHead
from ngram import Ngram
from randngram import RandNgram

def main():

    parser = argparse.ArgumentParser(description='Run file classification experiments')

    parser.add_argument("dirname", type=str)
    parser.add_argument("--n", type=int, default=10, help="number of trials",dest="n")
    parser.add_argument("classifier", type=str,
                        help="classifier to use, (svc|logit|rf)")
    parser.add_argument("feature", type=str,
                        help="feature to use, (head|rand|randhead|ngram|randngram)")
    parser.add_argument("--split", type=float, default=0.8,help="test/train split ratio",dest="split")
    parser.add_argument("--out", type=str, default="out.csv", dest="outfile",
                        help="file to write out results to")
    parser.add_argument("--head-bytes", type=int, default=512,dest="head_bytes",
                        help="size of file head in bytes, default 512, used for head and randhead")
    parser.add_argument("--rand-bytes",type=int, default=512,dest="rand_bytes",
                        help="number of random bytes, default 512, used in rand, randhead, and randngram")
    parser.add_argument("--ngram",type=int, dest="ngram", default=1,help="n for the ngram")
 
    args = parser.parse_args()
    
    if args.classifier not in ["svc","logit","rf"]:
        print("Invalid classifier option %s" % args.classifier)
        return

    print("Potato")
    if args.feature == "head":
        features = HeadBytes(head_size=args.head_bytes)
    elif args.feature == "rand":
        features = RandBytes(number_bytes=args.rand_bytes)
    elif args.feature == "randhead":
        features = RandHead(head_size=args.head_bytes,rand_size=args.rand_bytes)
    elif args.feature == "ngram":
        features = Ngram(args.ngram)
    elif args.feature == "randngram":
        features = RandNgram(args.ngram, args.rand_bytes)
    else:
        print("Invalid feature option %s" % args.feature)
        return

    reader = NaiveTruthReader(features)
    #reader = SystemReader(args.dirname, features)
    experiment(reader, args.classifier, args.outfile, args.n, split=args.split) 
    
def experiment(reader, classifier_name, outfile, trials, split):

    """
    reader - System reader with feature already set
    classifier - a string specifying the classifier type (svc, logit, etc.)
    outfile - string with filename of output file
    """
    
    read_start_time = time.time()
    reader.run()
    read_time = time.time() - read_start_time

    classifier = ClassifierBuilder(reader, classifier=classifier_name, split=split)
   
    # with open(outfile, "w") as f:
        #f.close()

    for i in range(trials):
        print("Running", i, "/", trials, "th trial")

        classifier_start = time.time()
        classifier.train() 
        accuracy = classifier.test()
        classifier_time = time.time() - classifier_start

        with open(outfile, "a") as data_file:
            data_file.write(str(accuracy)+","+str(read_time)+","+str(classifier_time)+\
		            ","+reader.feature.name+","+classifier_name+"\n")

        if i != trials-1:
            classifier.shuffle()


if __name__ == '__main__':
    main()
