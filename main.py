from morse_convertor import MorseConvertor

def Convertor():
    convertor = MorseConvertor()
    choice = int(input("Type 1 to convert to morse code or 0 to convert morse code to plain text: "))
    if choice == 1:
        user_message = input('Message to translate to morse code: ').upper()
        convertor.Convert(user_message)
    else:
        user_message = input('Message to translate to plain text: ').upper()
        convertor.Decode(user_message)

Convertor()
