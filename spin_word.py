def spin_words(sentence):
    sentence = sentence.split()
    final_sentence = []
    for i in sentence:
        if len(i) > 5:
            i = i[::-1]

        final_sentence.append(i)

    final_sentence = ' '.join(final_sentence)
    return final_sentence


phrase = "Olá Marilene hoje"
print(spin_words(phrase))
