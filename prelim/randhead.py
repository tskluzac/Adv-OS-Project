import numpy as np

from os.path import getsize
from feature import FeatureMaker

class RandHead(FeatureMaker):
    """
    take the head (the first h bytes) and k random bytes 
    from subsequent sections
    """
    def __init__(self,head_size=512,rand_size=512):

        self.name = "randhead"
        self.head_size = head_size
        self.rand_size = rand_size
        self.nfeatures = head_size + rand_size
        self.class_table = {}
        self._head = HeadBytes(head_size=self.head_size)

    def get_feature(self, open_file):

        head = self._head.get_feature(open_file)
        
        size = getsize(open_file.name)
        rand_index = [randint(self.head_size, size-1) for _ in range(self.rand_size)]

        sort(rand_index)
        sample_bytes = head

        for index in rand_index:
            
            open_file.seek(index)
            sample_bytes.append(open_file.read(1))

        return sample_bytes

    def translate(self, entry):
        return self._head.translate(entry)
