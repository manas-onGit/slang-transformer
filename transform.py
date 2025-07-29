import json
import re

print("✅ Script Started")

# Load slang dictionary and normalize keys to lowercase
with open('slang_dictionary.json', 'r') as file:
    original_dict = json.load(file)
    slang_dict = {k.lower(): v for k, v in original_dict.items()}  # ✅ convert all keys to lowercase

def transform_slang(sentence):
    # Break input into words and symbols while preserving order
    words = re.findall(r'\w+|\W+', sentence)
    transformed_words = []

    for word in words:
        if word.strip() == "":
            transformed_words.append(word)
            continue

        if word.isalnum():  # check if it's a word, not punctuation
            lower_word = word.lower()
            if lower_word in slang_dict:
                formal_word = slang_dict[lower_word]
                # Retain original capitalization if needed
                if word.istitle():
                    formal_word = formal_word.capitalize()
                elif word.isupper():
                    formal_word = formal_word.upper()
                transformed_words.append(formal_word)
            else:
                transformed_words.append(word)
        else:
            transformed_words.append(word)

    return ''.join(transformed_words)

# Testing
if __name__ == "__main__":
    input_text = "ily bro, brb! af smh. ttyl wassup IDK IDC"
    output_text = transform_slang(input_text)
    print("Input: ", input_text)
    print("Output:", output_text)
