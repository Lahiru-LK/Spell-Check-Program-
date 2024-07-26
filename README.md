# Spell Check Program 📝🔍

## Project Overview 🚀
This project implements a spell checker program inspired by Ben Dickens' Spell Check Programming . The spell checker corrects spelling errors in a given text file by referring to a dictionary of common misspellings.

![image](https://github.com/user-attachments/assets/bdca08bc-3bd1-4645-b5b4-36bc1c4f6e6b)


## Features ✨
- **Corrects spelling errors**: Automatically fixes misspelled words in the input text file.
- **Handles capitalization**: Maintains the original capitalization of words.
- **Ignores punctuation**: Handles punctuation marks such as `,`, `.`, `?`, and `!`.
- **Flexible dictionary**: Uses a dictionary file (`misspellings.txt`) to map incorrect words to their correct spellings.

## File Structure 📂
- `misspellings_1.txt`: Dictionary file for the first test case.
- `misspellings_2.txt`: Dictionary file for the second test case.
- `output_words_1.txt`: Output file for the first test case.
- `output_words_2.txt`: Output file for the second test case.
- `spellcheck.py`: Main program file.
- `words_1.txt`: Input file for the first test case.
- `words_2.txt`: Input file for the second test case.

## How to Use 📖
1. **Prepare the dictionary file**: Create a `misspellings.txt` file with the following format:
   ```
   incorrect_word->correct_word
   ```
   For example:
   ```
   hudnred->hundred
   fifeteen->fifteen
   ```

2. **Prepare the input file**: Create a text file with the content you want to spell-check.

3. **Run the program**:
   ```python
   if __name__ == '__main__':
       spell_dict = read_spellings('misspellings.txt')
       correct_spelling('words.txt', spell_dict)
   ```

4. **Check the output**: The corrected text will be saved in a file with the prefix `output_`, for example, `output_words.txt`.

## Example Usage 🌟

### Example 1 (No punctuation or capitalized words)
- `misspellings_1.txt`:
  ```
  datamic->dramatic
  elaphant->elephant
  ```

- `words_1.txt`:
  ```
  joe and his family went to the zoo the other day
  the zooo had many animals including an elofent
  ```

- Run the program:
  ```python
  if __name__ == '__main__':
      spell_dict = read_spellings('misspellings_1.txt')
      correct_spelling('words_1.txt', spell_dict)
  ```

- `output_words_1.txt`:
  ```
  joe and his family went to the zoo the other day
  the zoo had many animals including an elephant
  ```

### Example 2 (With punctuation and capitalized words)
- `misspellings_2.txt`:
  ```
  hereo->hero
  fluwe->flew
  jumpedd->jumped
  savved->saved
  ```

- `words_2.txt`:
  ```
  There once was a hero, named superman.
  Sumperan, being the hero he is, jumped.
  ```

- Run the program:
  ```python
  if __name__ == '__main__':
      spell_dict = read_spellings('misspellings_2.txt')
      correct_spelling('words_2.txt', spell_dict)
  ```

- `output_words_2.txt`:
  ```
  There once was a hero, named superman.
  Superman, being the hero he is, jumped.
  ```

## Code Overview 💻

### `read_spellings(filename)` 📘
This function reads the `misspellings.txt` file and returns a dictionary with misspelled words as keys and their correct spellings as values.

### `correct_spelling(input_filename, spell_dict)` ✏️
This function reads the input file, corrects the misspelled words using the dictionary, and writes the corrected text to an output file with the prefix `output_`.

## Contributing 🤝
Feel free to fork this repository and make contributions. Pull requests are welcome!

## License 📜
This project is licensed under the MIT License.

## Acknowledgments 🙏
- Thanks to Ben Dickens for the inspiration for this assignment.

---
