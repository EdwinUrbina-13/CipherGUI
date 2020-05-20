#Caesar's Cipher Class
#The Caesar Cipher is a shift cipher, one of the most easy and most famous encryption systems.
# It uses the substitution of a letter by another one further in the alphabet.

class CaesarCipher:
    #Max alphabet letters
    keyMax = 26

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

    #Caesar Cipher
    def caesar(self, text, key):
        """The Caesar Cipher is a shift cipher, one of the most easy and most famous encryption systems.
        It uses the substitution of a letter by another one further in the alphabet."""
        key = int(key)
        aString = ''

        for symbol in text: #Verify if string character is an alphabet letter
            if symbol.isalpha():
                num = ord(symbol) #Converts character to its numeric representation
                num += key

                #Verifies if upper case and encrypt/decrypt
                if symbol.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                #Verifies if lower case and encrypt/decrypt
                elif symbol.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26
                #Converts character's numeric representation back to the actual character
                aString += chr(num)
            else:
                aString += symbol
        #Returns encrypted/decrypted text
        return aString

    def encrypt(self):
        """Runs a Caesar Cipher using the given key. Finally it returns the encrypted text"""

        encrypted_text = self.caesar(self.text, self.key)
        return encrypted_text

    def decrypt(self):
        """Runs a decrypt Caesar Cipher using the given key. Finally it returns the decrypted text."""
        #self.key is negative beuase if it is being decrypted the key goes backwards in alphabet
        key = -int(self.key)
        decrypted_text = self.caesar(self.text, key)
        return decrypted_text

def test():
    """Test is used to test the modules ability to encrypt and decrypt text"""

    aString = "Oceans and lakes have much in common, but they are also quite different. " \
              "Both are bodies of water, but oceans are very large bodies of salt water, while lakes are much smaller bodies of fresh water. " \
              "Lakes are usually surrounded by land, while oceans are what surround continents. Both have plants and animals living in them. " \
              "The ocean is home to the largest animals on the planet, whereas lakes support much smaller forms of life. " \
              "When it is time for a vacation, both will make a great place to visit and enjoy."
    print("Original text:")
    print(aString, "\n")

    sentence = CaesarCipher(aString, 4)
    encrypted_sentence = sentence.encrypt()
    aString = encrypted_sentence

    decrypt_text = CaesarCipher(aString, 4)

    print("Encrypted:")
    print(encrypted_sentence, "\n")

    print("Decrypted:")
    print(decrypt_text.decrypt())

if __name__ == "__main__":
    test()