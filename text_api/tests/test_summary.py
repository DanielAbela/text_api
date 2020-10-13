from unittest import TestCase
from unittest.mock import patch

from summary import Summary


class TestSummary(TestCase):

    def test_formatted_text(self):
        text = 'This is a test piece of text.'
        summary = Summary(text)
        expected_test = 'This is a test piece of text.'
        actual_text = summary.formatted_text
        self.assertEqual(expected_test, actual_text)

    @patch('summary.nltk.corpus.stopwords.words')
    def test_filter_out_stopwords(self, mock_words):
        text = 'This Alpha is a Beta test piece Charlie of Delta Echo text.'
        summary = Summary(text)
        mock_words.return_value = ['Alpha', 'Beta', 'Charlie', 'Delta', 'Echo']
        expected_text = 'This is a test piece of text.'
        actual_text = summary._filter_out_stopwords()
        self.assertEqual(expected_text, actual_text)
