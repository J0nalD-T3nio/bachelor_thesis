import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import FreqDist
from collections import defaultdict

class Summarizer:
    def __init__(self):
        self.ensure_nltk_resources()

    def ensure_nltk_resources(self):
        nltk.data.path.append('C:/Users/Ronan/nltk_data')
        resources = ['punkt', 'averaged_perceptron_tagger', 'maxent_ne_chunker', 'words']
        for resource in resources:
            try:
                nltk.data.find(f'tokenizers/{resource}')
            except LookupError:
                print(f"Downloading {resource}...")
                nltk.download(resource, download_dir='C:/Users/Ronan/nltk_data')

    def generate_summary(self, text, num_sentences=3):
        sentences = sent_tokenize(text)
        words = word_tokenize(text)
        freq_dist = FreqDist(word.lower() for word in words if word.isalpha())

        sentence_scores = defaultdict(int)
        for sentence in sentences:
            for word in word_tokenize(sentence):
                if word.lower() in freq_dist:
                    sentence_scores[sentence] += freq_dist[word.lower()]

        summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
        return ' '.join(summarized_sentences)
