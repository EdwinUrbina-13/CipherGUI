class MorseCodeCipher:

    global alpha
    alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2",
                      "3","4","5","6","7","8","9",".",",","?","-","=",":",";","(",")","/",'"',"$","'","\n","_","@","!","+","~","#","&","\\"," ",
                      "[Error]","[Wait]","[Understood]","[End of message]","[End of work]","[Starting signal]", "[Invitation to transmit]"]
    
    global morse
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                     "..-","...-",".--","-..-","-.--","--..","-----",".----","..---","...--","....-",".....","-....","--...","---..","----.",
                     ".-.-.-","--..--","..--..","-....-","-...-","---...","-.-.-.","-.--.","-.--.-","-..-.",".-..-.","...-..-",".-.-..","..--.-",
                     ".--.-.","---.","-.-.--",".-.-.",".-...","...-.-",". ...","-..-.","/","......","...-...","...-..","..-.-..","...-.-.",".-.-.-.","-.-.-.-"]

    def __init__(self, text):
        self.text = text.upper()

    def searchAlpha(self, val):
        for i in range(len(alpha)):
            if val == alpha[i]:
                return i

    def searchMorse(self, val):
        for i in range(len(morse)):
            if val == morse[i]:
                return i
            
    def putInList(self, text):
        textInList = []
        aNewLetter = ""
        for i in range(len(self.text)):
            if(self.text[i] != " "):
                aNewLetter += self.text[i]
            else:
                textInList.append(aNewLetter)
                aNewLetter = ""
    
        return textInList        
        
    def encrypt(self):
        encryptedText = ""
        
        for i in range(len(self.text)):
            encryptedText += morse[self.searchAlpha(self.text[i])] + " "

        return encryptedText


    def decrypt(self):
        decryptedText = ""
        textInList = self.putInList(self.text)
        for i in range(len(textInList)):
            decryptedText += alpha[self.searchMorse(textInList[i])]

        return decryptedText

def test():
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
        
