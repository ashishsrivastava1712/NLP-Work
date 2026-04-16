"""
Retrieval-Based Chatbot Package

A simple NLP chatbot using TF-IDF and cosine similarity.
"""

__version__ = "1.0.0"
__author__ = "Your Name"

from .text_preprocessor import TextPreprocessor
from .chatbot import RetrievalChatbot
from .qa_dataset import QA_DATASET

__all__ = [
    'TextPreprocessor',
    'RetrievalChatbot',
    'QA_DATASET',
]
