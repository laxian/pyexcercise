class VigenereAutokeyCipher:
    def __init__(self, key, abc):
        self.key = key
        self.abc = abc

    def encode(self, text):
        for i in range(0,len(text)):
            print(self.key[i%len(self.key)])

    def decode(self, text):
        pass


VigenereAutokeyCipher('PASSWORD','ABCDEFGHIJKLMNOPQRSTUVWXYZ').encode('AAAAAAAAPASSWORDAAAAAAAA')