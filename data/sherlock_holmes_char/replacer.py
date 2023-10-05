def replace_characters(input_text):
    # Define the character mapping
    char_mapping = {
        '!': '!',
        '"': '"',
        '&': '&',
        "'": "'",
        '(': ' ',
        ')': ' ',
        '*': ' ',
        ',': ',',
        '-': '-',
        '.': '.',
        '/': ' ',
        '0': ' ',
        '1': ' ',
        '2': ' ',
        '3': '3',
        '4': ' ',
        '5': ' ',
        '6': ' ',
        '7': ' ',
        '8': ' ',
        '9': ' ',
        ':': ':',
        ';': ';',
        '?': '?',
        'A': 'A',
        'B': 'B',
        'C': 'C',
        'D': 'D',
        'E': 'E',
        'F': 'F',
        'G': 'G',
        'H': 'H',
        'I': 'I',
        'J': 'J',
        'K': 'K',
        'L': 'L',
        'M': 'M',
        'N': 'N',
        'O': 'O',
        'P': 'P',
        'Q': 'Q',
        'R': 'R',
        'S': 'S',
        'T': 'T',
        'U': 'U',
        'V': 'V',
        'W': 'W',
        'X': 'X',
        'Y': 'Y',
        'Z': 'Z',
        '[': ' ',
        ']': ' ',
        '`': '`',
        'a': 'a',
        'à': 'a',
        'â': 'a',
        'è': 'e',
        'é': 'e',
        'ê': 'e',
        'î': 'i',
        'ñ': 'n',
        'ô': 'o',
        'ö': 'o',
        'û': 'u',
        'ü': 'u',
        '’': "'",
        '`': "'",
        '£': '',
        '°': '',
        '½': '',
        'ß': '',
    }

    # Replace characters based on the mapping
    output_text = ''.join([char_mapping.get(char, char) for char in input_text])

    return output_text

# Test the function
# input_text = "Your input text goes here"
# output_text = replace_characters(input_text)
# print(output_text)

#  !$&',-.3:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
# !$&'()*,-.0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZ[]`abcdefghijklmnopqrstuvwxyz