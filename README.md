# 🤖 Retrieval-Based Chatbot

A complete NLP-based retrieval chatbot using TF-IDF and cosine similarity.

## 📁 Project Structure

```
retrieval-chatbot/
│
├── src/                          # Core source code
│   ├── __init__.py              # Package initialization
│   ├── chatbot.py               # Main chatbot class
│   ├── text_preprocessor.py     # Text preprocessing
│   └── qa_dataset.py            # Q&A dataset
│
├── ui/                           # User interfaces
│   └── streamlit_chatbot.py     # Web interface
│
├── notebooks/                    # Jupyter notebooks
│   └── (Can add tutorials here)
│
├── tests/                        # Testing scripts
│   └── test_chatbot.py          # Verification tests
│
├── docs/                         # Documentation
│   └── (Can add docs here)
│
├── main.py                       # Entry point (console app)
├── requirements.txt              # Dependencies
└── README.md                     # This file
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Chatbot

**Demo Mode (5 test queries):**
```bash
python main.py
```

**Interactive Mode (chat with bot):**
```bash
python main.py -i
```

**Web Interface (Streamlit):**
```bash
python main.py -web
```

Or directly:
```bash
streamlit run ui/streamlit_chatbot.py
```

### 3. Verify Installation

```bash
python tests/test_chatbot.py
```

## 📝 What Each File Does

### Core Files (src/)

#### `__init__.py`
- Package initialization file
- Exports main classes and dataset
- Allows importing: `from src import RetrievalChatbot, QA_DATASET`

#### `chatbot.py`
**Main chatbot logic**
- `RetrievalChatbot` class
- Uses TF-IDF vectorization
- Implements cosine similarity matching
- Returns answers with confidence scores

**Key Methods:**
- `__init__(qa_dataset)` - Initialize with Q&A pairs
- `find_best_match(query, threshold)` - Find similar Q&A pair
- `chat(query)` - Process query and return response
- `print_response(result)` - Format and display response

#### `text_preprocessor.py`
**Text preprocessing pipeline**
- `TextPreprocessor` class
- Handles tokenization
- Removes stopwords
- Cleans special characters

**Key Methods:**
- `preprocess(text)` - Complete preprocessing pipeline
- `clean_text(text)` - Remove special characters

#### `qa_dataset.py`
**Predefined Q&A knowledge base**
- `QA_DATASET` dictionary (20 Q&A pairs)
- Topics: Python, ML, NLP, AI, Data Science
- Helper functions:
  - `get_dataset()` - Get full dataset
  - `dataset_size()` - Get number of pairs
  - `get_all_questions()` - Get all questions
  - `get_all_answers()` - Get all answers

### Entry Point

#### `main.py`
**Standalone application launcher**
- Demo mode: `python main.py`
- Interactive: `python main.py -i`
- Web UI: `python main.py -web`
- Help: `python main.py -h`

**Functions:**
- `run_demo()` - Test with 5 predefined queries
- `run_interactive()` - Interactive chatbot loop
- `show_help()` - Display usage information

### Web Interface (ui/)

#### `streamlit_chatbot.py`
**Beautiful web UI**
- Chat history display
- Statistics dashboard
- Adjustable similarity threshold
- Example question buttons
- Q&A dataset viewer

**Run:**
```bash
streamlit run ui/streamlit_chatbot.py
```

### Testing (tests/)

#### `test_chatbot.py`
**Verification and testing script**
- Checks all dependencies
- Tests imports
- Verifies chatbot functionality
- Validates installation

**Run:**
```bash
python tests/test_chatbot.py
```

## 🧠 NLP Concepts Implemented

### 1. Tokenization
Breaking text into individual words/tokens
- **File:** `text_preprocessor.py`
- **Tool:** NLTK `word_tokenize()`
- **Example:** "What is Python?" → ["What", "is", "Python", "?"]

### 2. Stopword Removal
Filtering common non-informative words
- **File:** `text_preprocessor.py`
- **Tool:** NLTK `stopwords`
- **Example:** Remove "is" from "What is Python?"

### 3. Text Preprocessing
Complete cleaning pipeline
- **File:** `text_preprocessor.py`
- **Steps:**
  1. Lowercase
  2. Remove special chars
  3. Tokenize
  4. Remove stopwords

### 4. TF-IDF Vectorization
Convert text to numerical vectors
- **File:** `chatbot.py`
- **Tool:** sklearn `TfidfVectorizer`
- **Purpose:** Represent importance of each word

### 5. Cosine Similarity
Measure similarity between vectors
- **File:** `chatbot.py`
- **Tool:** sklearn `cosine_similarity`
- **Range:** 0 (different) to 1 (identical)

## 📊 How It Works

```
User Query
    ↓
Text Preprocessing (split, clean, tokenize)
    ↓
TF-IDF Vectorization (convert to numbers)
    ↓
Cosine Similarity (compare with 20 Q&A pairs)
    ↓
Find Best Match (highest similarity score)
    ↓
Check Threshold (≥ 0.3 by default)
    ↓
Return Answer + Confidence Score
```

## 💻 Usage Examples

### Python Code

```python
from src.chatbot import RetrievalChatbot

# Initialize
chatbot = RetrievalChatbot()

# Ask a question
result = chatbot.chat("What is machine learning?")
print(result['answer'])
print(f"Confidence: {result['similarity_score']:.2%}")
```

### Command Line

```bash
# Demo
python main.py

# Interactive
python main.py -i
# Then type: What is Python?
# Type: quit to exit

# Web UI
python main.py -web
```

## 🔧 Customization

### Add Q&A Pairs

Edit `src/qa_dataset.py`:
```python
QA_DATASET = {
    "What is Python?": "Python is...",
    "Your question?": "Your answer...",
}
```

### Adjust Threshold

In `main.py` or `chatbot.py`:
```python
answer, score, question = chatbot.find_best_match(query, similarity_threshold=0.5)
```

Lower = more lenient, Higher = stricter

## 🎓 For Your Assignment

**What to Submit:**
1. `src/` folder (all source code)
2. `main.py` (entry point)
3. `requirements.txt` (dependencies)
4. `README.md` (documentation)

**How to Present:**
1. Run: `python main.py`
2. Show similarity scores
3. Explain NLP concepts
4. Demo: `streamlit run ui/streamlit_chatbot.py`

## ✅ Requirements Met

- ✅ Tokenization
- ✅ Stopword removal
- ✅ Text preprocessing
- ✅ TF-IDF vectorization
- ✅ Cosine similarity
- ✅ 20 Q&A pairs
- ✅ Fallback handling
- ✅ Similarity scores
- ✅ Well-commented code
- ✅ Modular design
- ✅ CLI & Web interfaces (bonus)

## 📚 File Size Summary

| File | Type | Purpose |
|------|------|---------|
| main.py | Python | Entry point |
| src/chatbot.py | Python | Core logic |
| src/text_preprocessor.py | Python | Preprocessing |
| src/qa_dataset.py | Python | Q&A pairs |
| ui/streamlit_chatbot.py | Python | Web UI |
| tests/test_chatbot.py | Python | Verification |
| requirements.txt | Text | Dependencies |

## 🚨 Troubleshooting

**Module not found:**
```bash
pip install -r requirements.txt
```

**NLTK data missing:**
(Script auto-downloads, but if issues persist)
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

**Low similarity scores:**
- Lower threshold in code: `similarity_threshold=0.2`
- Or add more Q&A pairs

**Streamlit not found:**
```bash
pip install streamlit
```

## 📞 Support

- Check inline code comments
- Read concept explanations in this README
- Run tests: `python tests/test_chatbot.py`
- Try one of the example questions

---

**Status:** ✅ Ready to submit  
**Quality:** ⭐⭐⭐⭐⭐
