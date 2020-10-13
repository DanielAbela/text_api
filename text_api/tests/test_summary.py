from unittest import TestCase
from unittest.mock import patch, Mock

from summary import Summary
from collections import defaultdict

class TestSummary(TestCase):

    def test_formatted_text(self):
        text = 'This is a test piece of text.'
        summary = Summary(text)
        expected_test = 'This is a test piece of text '
        actual_text = summary.formatted_text
        self.assertEqual(expected_test, actual_text)

    @patch('summary.nltk.corpus.stopwords.words')
    def test_filter_out_stopwords(self, mock_words):
        text = 'This Alpha is a Beta test piece Charlie of Delta Echo text.'
        summary = Summary(text)
        mock_words.return_value = ['Alpha', 'Beta', 'Charlie', 'Delta', 'Echo']
        expected_text = ['This', 'is', 'a', 'test', 'piece', 'of', 'text']
        actual_text = summary._filter_out_stopwords()
        self.assertEqual(expected_text, actual_text)

    def test_calculate_word_frequencies(self):
        text = 'Alpha Beta Beta Charlie Charlie Charlie Delta Delta Delta Delta'
        summary = Summary(text)
        expected_word_frequencies = dict(Alpha=1, Beta=2, Charlie=3, Delta=4)
        actual_word_frequencies = summary._calculate_word_frequencies()
        self.assertEqual(expected_word_frequencies, actual_word_frequencies)

    def test_calculate_weighted_word_frequencies(self):
        text = 'This can be blank.'
        summary = Summary(text)
        word_frequencies = dict(Alpha=1, Beta=2, Charlie=3, Delta=4)
        summary._calculate_word_frequencies = Mock(return_value=word_frequencies)
        expected_weighted_word_frequencies = dict(Alpha=0.25, Beta=0.5, Charlie=0.75, Delta=1)
        actual_weighted_word_frequencies = summary._calculate_weighted_word_frequencies()
        self.assertEqual(expected_weighted_word_frequencies, actual_weighted_word_frequencies)

    def test_calculate_sentence_scores(self):
        weighted_word_frequencies = dict(Alpha=0.25, Beta=0.5, Charlie=0.75, Delta=1)
        text = 'This is sentence 1 Alpha Alpha. This is sentence 2 Beta. This is sentence 3 Charlie Charlie.'
        summary = Summary(text)
        expected_sentence_scores=defaultdict(int, {
            'This is sentence 1 Alpha Alpha.': 0.5,
            'This is sentence 2 Beta.': 0.5,
            'This is sentence 3 Charlie Charlie.': 1.5
        })
        actual_sentence_scores = summary._calculate_sentence_scores(weighted_word_frequencies)
        self.assertEqual(expected_sentence_scores, actual_sentence_scores)

