from math import ceil
from math import floor
from collections import OrderedDict
import random
import string


class DoubleTranspositionCipher:

    def __init__(self, text, key1, key2):
        # Assigns text to self.text
        self.text = text
        # Takes first key given by user, makes it lowercase, and removes repeated letters
        # Then assigns it to self.key1
        self.key1 = self.removeRepeatedLetters(key1.lower())
        # Takes second key given by user, makes it lowercase, and removes repeated letters
        # Then assigns it to self.key2
        self.key2 = self.removeRepeatedLetters(key2.lower())

    def getText(self):
        """Returns the text given by the user"""
        return self.text

    def getKey1(self):
        """Returns first key given by user"""
        return self.key1

    def getKey2(self):
        """Returns second key given by user"""
        return self.key2

    def transpose(self, aText, key):
        """The transposed method makes a 2d matrix were it makes the first row your key.
        After the key is set, it takes the given text and starts filling the rest of the matrix.
        Once the matrix is filled, it starts taking out a whole column at a time in alphabetical order and adds it to a string.
        The new text will be all distorted because everything will be out of order."""

        # Variable to hold a list of ascii letters
        alphabet = string.ascii_letters
        # Sets colums to the ceiling value of the length of the key
        columns = ceil(len(key))
        # Sets the rows to the ceiling result of the division of the legth of text by the length of key plus one
        rows = ceil(len(aText) / len(key)) + 1
        # nextLetter works as a counter to move throug the letters in a row
        nextLetter = 0

        # Creates a 2d matrix and assigns random letters taken from the 'alphabet' list
        grid = [[random.choice(alphabet) for i in range(columns)] for j in range(rows)]

        # Makes the key word the first row
        for i in range(columns):
            grid[0][i] = key[i]

        # Continues to insert the letters, numbers, and symbols of the text into the 2d matrix
        for i in range(1, rows, 1):
            for j in range(columns):
                if (len(aText) != nextLetter):
                    grid[i][j] = aText[nextLetter]
                    nextLetter += 1
                else:
                    break

        # Sorts the key in alphabetical order
        key_sorted = "".join(sorted(key))
        # Set index to 0
        index = 0
        # Defines transposed_text
        transposed_text = ""

        # While loop that lasts until all letters of the sorted key have been checked
        while (index < columns):
            # For loop that looks for the index of were the letter in the sorted key is in the first row
            for i in range(columns):
                if (grid[0][i] == key_sorted[index]):

                    # Takes out the column where that letter of the key is and adds it to 'transposed_text' (Doesn't add the key letter)
                    for j in range(1, rows, 1):
                        transposed_text += grid[j][i]

            # Increments index to look for the next column to add
            index += 1

            # Returns the transposed 2d matrix as a string
        return transposed_text

    def encrypt(self):

        """Runs an transpose using the first given key. Then it runs another transpose using the second key.
    Finally it returns the encrypted text"""

        return self.transpose(self.transpose(self.text, self.key1), self.key2)

    def unTranspose(self, aText, key):
        """The untransposed method makes a 2d matrix were it makes the first column your key sorted.
        After the sorted key is set, it takes the given text and starts filling the rest of the matrix.
        Once the matrix is filled, it starts taking out row by row the letters in the order of the
        original key and adds them to a string. The new text will be a cohesive text unless it has been encrypted more than once."""

        # Variable to hold a list of ascii letters
        alphabet = string.ascii_letters
        # Sets the columns to the ceiling result of the division of the legth of text by the length of key plus one
        columns = floor(len(aText) / len(key)) + 1
        # Sets rows to the ceiling value of the length of the key
        rows = floor(len(key))
        # nextLetter works as a counter to move throug the letters in a row
        nextLetter = 0

        # Sorts the key in alphabetical order
        key_sorted = "".join(sorted(key))

        # Creates a 2d matrix and assigns random letters taken from the 'alphabet' list
        grid = [[random.choice(alphabet) for i in range(columns)] for j in range(rows)]

        # Makes the sorted key word the first column
        for i in range(rows):
            grid[i][0] = key_sorted[i]

        # Continues to insert the letters, numbers, and symbols of the text into the 2d matrix
        for i in range(rows):
            for j in range(1, columns, 1):
                if (len(aText) != nextLetter):
                    grid[i][j] = aText[nextLetter]
                    nextLetter += 1
                else:
                    break

        # Defines transposed_text
        unTransposed_text = ""
        # Set index to 0
        index = 0
        # letterToGet is a counter to move through the columns of a specific row
        letterToGet = 1

        # While loop that lasts until the whole matrix is done being searched
        while (letterToGet < columns):

            # For loop with a range set to the maximum rows
            for i in range(rows):
                # If statement to match the letters of the original key to the place they are in the matrix
                if (key[index] == grid[i][0]):
                    # If the match is TRUE the value given by the row matched and
                    # the current letter to give is added to the unTransposed_text string
                    unTransposed_text += grid[i][letterToGet]

            # index is raised to get the next letter of the key
            index += 1

            # When all the letters in the first column of the first row are added
            # The row is set back to 0 and letterToGet is added 1 to go to the next column
            if (index == rows):
                index = 0
                letterToGet += 1

        # Returns untransposed 2d matrix as a string
        return unTransposed_text

    def decrypt(self):
        """Runs an untranspose using the second given key. Then it runs another untranspose using the first key.
    Finally it returns the decrypted text. **May have some trash at the end due to having to fill the matrix**"""

        decrypted_text = self.unTranspose(self.unTranspose(self.text, self.key2), self.key1)

        return decrypted_text

    def removeRepeatedLetters(self, key):
        """Removes the repeated letters in the keys provided by the user"""
        return "".join(OrderedDict.fromkeys(key))


def test():
    """Test is used to test the modules ability to encrypt and decrypt text"""

    aText = "Be at the third pillar from the left outside the lyceum theatre tonight at seven. If you are distrustful bring two friends."
    print("Original text:")
    print(aText, "\n")

    sentence = DoubleTranspositionCipher(aText, "Networksecurity", "Cryptographic")
    encrypted_sentence = sentence.encrypt()

    aText = encrypted_sentence
    decrypt_this_text = DoubleTranspositionCipher(aText, "Networksecurity", "Cryptographic")

    print("Encrypted:")
    print(encrypted_sentence, "\n")

    print("Decrypted:")
    print(decrypt_this_text.decrypt())


if __name__ == "__main__":
    test()






