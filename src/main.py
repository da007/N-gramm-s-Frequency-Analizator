import fa.utils
from fa.algorithms.bpe import get_list_optimized


with open("9000_nomi_propri.txt", "r", encoding="UTF-8") as file:
    text = file.readlines()
unique_words = fa.utils.get_unique_words(text, "ita")
N_grammes = fa.utils.get_N_grammes_from_words(unique_words)
result = get_list_optimized(unique_words, max = 30, depth = 30)
for e in result:
    print(e)