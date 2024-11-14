# Cryptography Program

**Author:** Zach Khan  
**Date:** March 10, 2023  

This program implements a simple substitution cipher, allowing the user to encode and decode messages based on a custom alphabetic key. The cipher replaces each letter in the plaintext with a corresponding letter from a shuffled alphabet key.

## Program Overview

The cryptography program provides a basic interface for:
- Encoding plaintext into a coded message.
- Decoding a coded message back into plaintext.

It utilizes a substitution cipher based on a custom alphabet key to perform the transformations.

## Features

- **Encode Text**: Converts a user-input message into a coded message using the cipher key.
- **Decode Text**: Converts a coded message back into the original text using the cipher key.
- **Interactive Menu**: Offers a simple menu for selecting encode, decode, or exit options.

## How It Works

- **Substitution Cipher**: Each letter in the plaintext is mapped to a corresponding letter in the cipher key (`alpha` to `key`).
- **Alphabet and Key**: 
  - `alpha`: The standard alphabet (`"ABCDEFGHIJKLMNOPQRSTUVWXYZ"`).
  - `key`: A shuffled version of the alphabet, representing the cipher (`"XPMGTDHLYONZBWEARKJUFSCIQV"`).

### Main Functions

- **`menu()`**: Displays the interactive menu and returns the user’s choice.
- **`encode(plain)`**: Encodes a plaintext message by substituting each letter with the corresponding letter in `key`.
- **`decode(coded)`**: Decodes a coded message by reversing the substitution, converting `key` letters back to `alpha`.

## Usage

To run the program, execute:

```bash
python cryptography.py
```

Upon running, the program will display a menu with the following options:

- Encode a message.
- Decode a message.
- Quit the program.

## Example Intercation
```bash
SECRET DECODER MENU

0) Quit
1) Encode
2) Decode

What is your choice? 1
text to be encoded: Hello World
Encoded text: YBYYS CYVWB

What is your choice? 2
code to be decyphered: YBYYS CYVWB
Decoded text: HELLO WORLD
```

## Future Improvements

- Add support for custom keys entered by the user.
- Implement additional cipher types. 
- Add error handling for non-alphabet characters.
