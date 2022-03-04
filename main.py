import re


# TODO 1: Create morse alphabet:

morse_alphabet = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '  '
}  # From  a-z  &  0-9  & space

# TODO 2: Create a pattern for the regex function (a-z , 0-9 and spaces accepted):

pattern = "^[a-z0-9 ]*$"

# TODO 3: Create the while loop to reject inputs. If accepted, create morse code output:

wrong_input = True


while wrong_input:
    user_input_non_morse = []
    text_to_convert = input('Input text to convert to morse code: ')
    text_to_convert = text_to_convert.lower()
    for char in text_to_convert:
        user_input_non_morse.append(char)
    if text_to_convert == '':
        wrong_input = True
        print('Input something please \n')
    elif not bool(re.match(pattern, text_to_convert)):
        wrong_input = True
        print('Only a-z, 0-9 or spaces allowed \n')
    else:
        user_input_in_morse = []
        for character in user_input_non_morse:
            user_input_in_morse.append(morse_alphabet[character])
            morse_code_output = ''.join(user_input_in_morse)
        break


# TODO 4:Print morse code output:

print(f'Morse code: \n {morse_code_output}')
