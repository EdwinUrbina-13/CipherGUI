class MorseCodeCipher:
    # Global List with the alphabet, numbers 1-9, symbols, and some messages in english
    global alpha
    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "W", "X", "Y", "Z", "0", "1", "2",
             "3", "4", "5", "6", "7", "8", "9", ".", ",", "?", "-", "=", ":", ";", "(", ")", "/", '"', "$", "'", "\n",
             "_", "@", "!", "+", "~", "#", "&", "\\", " ",
             "[Error]", "[Wait]", "[Understood]", "[End of message]", "[End of work]", "[Starting signal]",
             "[Invitation to transmit]"]

    # All members of alpha list converted into morse code and in the same index
    global morse
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-",
             "..-", "...-", ".--", "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....",
             "-....", "--...", "---..", "----.",
             ".-.-.-", "--..--", "..--..", "-....-", "-...-", "---...", "-.-.-.", "-.--.", "-.--.-", "-..-.", ".-..-.",
             "...-..-", ".-.-..", "..--.-",
             ".--.-.", "---.", "-.-.--", ".-.-.", ".-...", "...-.-", ". ...", "-..-.", "/", "......", "...-...",
             "...-..", "..-.-..", "...-.-.", ".-.-.-.", "-.-.-.-"]

    def __init__(self, text):
        # Assigns the text given by user to self.text with letters in uppercase
        self.text = text.upper()

    def searchAlpha(self, val):
        """"The searchAlpha method returns the index where it finds the match of 'val' in alpha list."""

        # For loop that searches in the alpha list the match of the value given
        for i in range(len(alpha)):
            # If the if statement is true it returns the index where it found the match
            if val == alpha[i]:
                return i

    def searchMorse(self, val):
        """"The searchMorse method returns the index where it finds the match of 'val' in morse list."""

        # For loop that searches in the morse list the match of the value given
        for i in range(len(morse)):
            # If the if statement is TRUE it returns the index where it found the match
            if val == morse[i]:
                return i

    def putInList(self, text):
        """The putInList method takes a text writen and morse code and stores it in a list. First it reads a text written in morse code.
        It then adds each combination of dots and dashes (this formulate a morse code value) before each " " into the list.
        It later returns the list. This method is necessary to be able to use searchMorse and find matches"""

        # Creates a list to store the morse code values
        textInList = []
        # A string to hold a morse code value
        aNewLetter = ""

        # For loop to go through the text
        for i in range(len(self.text)):
            # If the letter in a text in the text is not a spaces it adds it to the aNewLetter string
            if (self.text[i] != " "):
                aNewLetter += self.text[i]
            # If the letter in the text is a space it means all the previous characters added
            # to aNewLetter forms a character in morse code
            else:
                # Adds the found morse character to the list
                textInList.append(aNewLetter)
                # Set aNewLetter back to an empty string to get the next morse character
                aNewLetter = ""

        # Returns
        return textInList

    def encrypt(self):
        """The encrypt method uses searchAlpha to find the index of the value being search for in the text in 'alpha list'.
        After this it takes that index and add the value inside 'morse list' with the same index"""
        # Sets encryptedText as an empty string
        encryptedText = ""

        # For loop that runs throug the text
        for i in range(len(self.text)):
            # It adds to encryptedText the corresponding morse code value found in the index given by 'alphaSearch' and adds a space
            encryptedText += morse[self.searchAlpha(self.text[i])] + " "

        # Returns the encrypted text
        return encryptedText

    def decrypt(self):
        """The decrypt method converts the given text into a list. After this, it uses searchMorse to find the index of the value
        being search for in the list created in 'morse list'. Finally, it takes that index and add the value inside 'alpha list' with the same index"""
        ##Sets decryptedText as an empty string
        decryptedText = ""
        # Converts the text into a list
        textInList = self.putInList(self.text)

        # For loop that runs throug the text
        for i in range(len(textInList)):
            # It adds to decryptedText the corresponding letter, number, symbol, or message found in the index given by 'morseSearch'
            decryptedText += alpha[self.searchMorse(textInList[i])]

        # Returns the decrypted text
        return decryptedText


def test():
    """Test is used to test the modules ability to encrypt and decrypt text"""
    aText = "Be at the third pillar from the left outside the lyceum theatre tonight at seven. If you are distrustful bring two friends."
    print("Original text:")
    print(aText, "\n")

    sentence = MorseCodeCipher(aText)
    encrypted_sentence = sentence.encrypt()

    aText = encrypted_sentence
    decrypt_this_text = MorseCodeCipher(aText)

    print("Encrypted:")
    print(encrypted_sentence, "\n")

    print("Decrypted:")
    print(decrypt_this_text.decrypt())


if __name__ == "__main__":
    test()

