"""
Q&A Dataset Module

Contains 20 predefined Q&A pairs for the chatbot knowledge base.
"""

QA_DATASET = {
    # ===== Python & Programming =====
    "What is Python?": 
        "Python is a high-level, interpreted programming language known for its simplicity and readability. "
        "It is widely used in web development, data science, and artificial intelligence.",

    "Python programming language":
        "Python is a versatile, easy-to-learn language that works great for beginners and experts. "
        "Its clean syntax makes it perfect for automation, web development, and scientific computing.",

    "How to learn Python?":
        "Start with basic Python syntax and concepts. Use online resources, write simple programs, practice regularly, "
        "and gradually work on more complex projects to build your programming skills.",

    "What is applications of Python?":
        "Python powers web applications (Django, Flask), data analysis (Pandas, NumPy), machine learning (TensorFlow, scikit-learn), "
        "automation scripts, scientific research, and even game development.",

    "How do I start learning programming?":
        "To start learning programming, choose a beginner-friendly language like Python, follow online tutorials "
        "and courses, practice coding regularly, solve problem sets, and build small projects to reinforce your learning.",

    "What is the purpose of an algorithm?":
        "An algorithm is a step-by-step procedure designed to solve a specific problem or perform a computation. "
        "Algorithms are the foundation of computer science and software development.",

    # ===== Machine Learning =====
    "What is machine learning?":
        "Machine learning is a subset of artificial intelligence that enables systems to learn and improve from "
        "experience without being explicitly programmed. It uses data patterns to make predictions.",

    "How does machine learning work?":
        "Machine learning works by training algorithms on historical data so they can learn patterns and relationships. "
        "Once trained, models can predict outcomes for new, unseen data with reasonable accuracy.",

    "Machine learning applications":
        "ML is used in recommendation systems (Netflix, Amazon), email spam filtering, image recognition, "
        "autonomous vehicles, medical diagnosis, financial forecasting, and natural language processing.",

    "What is supervised learning?":
        "Supervised learning is a type of machine learning where the algorithm learns from labeled training data "
        "(input-output pairs). The model tries to learn the relationship between inputs and correct outputs.",

    "What is unsupervised learning?":
        "Unsupervised learning is a type of machine learning where the algorithm learns patterns from unlabeled data "
        "without predefined output labels. Clustering and dimensionality reduction are common unsupervised tasks.",

    "What is deep learning?":
        "Deep learning is a subset of machine learning that uses artificial neural networks with multiple layers "
        "(hence 'deep') to learn representations of data. It powers modern AI applications.",

    # ===== Natural Language Processing =====
    "What is NLP?":
        "Natural Language Processing (NLP) is a branch of artificial intelligence that focuses on interactions "
        "between computers and human languages. It helps computers understand, interpret, and generate human language.",

    "Natural language processing basics":
        "NLP combines linguistics and computer science to process text and speech. It involves tokenization, "
        "part-of-speech tagging, named entity recognition, and sentiment analysis.",

    "What is tokenization?":
        "Tokenization is the process of breaking down text into smaller units called tokens, which are typically words "
        "or phrases. It is the first step in NLP text processing.",

    "Tokenization in NLP":
        "Tokenization splits sentences into words or subwords. This preprocessing step is essential for all downstream "
        "NLP tasks like sentiment analysis, named entity recognition, and text classification.",

    "Text preprocessing pipeline":
        "The text preprocessing pipeline typically includes: lowercasing, removing special characters, tokenization, "
        "stopword removal, lemmatization, and vectorization for machine learning model input.",

    "What is stopword removal?":
        "Stopword removal is the process of filtering out commonly used words (like 'the', 'is', 'and') that don't "
        "carry significant meaning in text analysis. This reduces noise and improves model efficiency.",

    "What is the difference between stemming and lemmatization?":
        "Stemming removes prefixes and suffixes to get the root form of words, often resulting in non-real words. "
        "Lemmatization uses vocabulary to convert words to their proper base form, producing valid dictionary words.",

    # ===== Information Retrieval & Similarity =====
    "What is TF-IDF?":
        "TF-IDF (Term Frequency-Inverse Document Frequency) is a numerical technique used to evaluate the importance "
        "of a word in a document relative to a collection of documents. It is commonly used in information retrieval.",

    "Term Frequency and Inverse Document Frequency":
        "TF measures how often a word appears in a document. IDF measures how unique or rare a word is across documents. "
        "TF-IDF combines both metrics to identify important, discriminative words.",

    "What is cosine similarity?":
        "Cosine similarity is a metric used to measure the similarity between two non-zero vectors of an inner product space. "
        "It calculates the cosine of the angle between vectors, where values range from -1 to 1.",

    "Vector similarity measurement":
        "Cosine similarity, Euclidean distance, and Manhattan distance are common metrics for comparing vectors. "
        "Cosine similarity works well for high-dimensional text data in NLP applications.",

    # ===== AI & Chatbots =====
    "What is artificial intelligence?":
        "Artificial Intelligence (AI) is the simulation of human intelligence processes by computer systems. "
        "AI includes learning, reasoning, problem-solving, and can perform tasks that typically require human intelligence.",

    "What is a chatbot?":
        "A chatbot is a software application designed to simulate conversation with users. "
        "Chatbots can be rule-based, retrieval-based, or generative AI-based.",

    "How chatbots work?":
        "Chatbots process user input, extract intent and entities, and generate responses. Retrieval-based chatbots "
        "select from predefined answers, while generative chatbots create new responses using neural networks.",

    # ===== Data Science =====
    "What is data science?":
        "Data science is an interdisciplinary field that combines statistics, mathematics, and programming to extract "
        "insights from data. Data scientists use various techniques to analyze and interpret complex datasets.",

    "Data science workflow":
        "The typical data science workflow includes: problem definition, data collection, data cleaning, exploratory analysis, "
        "feature engineering, model building, evaluation, and deployment.",
}


def get_dataset():
    """Get the Q&A dataset."""
    return QA_DATASET


def dataset_size():
    """Get the number of Q&A pairs in the dataset."""
    return len(QA_DATASET)


def get_all_questions():
    """Get all questions from the dataset."""
    return list(QA_DATASET.keys())


def get_all_answers():
    """Get all answers from the dataset."""
    return list(QA_DATASET.values())
