# Morse Code Converter

A desktop GUI application built with Python and Tkinter that converts text to Morse code and Morse code back to readable text.

This project was developed as a learning project while building Python programming skills. It contains two versions of the implementation, showing the progression from a list-based approach to a dictionary-based design with improved input handling and GUI structure.

---

## Features

* Convert text to Morse code
* Convert Morse code back to text
* Graphical user interface built with Tkinter
* Supports:

  * Letters A–Z
  * Numbers 0–9
  * Common punctuation
* Uses `/` to separate words in Morse code
* Input validation with user-facing error messages
* Clear button for resetting the input and output fields

---

## Implementation

### Version 1

The original implementation uses two parallel lists:

* One list containing supported characters
* One list containing their corresponding Morse codes

Conversion is performed by finding the position of a character or Morse code in one list and using the same position in the other list.

This version was useful for learning basic data structures, iteration, string processing, and GUI event handling.

### Version 2 — Current

Version 2 refactors the conversion logic around dictionaries.

It introduces:

* A dictionary for character-to-Morse conversion
* A reversed dictionary for Morse-to-character conversion
* Improved text input using Tkinter `Text` widgets
* Separate conversion functions for each direction
* Input validation with user-facing error messages
* A clear function for resetting the interface
* A more structured Tkinter implementation using `tkinter as tk`

The second version is the current implementation.

---

## How Conversion Works

### Text → Morse Code

1. The input text is converted to uppercase.
2. The text is split into words.
3. Each character is looked up in the conversion dictionary.
4. Characters within a word are separated by spaces.
5. Words are separated using `/`.

For example:

```text
HELLO WORLD
```

becomes:

```text
.... . .-.. .-.. ---/.-- --- .-. .-.. -..
```

### Morse Code → Text

1. The input is split into words using `/`.
2. Each word is split into individual Morse characters.
3. Each Morse sequence is looked up in the reverse conversion dictionary.
4. The decoded characters are combined into words.

---

## Technologies Used

* **Python 3**
* **Tkinter**

No external Python packages are required.

> On some Linux distributions, Tkinter may need to be installed separately through the operating system's package manager.

---

## Running the Project

From this directory, run the current version with:

```bash
python3 morse_code_converter_v2.py
```

The original implementation is preserved as:

```bash
python3 morse_code_converter_v1.py
```

Version 1 is retained for comparison and development history; Version 2 is the current implementation.

---

## Project Structure

```text
morse-code-converter/
├── morse_code_converter_v1.py
├── morse_code_converter_v2.py
└── README.md
```

---

## Input Rules

For Morse code input:

* Individual Morse characters must be separated by spaces.
* Words must be separated using `/`.
* Morse characters use `.` and `-`.
* Unsupported characters produce an input error message.

For text input:

* Letters and numbers are supported.
* Supported punctuation includes `. , ? ' ! / ( ) : ;`.
* Text is converted to uppercase before encoding.
* Multiple spaces are normalized when converting text to Morse code.

---

## What I Learned

This project provided practical experience with:

* Python functions and control flow
* Lists and dictionaries
* Dictionary lookups and reverse mappings
* String parsing and transformation
* Tkinter GUI development
* Event-driven programming
* User input validation
* Refactoring an existing implementation
* Improving code readability and maintainability

The transition from Version 1 to Version 2 was particularly useful for understanding how choosing an appropriate data structure can simplify program logic.

---

## Possible Future Improvements

* Copy-to-clipboard functionality
* Improved visual feedback for invalid input
* Dark mode
* Morse code audio playback
* Additional Morse code standards or symbols
* A web-based version

---

## Author

**Griffin Hamilton**

A Python learning project developed as part of my Computer Science portfolio.
