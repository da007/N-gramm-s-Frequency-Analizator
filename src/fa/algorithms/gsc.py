import fa.utils as u

def subtract_from(words, subtrahend):
    new_words = []
    for word in words:
        new_word = word.replace(subtrahend, "")
        if new_word:
            new_words.append(new_word)
    return new_words

def get_list_optimized(unique_words, max=30):
    new_words = unique_words.copy()
    result = []
    i = 1
    while len(result) < max and new_words:
        stats = u.get_N_grammes_from_words(new_words).most_common()
        best = None
        max_score = -1
        
        for gram, freq in stats:
            score = freq * len(gram)
            if score > max_score:
                max_score = score
                best = gram
                
        result.append(best)
        new_words = subtract_from(new_words, best)
    return result