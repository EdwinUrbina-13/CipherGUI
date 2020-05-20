class VigenereCipher:
    global alpha
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, text, key):
        self.text = text.upper()
        self.key = key

    def edKey(self, key):
        self.key = key.upper()
        return self.key

    def text_length(self):
        self.t_length = len(self.text)
        return self.t_length

    def expand_key(self, key):
        # This function cycles the key and appends itself until its length is equal or longer than the encrypted text
        self.expanded_key = self.key
        self.key_length = len(self.expanded_key)

        if self.text_length() == self.key_length:
            return (self.expanded_key)
        else:
            for i in range(self.text_length() - self.key_length):
                self.expanded_key = self.expanded_key + self.key
            return (self.expanded_key)

    def encrypt(self):
        key_pos = 0
        enc_text = ""
        K = self.edKey(self.key)
        expanded_key = self.expand_key(K)

        for i in self.text:
            if i in alpha:
                # Finds the numerical position of the letter in the alphabet
                position = alpha.find(i)
                # moves along key and finds the value of the character
                key_char = expanded_key[key_pos]
                key_character_position = alpha.find(key_char)
                key_pos = key_pos + 1
                new_position = position + key_character_position
                if new_position >= 26:
                    new_position = new_position - 26
                new_character = alpha[new_position]
                # Stores encrypted message letter by letter
                enc_text = enc_text + new_character
            else:
                enc_text = enc_text + i
        return enc_text

    def decrypt(self):
        key_pos = 0
        enc_text = ""
        K = self.edKey(self.key)
        expanded_key = self.expand_key(K)

        for i in self.text:
            if i in alpha:
                # Finds the numerical position of the letter in the alphabet
                position = alpha.find(i)
                # moves along key and finds the value of the character
                key_char = expanded_key[key_pos]
                key_character_position = alpha.find(key_char)
                key_pos = key_pos + 1
                new_position = position - key_character_position
                if new_position >= 26:
                    new_position = new_position + 26
                new_character = alpha[new_position]
                # Stores encrypted message letter by letter
                enc_text = enc_text + new_character
            else:
                enc_text = enc_text + i
        return enc_text


def test():
    """Test is used to test the modules ability to encrypt and decrypt text"""

    aText = "Be at the third pillar from the left outside the lyceum theatre tonight at seven. If you are distrustful bring two friends."
    print("Original text:")
    print(aText, "\n")

    sentence = VigenereCipher(aText, "networksecishard")
    encrypted_sentence = sentence.encrypt()

    aText = encrypted_sentence
    decrypt_this_text = VigenereCipher(aText, "networksecishard")

    print("Encrypted:")
    print(encrypted_sentence, "\n")

    print("Decrypted:")
    print(decrypt_this_text.decrypt())


if __name__ == "__main__":
    test()

