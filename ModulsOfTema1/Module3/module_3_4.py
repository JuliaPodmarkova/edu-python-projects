def  single_root_words(root_words, *other_words):
    same_words = []
    root_wordsLower = root_words.lower()
    for word in other_words:
        wordLower = word.lower()
        if root_wordsLower in wordLower or wordLower in root_wordsLower:
            same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
