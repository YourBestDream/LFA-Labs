class Grammar:
    def __init__(self):
        self.VN = ['S','B','C']
        self.VT = ['a','b','c']
        self.P = {
            'S':['aB'],
            'B':['aC','bB'],
            'C':['bB','c','aS']
        }