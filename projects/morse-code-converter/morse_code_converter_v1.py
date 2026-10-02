from tkinter import *

CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              '.', ',', '?', "'", '!', '/', '(', ')', ':', ';']

MORSE_CODE = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
              '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-',
              '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--',
              '....-', '.....', '-....', '--...', '---..', '----.', '.-.-.-', '--..--',
              '..--..', '.----.', '-.-.--', '-..-.', '-.--.', '-.--.-', '---...', '-.-.-.']


# Convert Morse Code to Characters
def convert_to_char():
    code = input_text_entry.get()
    if len(code)>0:
        if code[len(code)-1]!=' ':
            code = code + ' '
    broken_code = []
    while code.find(' ')>0:
        if code.find('\t')==0:
            broken_code.append(' ')
            code = code[1:]
        else:
            broken_code.append(code[0: code.find(' ')+1])
            code = code[code.find(' ')+1:]
    solution = ''
    for i in range(len(broken_code)):
        if broken_code[i]==' ':
            solution = solution + ' '
        else:
            solution = solution + CHARACTERS[MORSE_CODE.index(broken_code[i][0:len(broken_code[i])-1])]
    output_text_label.config(text="Your converted phrase goes here:")
    output_text_entry.delete(0, END)
    output_text_entry.insert(0, solution)

# Convert Characters to Morse Code
def convert_to_code():
    phrase = input_text_entry.get()
    broken_characters = []
    # phrase.upper()
    for i in range(len(phrase)):
        if phrase[i]==' ':
            broken_characters.append('\t')
        else:
            broken_characters.append(phrase[i].upper())
    solution = ''
    for i in range(len(broken_characters)):
        if broken_characters[i]=='\t':
            solution = solution + '\t'
        else:
            solution = solution + MORSE_CODE[CHARACTERS.index(broken_characters[i])] + ' '
    output_text_label.config(text="Your converted code goes here:")
    output_text_entry.delete(0, END)
    output_text_entry.insert(0, solution)

# GUI
window = Tk()
window.title("Morse Code Translator")
window.config(width=400, height=400)

# Input Components
input_text_label = Label(text="Please enter the code/phrase you would like to convert:", font=("Courier", 15))
input_text_label.grid(column=0, row=0, columnspan=2)

input_text_entry = Entry(width=50, font=("Courier", 25))
input_text_entry.grid(column=0, row=1, columnspan=2)

# Process Components
convert_to_char_button = Button(text="Convert to characters", command=convert_to_char, highlightthickness=0)
convert_to_char_button.grid(column=0, row=2)

convert_to_code_button = Button(text="Convert to code", command=convert_to_code, highlightthickness=0)
convert_to_code_button.grid(column=1, row=2)

# Output Components
output_text_label = Label(text="Your converted code/phrase goes here:", font=("Courier", 15))
output_text_label.grid(column=0, row=3, columnspan=2)

output_text_entry = Entry(width=50, font=("Courier", 25))
output_text_entry.grid(column=0, row=4, columnspan=2)

window.mainloop()
