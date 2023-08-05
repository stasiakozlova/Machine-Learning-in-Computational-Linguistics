import pandas as pd
from nltk.tokenize import TweetTokenizer
from nltk import ngrams
import string
from collections import Counter


def preprocess(data: pd.Series):
    tweet_tokenizer = TweetTokenizer()
    convert_to_lowercase = lambda item: item.lower()
    lower = data.apply(convert_to_lowercase)
    tokenized = lower.apply(tweet_tokenizer.tokenize)
    filter_punctuation_numbers = lambda word: not set(word).issubset(set(string.punctuation)) and not word.isnumeric()
    filtered = tokenized.apply(lambda words: list(filter(filter_punctuation_numbers, words)))
    return filtered


def get_most_common_ngrams(data: pd.Series):
    n2_grams = data.apply(lambda words: list(ngrams(words, 2)))
    flatten = n2_grams.values.flatten()
    flatten = [item for sublist in flatten for item in sublist]
    return Counter(flatten).most_common()


def get_most_common_words(data: pd.Series):
    flatten = data.values.flatten()
    flatten = [item for sublist in flatten for item in sublist]
    return Counter(flatten).most_common()


def get_df():
    df = pd.read_csv("spam.csv", encoding="ISO-8859-1")

    # объединяем колонки с текстом, и переименовываем названия колонок
    df['text'] = df.iloc[:, 1:].astype(str).sum(1)
    df = df.iloc[:, [0, -1]]
    df.columns = ["category", "text"]

    df['category'] = df['category'].apply(lambda category: 1 if category == 'spam' else 0)

    return df
