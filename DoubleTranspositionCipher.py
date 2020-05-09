from math import ceil
from math import floor
from collections import OrderedDict
import random 
import string

class DoubleTranspositionCipher:

    def __init__(self, text, key1, key2):
        self.text = text
        self.key1 = self.removeRepeatedLetters(key1.lower())
        self.key2 = self.removeRepeatedLetters(key2.lower())

    def getText(self):
        return self.text

    def getKey1(self):
        return key1

    def getKey2(self):
        return key2

    def transpose(self, aText, key):

        alphabet = string.ascii_letters
        columns = ceil(len(key))
        rows = ceil(len(aText)/len(key)) + 1
        nextLetter = 0
        grid = [[random.choice(alphabet) for i in range(columns)] for j in range(rows)] 
        
        for i in range(columns):
            grid[0][i] = key[i]

        for i in range(1, rows, 1):
            for j in range(columns):
                if(len(aText) != nextLetter):
                    grid[i][j] = aText[nextLetter]
                    nextLetter += 1
                else:
                    break
          
        key_sorted = "".join(sorted(key))
        index = 0
        transposed_text = ""

        while(index < columns):

            for i in range(columns):
                if(grid[0][i] == key_sorted[index]):
                    
                    for j in range(1, rows, 1):
                        transposed_text += grid[j][i]
            index += 1            
        
        return transposed_text

    def encrypt(self):
        
        return self.transpose(self.transpose(self.text, self.key1), self.key2)

    def unTranspose(self, aText, key):
        
        alphabet = string.ascii_letters
        columns = floor(len(aText)/len(key)) + 1
        rows = floor(len(key))
        nextLetter = 0
        
        key_sorted = "".join(sorted(key))
        
        grid = [[random.choice(alphabet) for i in range(columns)] for j in range(rows)] 
        
        extraLetters = (len(aText)/len(key)) % 1
        
        if(extraLetters != 0.0):
            lettersToEliminate = ceil(extraLetters * 10)
            aText = aText[:-int(lettersToEliminate)] 
        
        for i in range(rows):
            grid[i][0] = key_sorted[i]
        
        for i in range(rows):
            for j in range(1, columns, 1):
                if(len(aText) != nextLetter):
                    grid[i][j] = aText[nextLetter]
                    nextLetter += 1
                else:
                    break
        
        unTransposed_text = ""
        index = 0
        letterToGet = 1
        
        while(letterToGet < columns):
            
            for i in range(rows):
                if(key[index] == grid[i][0]):
                    unTransposed_text += grid[i][letterToGet]

            index += 1
            
            if(index == rows):
                index = 0
                letterToGet += 1
        
        return unTransposed_text

    def decrypt(self):
        decrypted_text = self.unTranspose(self.unTranspose(self.text, self.key2), self.key1)
        
        if(len(decrypted_text) != len(self.text)):
            extraLetters = floor(len(self.key1)/len(decrypted_text)  * 100)
            decrypted_text = decrypted_text[:-extraLetters]
            
        return decrypted_text

    def removeRepeatedLetters(self, key):
        return "".join(OrderedDict.fromkeys(key))
        

def test():
    
    aText = "Be at the third pillar from the left outside the lyceum theatre tonight at seven. If you are distrustful bring two friends."
    print("Original text:")
    print(aText, "\n")
    
    sentence = DoubleTranspositionCipher(aText, "Cryptographic", "Networksecurity")
    encrypted_sentence = sentence.encrypt()

    aText = encrypted_sentence
    decrypt_this_text = DoubleTranspositionCipher(aText, "Cryptographic", "Networksecurity")

    print("Encrypted:")
    print(encrypted_sentence, "\n")

    print("Decrypted:")
    print(decrypt_this_text.decrypt())


if __name__ == "__main__":
    test()

    
        

        
            
