alphabet = {
    "A": '4',
    "B": 'I3',
    "C": '[',
    "D": ')',
    "E": '3',
    "F": '|=',
    "G": '&',
    "H": '#',
    "I": '1',
    "J": ',_|',
    "K": '>|',
    "L": '1',
    "M": '/\\/\\',
    "N": '^/',
    "O": '0',
    "P": '|*',
    "Q": '(_,)',
    "R": 'I2',
    "S": '5',
    "T": '7',
    "U": '(_)',
    "V": '\\/',
    "W": '\\/\\/',
    "X": '><',
    "Y": 'j',
    "Z": '2',
    "1": 'L',
    "2": 'R',
    "3": 'E',
    "4": 'A',
    "5": 'S',
    "6": 'b',
    "7": 'T',
    "8": 'B',
    "9": 'g',
    "0": 'o'
}


def format_txt(txt):
    caracteres = []  # Lista vacía para acumular caracteres

    for abc in txt.upper():
        # Agregar el carácter modificado o el original a la lista
        caracteres.append(alphabet.get(abc) if alphabet.get(abc) else abc)

    # Unir todos los caracteres en una sola cadena
    txt_format = ''.join(caracteres)
    print(txt_format)

# Prueba
format_txt("Hello word")

