
def spin_words(sentence):
    return ' '.join(word[::-1] if len(word)>4 else word for word in [w for w in sentence.split()])

sen = "Hey fellow warriors"

print(spin_words(sen))