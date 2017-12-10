import numpy as np

from os.path import getsize
from feature import FeatureMaker
from random import randint
from itertools import product

class RandNgram(FeatureMaker):
    
    def __init__(self, n, k):
        """randomly sample k ngrams"""
        self.name = "randngram"+str(n)
        self.nfeatures = 257**n
        self.n = n
        self.k = k
        self.sequence_table = {}

        self.sequence_table = [0 for _ in range(257 ** n)]
        #for seq in product([a.to_bytes(1, "big") for a in range(256)]+[b''], repeat=n):
        #    self.sequence_table[seq] = len(self.sequence_table)

        self.class_table = {}

    def get_feature(self, open_file):

        size = getsize(open_file.name)

        if size < self.n:
            raise FileNotFoundError()

        rand_index = [randint(0, size-(self.n-1)) for _ in range(self.k)]
        #rand_index.sort()

        #feature = [0 for _ in self.sequence_table.keys()]
        feature = [0 for _ in len(self.sequence_table)]

        for index in rand_index:
            open_file.seek(index)

            """
            seq = []

            for _ in range(self.n):
                seq.append(open_file.read(1))

            feature[self.sequence_table[tuple(seq)]] += 1
            """

            seq = 0
            for _ in range(self.n):
                seq = seq * 257 + ord(open_file.read(1))
                print(ord(open_file.read(1)), seq)
            feature[seq] += 1 / self.k

        return feature

    def translate(self, entry):

        try:
            y = self.class_table[entry[-1]]
        except KeyError:
            self.class_table[entry[-1]] = len(self.class_table)
            y = self.class_table[entry[-1]]
    
        return np.array(entry[2]),y
