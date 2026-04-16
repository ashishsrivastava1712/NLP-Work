"""
Streamlit Web UI for Retrieval-Based Chatbot

Beautiful web interface for the chatbot.

Run with:
    streamlit run ui/streamlit_chatbot.py
"""

import sys
import os

# Add src directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join(parent_dir, "src")

if src_dir not in sys.path:
    sys.path.insert(0, src_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import streamlit as st

# Import chatbot modules
from chatbot import RetrievalChatbot
from qa_dataset import QA_DATASET

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Retrieval-Based Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .chatbot-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .user-message {
        background-color: #e3f2fd;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
        border-left: 4px solid #667eea;
    }
    .bot-message {
        background-color: #f0f4c3;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
        border-left: 4px solid #764ba2;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# PAGE HEADER
# ============================================================================

st.markdown("""
    <div class="chatbot-header">
        <h1>🤖 Retrieval-Based Chatbot</h1>
        <p>Powered by TF-IDF and Cosine Similarity</p>
    </div>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.header("⚙️ Settings")

    # Similarity threshold
    similarity_threshold = st.slider(
        "Similarity Threshold",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.05,
        help="Lower = more lenient, Higher = stricter matching"
    )

    st.markdown("---")

    st.header("ℹ️ About")
    st.markdown("""
    ### How It Works:
    1. Text preprocessing (tokenization, stopwords)
    2. TF-IDF vectorization
    3. Cosine similarity matching
    4. Return best answer

    ### Features:
    - 20 Q&A pairs
    - Similarity scores
    - Fallback handling
    """)

# ============================================================================
# MAIN CONTENT
# ============================================================================

# Initialize chatbot in session state
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = RetrievalChatbot()
    st.session_state.chat_history = []

chatbot = st.session_state.chatbot

# Left column - Chat
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("💬 Chatbot")

    # Display chat history
    if st.session_state.chat_history:
        for user_msg, bot_response in st.session_state.chat_history:
            st.markdown(f"""
            <div class="user-message">
                <strong>👤 You:</strong><br/>
                {user_msg}
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="bot-message">
                <strong>🤖 Bot:</strong><br/>
                {bot_response['answer']}<br/>
                <small>📊 Match: {bot_response['similarity_score']:.2%}</small>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("👋 Start by asking a question about Python, AI, ML, or NLP!")

# Right column - Stats
with col2:
    st.subheader("📊 Stats")

    if st.session_state.chat_history:
        scores = [msg[1]['similarity_score'] for msg in st.session_state.chat_history]
        st.metric("Questions Asked", len(st.session_state.chat_history))
        st.metric("Avg Match", f"{sum(scores)/len(scores):.1%}")
        st.metric("Best Match", f"{max(scores):.1%}")
    else:
        st.metric("Questions Asked", 0)

# ============================================================================
# INPUT SECTION
# ============================================================================

st.markdown("---")

col1, col2 = st.columns([4, 1])

with col1:
    user_input = st.text_input(
        "Ask a question:",
        placeholder="e.g., What is machine learning?",
        label_visibility="collapsed"
    )

with col2:
    send_button = st.button("🚀 Send", use_container_width=True)

if send_button and user_input.strip():
    result = chatbot.chat(user_input.strip())
    result['similarity_threshold'] = similarity_threshold

    if result['similarity_score'] >= similarity_threshold:
        st.session_state.chat_history.append((user_input, result))
    else:
        st.session_state.chat_history.append((user_input, {
            **result,
            'answer': "I didn't understand that. Could you please rephrase?"
        }))

    st.rerun()

# ============================================================================
# EXAMPLE QUESTIONS
# ============================================================================

st.markdown("---")
st.subheader("💡 Example Questions")

example_questions = [
    "What is machine learning?",
    "Tell me about Python",
    "What is NLP?",
    "Explain tokenization",
    "What is TF-IDF?",
    "What is cosine similarity?",
]

cols = st.columns(2)
for idx, question in enumerate(example_questions):
    col = cols[idx % 2]
    if col.button(f"❓ {question}", key=f"ex_{idx}", use_container_width=True):
        result = chatbot.chat(question)
        st.session_state.chat_history.append((question, result))
        st.rerun()

# ============================================================================
# FOOTER OPTIONS
# ============================================================================

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🗑️ Clear History", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

with col2:
    if st.button("📋 View All Q&A", use_container_width=True):
        st.session_state.show_qa = not st.session_state.get('show_qa', False)
        st.rerun()

# Show Q&A dataset if requested
if st.session_state.get('show_qa', False):
    st.markdown("---")
    st.subheader("📚 All Q&A Pairs")

    for i, (q, a) in enumerate(QA_DATASET.items(), 1):
        with st.expander(f"{i}. {q}"):
            st.write(a)
