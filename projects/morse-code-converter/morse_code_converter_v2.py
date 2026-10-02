import tkinter as tk

FONT = ('Arial', 12)
CONVERSIONS = {
    'A' : '.-', 'B' : '-...',  'C' : '-.-.', 'D' : '-..',
    'E' : '.', 'F' : '..-.', 'G' : '--.', 'H' : '....',
    'I' : '..', 'J' : '.---', 'K' : '-.-', 'L' : '.-..',
    'M' : '--', 'N' : '-.', 'O' : '---', 'P' : '.--.',
    'Q' : '--.-', 'R' : '.-.', 'S' : '...', 'T' : '-',
    'U' : '..-', 'V' : '...-', 'W' : '.--', 'X' : '-..-',
    'Y' : '-.--', 'Z' : '--..',
    '0' : '-----', '1' : '.----', '2' : '..---', '3' : '...--',
    '4' : '....-', '5' : '.....', '6' : '-....', '7' : '--...',
    '8' : '---..', '9' : '----.',
    '.' : '.-.-.-', ',' : '--..--', '?' : '..--..', '\'' : '.----.',
    '!' : '-.-.--', '/' : '-..-.', '(' : '-.--.', ')' : '-.--.-',
    ':' : '---...', ';' : '-.-.-.',
    ' ' : '/'
}
reversed_conversions = {v: k for (k, v) in CONVERSIONS.items()}

# Text to Code Conversion
def text_to_code():
    text = input_text.get("1.0", "end-1c").upper().split()
    code = []
    try:
        for word in text:
            coded_char = []
            for char in word:
                coded_char.append(CONVERSIONS[char])
            code.append(' '.join(coded_char))
        output = "/".join(code)
    except KeyError:
        output = "Please only use letters (a-z,A-Z), numbers (0-9),\n"
        output = output + "these special characters (. , ? \' ! / ( ) : ;)\n"
        output = output + "spaces ( )"
    output_text.delete("1.0", "end")
    output_text.insert("end", output)

# Code to Text Conversion
def code_to_text():
    code = input_text.get("1.0", "end-1c").upper().split('/')
    text = []
    try:
        for word in code:
            coded_word = word.split()
            decoded_word = []
            for char in coded_word:
                decoded_word.append(reversed_conversions[char])
            text.append(''.join(decoded_word))
        output = ' '.join(text)
    except KeyError:
        output = "Please only use dashes (-), full stops(.),\n"
        output = output + "spaces( ) and forward slashes(/)"
    output_text.delete("1.0", "end")
    output_text.insert("end", output)

# Clear The Text Widgets
def clear():
    output_label.config(text="Converted Text/Morse Code:")
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")

# GUI
window = tk.Tk()
window.title("Morse Code Converter")
window.config(padx=25, pady=25)

instruction_label = tk.Label(text="Please use a single space to separate\n" +
                          "individual Morse Code Characters and\n" +
                          "a '/' to separate words", font=FONT, justify='center', pady=10)
instruction_label.grid(column=0, row=0, columnspan=2)

input_label = tk.Label(text='Please insert text or Morse Code:', font=FONT, pady=10)
input_label.grid(column=0, row=1, columnspan=2)

input_text = tk.Text(width=50, height=5, pady=10)
input_text.grid(column=0, row=2, columnspan=2)

text_to_code_button = tk.Button(text="Convert Text to Morse Code", command=text_to_code, font=FONT, pady=10)
text_to_code_button.grid(column=0, row=3)

code_to_text_button = tk.Button(text="Convert Morse Code to Text", command=code_to_text, font=FONT, pady=10)
code_to_text_button.grid(column=1, row=3)

output_label = tk.Label(text="Converted Text/Morse Code:", font=FONT, pady=10)
output_label.grid(column=0, row=4, columnspan=2)

output_text = tk.Text(width=50, height=5, pady=10)
output_text.grid(column=0, row=5, columnspan=2)

clear_button = tk.Button(text="Clear", command=clear, font=FONT, pady=10)
clear_button.grid(column=0, row=6)

window.mainloop()
