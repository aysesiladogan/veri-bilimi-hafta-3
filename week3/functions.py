def word_counter(text):
    words = text.split()
    sum = len(words)
    longest = max(words, key=len)
    often = max(set(words), key=words.count)
    return sum, longest, often

text = "veri bilim veri techcareer yapay zekâ python"
print(word_counter(text))

