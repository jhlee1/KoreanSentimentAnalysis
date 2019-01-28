from __future__ import division

import re
from Crawlers import EdgeCrawler
import matplotlib.pyplot as pyplot
import pandas as pd
from konlpy.tag import Kkma


def preprocessor(text):
    text = text.rstrip().lstrip()
    return re.sub('[/[\{\}\[\]\/?|\)*~`!\-_+<>@\#$%&\\\=\(\'\"]+', '', text)  # remove special chars

def scores_to_percentiles(scores):
    sum_of_scores = sum(scores.values())

    for category in scores:
        scores[category] = scores[category] / sum_of_scores

    return scores


def analyze_sentences_into_chunks(sentences):
    kkma = Kkma()
    analyzed_words = []

    for s in sentences:
        s = preprocessor(s)
        analyzed_in_dicts = kkma.pos(s)
        tmp = []

        for word in analyzed_in_dicts:
            tmp.append("/".join(word))
        analyzed_words.append(";".join(tmp))

    return analyzed_words


def categorize_word_chunks(chunks, lexicons):
    scores = {'POS': 0, 'NEG': 0, 'NEUT': 0, 'COMP': 0, 'None': 0}
    for chunk in chunks:
        for index, row in lexicons.iterrows():
            if row['ngram'] in chunk:
                scores[row['max.value']] += row['max.prop']

    return scores_to_percentiles(scores)


# Get data and Read files
raw_data = EdgeCrawler.crawl_nexon_board()
# raw_data = open('resources/example.txt', encoding='utf-8')

sentiment_data_frame = pd.read_csv('lexicon/polarity.csv')
# Split sentences to chunks
word_chunks = analyze_sentences_into_chunks(raw_data)
# Analyze sentiments from chunks and polarity data frame
categorized_scores = categorize_word_chunks(word_chunks, sentiment_data_frame)

# Draw pie chart
pyplot.pie(categorized_scores.values(), explode=(0.02, 0.02, 0.02, 0.02, 0.02), labels=['Positive', 'Negative', 'Neutral', 'Composite', 'None'], autopct='%.2f', startangle=90)
pyplot.axis('equal')
pyplot.show()
