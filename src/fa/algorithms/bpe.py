import fa.utils as u
from collections import Counter

def get_stats(vocab):
    """Считает частоту пар символов, стоящих рядом."""
    pairs = Counter()
    for word in vocab:
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[symbols[i], symbols[i+1]] += 1
    return pairs

def merge_vocab(pair, v_in):
    """Объединяет самую частую пару во всем словаре."""
    v_out = []
    old_tokens = " ".join(pair)
    new_token = "".join(pair)
    for word in v_in:
        word = word.replace(old_tokens, new_token)
        v_out.append(word)
    return v_out

def get_list_optimized(unique_words, max=30, depth = 50):
    i = 1
    vocab = [" ".join(list(word)) for word in unique_words]
    pairs = None
    while i < depth:
        pairs = get_stats(vocab)
        best = pairs.most_common(1)[0][0]
        vocab = merge_vocab(best, vocab)
        i += 1
    return ["".join(pair) for pair, freq in pairs.most_common(max)]