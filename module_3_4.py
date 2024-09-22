def single_root_words(root_word, *other_words):
    same_words = []
    words = list(other_words)

    for i in range(len(words)):
        if root_word.lower() in words[i].lower() or words[i].lower() in root_word.lower():
            same_words.append(words[i])
    return (same_words)

result1 = single_root_words('brave', 'bravery', 'bravely')
result2 = single_root_words('advantage', 'disadvantage', 'advantageous')
print(result1)
print(result2)
