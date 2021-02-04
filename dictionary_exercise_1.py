# Open txt file into string
text_file = open("text.txt", "r")
text_string = text_file.read()

# Make list of all the words
words_in_text = text_string.split()

# Make a list of distinct words
set_of_words = set(words_in_text)
unique_words_in_text = list(set_of_words)

# Make dictionary
word_frequency_dict = {}

# Add words to dictionary from distinct words list as keys, with their frequencies as values
for x in unique_words_in_text:
    frequency = words_in_text.count(x)
    word_frequency_dict[x] = frequency

print(word_frequency_dict)