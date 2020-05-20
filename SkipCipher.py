#Skip Cipher Class
#The Skip Cipher reorders the letters of a message by selecting them after a N character jump.

class SkipCipher:
    def __init__(self, text, key):
        # Assigns text to self.text
        self.text = text
        # Assigns key to self.key
        self.key = key

    def getText(self):
        """Returns the text given by the user"""
        return self.text

    def getKey(self):
        """Returns key given by user"""
        return self.key

    #Recursive function to return gcd of two numbers
    #Needed for coprime function
    def gcd(self,a, b):
        # Everything divides 0
        if (a == 0 or b == 0): return 0

        # base case
        if (a == b): return a

        # a is greater
        if (a > b):
            return self.gcd(a - b,b)

        return self.gcd(a,b - a)

    #Verify if two (text length and key) numbers are co-prime
    #It is necessary to use a jump value that is coprime with the length of the message
    def coprime(self,a,b):

        if (self.gcd(a,b) == 1):
            return True
        else:
            return False

    #Skip Cipher
    def skip(self, aString, key):
        """The Skip method reorders the letters of a
        message by selecting them after a N character jump. """
        key = int(key)
        if self.coprime(len(aString), key)== True:
            length = len(aString)
            text = ''
            count = 0
            pos = 0
            #Selects the nth character and adds it to new text
            while count < length:
                pos = (pos) % length
                text = text + aString[pos]
                count = count + 1
                pos = pos + key
            return text
        else:
            print("Sorry, " + str(key) + " is not coprime with text length.")

    def encrypt(self):
        """Runs a skip using the given key. Finally it returns the encrypted text"""

        encrypted_text = self.skip(self.text, self.key)
        return encrypted_text

    def unSkip(self,aString, key):
        """The unSkip method reorders the letters of a
        message by indexing the message characters in order with the jump. """
        key = int(key)
        if self.coprime(len(aString), key)== True:
            length = len(aString)
            decStr = []
            #Creates list to order characters in their respective indexes
            for x in range(1000):
                decStr.append('')
            i = 1
            text = ""
            #Gets character index and adds it to the decrypted string
            while i <= length:
                idx = ((i - 1) * key) % length
                decStr[idx] = aString[i - 1]
                i = i + 1
            return text.join(decStr) #Gets list characters as string
        else:
            print("Sorry, " + str(key) + " is not coprime with text length.")

    def decrypt(self):
        """Runs an unSkip using the given key. Finally it returns the decrypted text."""
        decrypted_text = self.unSkip(self.text, self.key)
        return decrypted_text

def test():
    """Test is used to test the modules ability to encrypt and decrypt text"""

    aString = "Sunset is the time of day when our sky meets the outer space solar winds. " \
              "There are blue, pink, and purple swirls, spinning and twisting, like clouds of balloons caught in a whirlwind." \
              "The sun moves slowly to hide behind the line of horizon, while the moon races to take its place in prominence atop the night sky. " \
              "People slow to a crawl, entranced, fully forgetting the deeds that must still be done. " \
              "There is a coolness, a calmness, when the sun does set."
    print("Original text:")
    print(aString, "\n")

    sentence = SkipCipher(aString, 7)
    encrypted_sentence = sentence.encrypt()

    aString = encrypted_sentence
    decrypt_text = SkipCipher(aString, 7)

    print("Encrypted:")
    print(encrypted_sentence, "\n")

    print("Decrypted:")
    print(decrypt_text.decrypt())


if __name__ == "__main__":
    test()