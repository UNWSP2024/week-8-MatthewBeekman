def convert_run_together(sentence):
    words = []
    current_word = ""
    for char in sentence:
        if char.isupper() and current_word:
            words.append(current_word)
            current_word = char
        else:
            current_word += char
    if current_word:
        words.append(current_word)
    result = ' '.join(words)
    return result.capitalize()
input_sentence = input("Write a sentence(don't include spaces and the first letter of each word is capital): ")
output_sentence = convert_run_together(input_sentence)
print(output_sentence)

# Matthew Beekman
# 10/24/2024
# Program 2