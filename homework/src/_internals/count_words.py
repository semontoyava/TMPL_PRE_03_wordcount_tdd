def count_words(words):
    counter = {}
    for w in words:
        counter[w] = counter.get(w, 0) + 1
    return counter
