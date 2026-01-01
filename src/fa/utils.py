from collections import Counter

MIN_N = 2
MAX_N = 4

def get_unique_by_chars(text, alphabet, replace):
    """
    Возвращает множество уникальных слов по символам, состоящие из алфавита, с заменной некоторых символов(например ударения)
    
    Args:
        text: Генератор строк для перебора
        alphabet: Алфавит
        replace: Словарь замены символов на другие
        
    Returns:
        Возвращает множество уникальных слов
    """
    if not text:
        return None
    
    unique_words = set()
    
    for line in text:
        word = ""
        for char in line:
            char = char.lower()
            char = replace.get(char, char)
            # empty chars - pass
            if not char:
                continue
            if char in alphabet:
                word += char
            elif not word:
                unique_words.add(word)
                word = ""
        if word:
            unique_words.add(word)
            word = ""
    
    return list(unique_words)

def get_N_grammes_from_word(word):
    N_grammes = []
    if len(word) >= MIN_N:
        for n in range(MIN_N, MAX_N + 1):
            N_grammes += [word[i:i+n] for i in range(len(word)- n + 1)]
    return Counter(N_grammes)

def get_N_grammes_from_words(unique_words):
    total_N_grammes = Counter()
    for word in unique_words:
        total_N_grammes.update(get_N_grammes_from_word(word))
    return total_N_grammes

def get_unique_words(text, lang):
    import fa.langs as langs 
    alphabet = langs.alphabetes.get(lang, langs.alphabetes["general"])
    replace = langs.replaces.get(lang, langs.replaces["general"])
    return get_unique_by_chars(text, alphabet, replace)

def get_N_grammes_from_text(text, lang):
    unique_words = get_unique_words(text, lang)
    return get_N_grammes_from_words(unique_words)