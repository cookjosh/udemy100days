
def main():
    user_text = (input("Please enter the text you'd like to translate: ")).upper()

    morse_code_dict = { 'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..', '/':'-..-.', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-'}
    translated_text = ""
    for character in user_text:
        if character in morse_code_dict.keys():
            translated_text += (morse_code_dict[character] + " ")
        else:
            print("Not every character you entered is in our Morse dictionary!")
            print("Please try again!")

    print(f"Morse translation: {translated_text}")

if __name__ == "__main__":
    main()