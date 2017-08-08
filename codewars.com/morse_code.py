# https://www.codewars.com/kata/54b724efac3d5402db00065e

MORSE_CODE = {'.-...': '&', '--..--': ',', '....-': '4', '.....': '5', '...---...': 'SOS', '-...': 'B', '-..-': 'X',
              '.-.': 'R',
              '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F', '.': 'E', '.-..': 'L', '...': 'S',
              '..-': 'U',
              '..--..': '?', '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=', '---': 'O', '.--.': 'P',
              '.-.-.-': '.', '--': 'M', '-.': 'N', '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
              '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G', '--.-': 'Q', '--..': 'Z',
              '-..-.': '/',
              '.-.-.': '+', '-.-.': 'C', '---...': ':', '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$',
              '.---': 'J',
              '-----': '0', '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3'}


# def decodeMorse(morseCode):
#     words = morseCode.split("   ")
#     plain = ""
#     for w in words:
#         chars = w.split(" ")
#         new_word = ""
#         for c in chars:
#             if c in MORSE_CODE:
#                 new_word += MORSE_CODE[c]
#         plain += new_word + " "
#
#     return plain[:-1]
#
#
# def decodeMorse2(morseCode):
#     return ' '.join([''.join(map(lambda i: MORSE_CODE[i], x.split())) for x in [w for w in morseCode.strip().split('  ')]])


def decodeMorse(morseCode):
    return ' '.join(
        ''.join(map(lambda i: MORSE_CODE[i], word.split())) for word in [w for w in morseCode.strip().split('   ')])


print(decodeMorse('.'))
