def topk_words(words,k):
    final, dico, sorted_inverted_dico, bonbon = [], {}, {}, []
    for word in words:
        dico[word] = dico.get(word,0) + 1
    for word in dico:
        if dico[word] not in sorted_inverted_dico:
            sorted_inverted_dico[dico[word]] = [word]
        else:
            sorted_inverted_dico[dico[word]].append(word)
    highest = 0
    for key in sorted_inverted_dico:
        if key >= highest:
            highest = key
    for index in range(highest,0,-1):
        if index in sorted_inverted_dico:
            final.append((index,sorted_inverted_dico[index]))
    for thing in final[0:k]:
        bonbon.append(thing)
    return bonbon