"""
Text Preprocessing Module

Handles all text cleaning and preprocessing steps for NLP pipeline.
"""

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK data if not present
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)


class TextPreprocessor:
    """
    Handles text preprocessing with the following steps:
    1. Lowercasing
    2. Removing special characters
    3. Tokenization
    4. Stopword removal
    """

    def __init__(self):
        """Initialize the preprocessor with English stopwords."""
        self.stop_words = set(stopwords.words('english'))

    def clean_text(self, text):
        """
        Remove special characters and extra whitespace.

        Args:
            text (str): Raw input text

        Returns:
            str: Cleaned text with only letters and spaces
        """
        # Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

        # Remove email addresses
        text = re.sub(r'\S+@\S+', '', text)

        # Remove special characters - keep only letters and spaces
        text = re.sub(r'[^a-zA-Z\s]', '', text)

        # Remove extra whitespace
        text = ' '.join(text.split())

        return text

    def preprocess(self, text):
        """
        Complete preprocessing pipeline.

        Args:
            text (str): Raw input text

        Returns:
            str: Fully preprocessed text (lowercase, cleaned, stopwords removed)
        """
        # Step 1: Lowercase
        text = text.lower()

        # Step 2: Clean special characters
        text = self.clean_text(text)

        # Step 3: Tokenization
        tokens = word_tokenize(text)

        # Step 4: Stopword removal
        tokens = [token for token in tokens if token not in self.stop_words]

        # Step 5: Join back into string
        return ' '.join(tokens)
