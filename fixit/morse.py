MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}


REVERSE_MORSE = {}
for key, value in MORSE.items():
    REVERSE_MORSE[value] = key


def encode(text):
    result = []
    
    for i in text.upper():
        if i in MORSE:
            result.append(MORSE[i])
        else:
            raise ValueError("Unsupported character")
            
    return " ".join(result)


def decode(text):
    result = []
    
    words= text.strip().split(" / ")
    
    for j in words:
        decoded = []
        letters = j.split(" ")
        
        for i in letters:
            if i in REVERSE_MORSE:
                decoded.append(REVERSE_MORSE[i])
            elif i != "":
                raise ValueError("Unsupported character")
                
        result.append("".join(decoded))
        
    return " ".join(result)
