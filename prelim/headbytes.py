from feature import FeatureMaker

class HeadBytes(FeatureMaker):
    def __init__(self, head_size=512):
        self.name = "head"
        self.head_size = head_size

    def get_feature(self, open_file):
        
        byte = open_file.read(1) 
        read = 1  
        head = [] 
        print(type(byte))
        while byte and read < self.head_size:
            head.append(byte)
            read += 1
            byte = open_file.read(1)

        if len(head) < self.head_size:
            head.extend([b'' for i in range(self.head_size - len(head))])
        assert len(head) == self.head_size
        return head
