import heapq
import re
from builtins import property
from collections import defaultdict

import nltk
from flask import Flask

app = Flask(__name__)


class Summary:
    MAXIMUM_SENTENCE_LENGTH = 30

    def __init__(self, text):
        self.text = text

    @property
    def formatted_text(self):
        formatted_article_text = re.sub("[^a-zA-Z]", " ", self.text)
        return re.sub(r"\s+", " ", formatted_article_text)

    def _filter_out_stopwords(self):
        return [
            word
            for word in self.formatted_text.split(" ")
            if word not in nltk.corpus.stopwords.words("english")
        ]

    def _calculate_word_frequencies(self):
        app.logger.info("Calculating word frequencies for text: %s", self.text)
        word_frequencies = defaultdict(int)
        for word in self._filter_out_stopwords():
            word_frequencies[word] += 1
        return word_frequencies

    def _calculate_weighted_word_frequencies(self):
        app.logger.info("Calculating weighted word frequencies for text: %s", self.text)
        word_frequencies = self._calculate_word_frequencies()
        weighted_word_frequencies = dict()
        maximum_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            weighted_word_frequencies[word] = word_frequencies[word] / maximum_frequency
        return weighted_word_frequencies

    def _calculate_sentence_scores(
        self, weighted_word_frequencies, max_sentence_length=MAXIMUM_SENTENCE_LENGTH
    ):
        app.logger.info("Calculating sentence scores for text: %s", self.text)
        sentence_scores = defaultdict(int)
        sentences = nltk.sent_tokenize(self.text)
        for sentence in sentences:
            for word in nltk.word_tokenize(sentence.lower()):
                if (
                    word in weighted_word_frequencies.keys()
                    and len(sentence.split(" ")) < max_sentence_length
                ):
                    sentence_scores[sentence] += weighted_word_frequencies[word]
        return sentence_scores

    def create(self):
        weighted_word_frequencies = self._calculate_weighted_word_frequencies()
        sentence_scores = self._calculate_sentence_scores(weighted_word_frequencies)
        return "".join(heapq.nlargest(7, sentence_scores, key=sentence_scores.get))
