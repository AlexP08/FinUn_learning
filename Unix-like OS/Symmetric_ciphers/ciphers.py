from dataclasses import dataclass, field
import string
import collections


@dataclass
class CAESAR:
    key: int
    input_message: str
    encrypted_message: str = field(init=False)
    decrypted_message: tuple = field(init=False)

    def __post_init__(self):
        self.encrypted_message = self.encrypt(self.key, self.input_message)
        self.decrypted_message = self.check_result(self.input_message, self.nonkey_decrypt())

    def encrypt(self, key, string):
        result = ''
        for char in string:
            if char.isalpha() is True:
                result += chr((ord(char) + key) % 65536)
            else:
                result += char
        return result

    def decrypt(self, k, msg):
        return self.encrypt((-1) * k, msg)

    def nonkey_decrypt(self):
        c = collections.Counter(filter(lambda simb: not simb.isspace(), self.encrypted_message))
        most_common = c.most_common()
        plaintext = {}
        for ch, _ in most_common:
            for i in string.ascii_lowercase + ''.join([chr(i) for i in range(ord('а'), ord('а') + 32)]):
                diff = ord(ch) - ord(i)
                plaintext[diff] = self.decrypt(diff, self.encrypted_message)
        return plaintext

    def check_result(self, dec_messgage, dec_nonkey_message):
        for key, msg in dec_nonkey_message.items():
            if dec_messgage == msg:
                return msg, key


@dataclass
class VIGENERE():
    key: str
    input_message: str
    encrypted_func: object = field(init=False)
    decrypted_func: object = field(init=False)
    d: list = field(init=False)
    prepval: object = field(init=False)

    def __post_init__(self):
        self.prepval = lambda val: zip(range(0, len(val)), val)
        self.d = [chr(i) for i in range(127)]
        self.encrypted_func = lambda ch, key: (ch + key) % len(self.d)
        self.decrypted_func = lambda ch, key: (ch - key + len(self.d)) % len(self.d)

    def vigenere(self, value, key, func):
        kl = len(key)
        value = self.prepval(value)
        e = [func(ord(c), ord(key[i % kl])) for (i, c) in value]
        return ''.join([self.d[c] for c in e])


if __name__ == "__main__":
    print('--=ШИФР ЦЕЗАРЯ=--')
    caesar = CAESAR(6, 'Если под вечностью понимать не бесконечную временную продолжительность, а безвременье, то живущий в настоящем живет вечно.')
    print('Зашифрованное сообщение:  ', caesar.encrypted_message)
    print('Расшифрованное сообение с переданным ключем:   ', caesar.decrypt(caesar.key, caesar.encrypted_message))
    print(f"Найденный ключ сообшения - {caesar.decrypted_message[1]}, Расшифрованное сообщение без ключа - {caesar.decrypted_message[0]}")
    print('--=ШИФР Вернама=--')
    vigenere = VIGENERE('key', 'I took my Power in my Hand and went against the World')
    massage = vigenere.vigenere(vigenere.input_message, vigenere.key, vigenere.encrypted_func)
    print('Зашифрованное сообщение - ', massage)
    print('Расшифрованное сообщение - ', vigenere.vigenere(massage, vigenere.key, vigenere.decrypted_func))
