def read_spellings(filename):
    misspellings = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                incorrect, correct = line.strip().split('->')
                misspellings[incorrect] = correct
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        exit(1)
    return misspellings


#correct_spelling---

def correct_spelling(input_filename, spell_dict):
    output_filename = 'output_' + input_filename
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                corrected_line = []
                words = line.split()
                for word in words:
                    punctuation = ''
                    if word[-1] in ',.?!':
                        punctuation = word[-1]
                        word = word[:-1]
                    lower_word = word.lower()
                    if lower_word in spell_dict:
                        corrected_word = spell_dict[lower_word]
                        if word[0].isupper():
                            corrected_word = corrected_word.capitalize()
                        corrected_word += punctuation
                    else:
                        corrected_word = word + punctuation
                    corrected_line.append(corrected_word)
                outfile.write(' '.join(corrected_line) + '\n')
    except FileNotFoundError:
        print(f"Error: '{input_filename}' not found.")
        exit(1)

# main------------------------------------------------------------

if __name__ == '__main__':
    spell_dict_1 = read_spellings('misspellings_1.txt')
    correct_spelling('words_1.txt', spell_dict_1)

    spell_dict_2 = read_spellings('misspellings_2.txt')
    correct_spelling('words_2.txt', spell_dict_2)


# Output --------------------------------------------------























