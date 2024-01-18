import nltk as nl

test_string = ("Among Us is free to play on iOS and Android devices "
               "(you can download it on the App Store or Google Play Store). "
               "Or, it costs $5 to play on a PC (you can download it on Steam or itch.io).")

words = nl.word_tokenize(test_string)
print(nl.pos_tag(words))

stop_words = set(nl.corpus.stopwords.words('english'))
