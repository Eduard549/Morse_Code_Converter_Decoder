MORSE_CODE_STR = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..',
                  '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
                  '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----',
                  '.-.-.-', '..--..', '-...-', '-..-.', '-.-.--', '---...', '/', '--..--', '-....-', '.-..-.',
                  '.----.', '-.--.', '-.--.-', '.-.-.', '.--.-.']
LTR_NMR_PCT_STR = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                   '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                   '.', '?', '=', '/', '!', ':', ' ', ',', '-', '"', "'", '(', ')', '+', '@']


class MorseConvertor:
    def __init__(self):
        self.morse_dict = dict(zip(LTR_NMR_PCT_STR, MORSE_CODE_STR))
        self.str_dict = dict(zip(MORSE_CODE_STR, LTR_NMR_PCT_STR))

    def Convert(self, user_message):
        morse_coded_message = ''
        for x in user_message:
            try:
                morse_coded_message += (self.morse_dict[x] + ' ')
            except:
                pass
        print(f'Your message as morse code: {morse_coded_message}')
        return morse_coded_message

    def Decode(self, user_message):
        plain_text = ''
        message = user_message.split(" ")
        for x in message:
            if x in self.str_dict:
                try:
                    plain_text += self.str_dict[x]
                except:
                    pass
        print(plain_text)
        return plain_text



