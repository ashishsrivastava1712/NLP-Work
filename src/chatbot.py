"""
Retrieval-Based Chatbot Module

Main chatbot implementation using TF-IDF and cosine similarity.
"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try:
    from .text_preprocessor import TextPreprocessor
    from .qa_dataset import QA_DATASET
except ImportError:
    from src.text_preprocessor import TextPreprocessor
    from src.qa_dataset import QA_DATASET


class RetrievalChatbot:
    """
    A retrieval-based chatbot that uses TF-IDF and cosine similarity
    to find the most relevant answer from a predefined dataset.

    Architecture:
    1. Text Preprocessing (tokenization, stopword removal)
    2. TF-IDF Vectorization (convert text to numerical vectors)
    3. Cosine Similarity (find most similar Q&A pair)
    4. Return Answer with Confidence Score
    """

    def __init__(self, qa_dataset=None):
        """
        Initialize chatbot with Q&A dataset.

        Args:
            qa_dataset (dict): Dictionary with questions as keys and answers as values.
                              If None, uses default QA_DATASET.
        """
        self.qa_dataset = qa_dataset or QA_DATASET
        self.preprocessor = TextPreprocessor()

        # Store original questions and answers
        self.questions = list(self.qa_dataset.keys())
        self.answers = list(self.qa_dataset.values())

        # Preprocess all questions
        self.preprocessed_questions = [
            self.preprocessor.preprocess(q) for q in self.questions
        ]

        # Initialize TF-IDF vectorizer and fit on all questions
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.preprocessed_questions)

        print(f"✓ Chatbot initialized with {len(self.questions)} Q&A pairs")

    def find_best_match(self, user_query, similarity_threshold=0.3):
        """
        Find the most relevant answer using cosine similarity.

        Args:
            user_query (str): User's input query
            similarity_threshold (float): Minimum similarity score to return an answer
                                        (0.3 = 30% match)

        Returns:
            tuple: (answer, similarity_score, original_question) or
                   (fallback_response, score, None) if below threshold
        """
        # Preprocess user query
        preprocessed_query = self.preprocessor.preprocess(user_query)

        # Convert query to TF-IDF vector
        query_tfidf = self.vectorizer.transform([preprocessed_query])

        # Calculate cosine similarity with all questions
        similarities = cosine_similarity(query_tfidf, self.tfidf_matrix)[0]

        # Find the index of most similar question
        most_similar_idx = np.argmax(similarities)
        similarity_score = similarities[most_similar_idx]

        # Check if similarity meets threshold
        if similarity_score >= similarity_threshold:
            best_answer = self.answers[most_similar_idx]
            best_question = self.questions[most_similar_idx]
            return best_answer, similarity_score, best_question
        else:
            # Return fallback response if no match meets threshold
            fallback = "I didn't understand that. Could you please rephrase your question?"
            return fallback, similarity_score, None

    def chat(self, user_query, show_details=True):
        """
        Process user query and return response with optional details.

        Args:
            user_query (str): User's message
            show_details (bool): Whether to include all details in response

        Returns:
            dict: Contains 'answer', 'similarity_score', and 'matched_question'
        """
        answer, similarity_score, matched_question = self.find_best_match(user_query)

        result = {
            'user_query': user_query,
            'answer': answer,
            'similarity_score': round(similarity_score, 4),
            'matched_question': matched_question
        }

        return result

    def print_response(self, result):
        """
        Print chatbot response in a formatted way.

        Args:
            result (dict): Result dictionary from chat() method
        """
        print("\n" + "="*70)
        print(f"You: {result['user_query']}")
        print("-"*70)
        print(f"Bot: {result['answer']}")
        print("-"*70)
        print(f"📊 Similarity Score: {result['similarity_score']:.2%}")
        if result['matched_question']:
            print(f"🎯 Matched Question: {result['matched_question']}")
        print("="*70)
