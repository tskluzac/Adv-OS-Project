"""
abstract base class for building features from files
Each new set of features should subclass this
"""

class FeatureMaker:
    """
    Takes a open file, and produces features
    """
    def __init__(self):
        self._name = "test"
    
    def get_feature(self, open_file):
        return open_file.name
