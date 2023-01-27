def calculate_word_frequencies(text):

    words = text.split()
    word_frequencies = {}
    for word in words:   #Iterate through the string, placing the words into a dict. The first time a word is seen, the frequency is 1. Each time the word is seen again, increment the frequency.
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1 # if the word is already in the dictionary, increment its frequency
    return word_frequencies

text = " Count each unique occurrence of a word and calculate frequency of occurrence and store in a dictionary."
frequencies = calculate_word_frequencies(text)
print(frequencies)
