from base64 import *


class base64cipher:
    def __init__(self, text):
        self.text = text

    def encrypt(self):
        """Encrypt first converts the text supplied by the user into bytes, then encodes into base64 code using the base64
        python library, and finally decodes it from bytes into plaintext"""
        bytes_text = bytes(self.text, 'utf-8')
        self.encode = b64encode(bytes_text)
        coded_message = self.encode.decode('utf-8')
        return coded_message

    def decrypt(self):
        """Decrypt converts the base64 encryption supplied by the user using the base64 python library,
        and then decodes the byte data into plaintext"""
        self.decode = b64decode(self.text)
        message = self.decode.decode('utf-8')
        return message


def test():
    aText = "Be at the third pillar from the left outside the lyceum theatre tonight at seven. If you are distrustful bring two friends."
    print("Original text:")
    print(aText, "\n")

    sentence = base64cipher(aText)
    encrypted_sentence = sentence.encrypt()

    aText = encrypted_sentence
    decrypt_this_text = base64cipher(aText)

    print("Encrypted:")
    print(encrypted_sentence, "\n")

    print("Decrypted:")
    print(decrypt_this_text.decrypt())


if __name__ == "__main__":
    test()
