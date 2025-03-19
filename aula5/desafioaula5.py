import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt', quiet=False)
nltk.data.path.append('/home/codespace/nltk_data')
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import string

print("\n")
texto = 'running better studies wolves mice children was ate swimming parties leaves knives happier studying played goes driving talked'

tokens = tokenizer.tokenize(texto)
print("Tokenizado", tokens)

print("\n")

def lemmatize_tokens(tokens):
    
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]

lemmatized_tokens = lemmatize_tokens(tokens)
print("Lematizado:", lemmatized_tokens)

print("\n, Frase lematizada: ")

def basic_cleaning(text):
    
    text = text.lower()
    
    
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    
    text = re.sub(r'\d+', '', text)
    
   
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

frase =  "The children were playing in the leaves yesterday."

cleaned_sentence = basic_cleaning(frase)
print("Após limpeza básica:", cleaned_sentence)

tokensTwo = tokenizer.tokenize(frase)
print("Frase Tokenizada", tokensTwo)

lemmatized_tokens = lemmatize_tokens(tokensTwo)
print("Lematizado:", lemmatized_tokens)

