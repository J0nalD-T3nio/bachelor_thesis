import unittest
from logic.summarizer import Summarizer

class TestSummarizer(unittest.TestCase):
    def setUp(self):
        self.summarizer = Summarizer()

    def test_generate_summary(self):
        text = "This is a test. It has multiple sentences. We want to summarize it."
        summary = self.summarizer.generate_summary(text, num_sentences=2)
        self.assertIsNotNone(summary)
        self.assertTrue(len(summary) > 0)
        self.assertTrue(len(summary.split('.')) <= 2)

if __name__ == '__main__':
    unittest.main()
