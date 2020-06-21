
import nltk
from nltk.util import ngrams
 
# Function to generate n-grams from sentences.
def extract_ngramss(data, num):
    n_grams = ngrams(nltk.word_tokenize(data), num)
    return [ ' '.join(grams) for grams in n_grams]

def extract_ngrams(content, num):
    sentence = content.split()
    return [' '.join(sentence[i:i+num]) for i in range(len(sentence)-num+1)]
 
data = 'Botminds is for advanced document understanding using AI'
 
print("1-gram: ", extract_ngrams(data, 1))
print("2-gram: ", extract_ngrams(data, 2))
print("3-gram: ", extract_ngrams(data, 3))
print("4-gram: ", extract_ngrams(data, 4))