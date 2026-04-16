"""
Test and Verification Script

Tests the chatbot functionality and dependencies.
"""

import sys
import subprocess

print("\n" + "="*70)
print("🤖 RETRIEVAL-BASED CHATBOT - VERIFICATION TEST")
print("="*70)

# Check Python version
print("\n📦 CHECKING DEPENDENCIES:\n")

checks = {
    "Python": None,
    "NumPy": "numpy",
    "NLTK": "nltk",
    "Scikit-learn": "sklearn",
}

all_good = True

for name, module in checks.items():
    if module is None:
        print(f"  ✅ {name:<20} {sys.version.split()[0]}")
    else:
        try:
            __import__(module)
            mod = sys.modules[module]
            version = getattr(mod, '__version__', 'unknown')
            print(f"  ✅ {name:<20} {version}")
        except ImportError:
            print(f"  ❌ {name:<20} NOT INSTALLED")
            all_good = False

# Test imports
print("\n⚙️ TESTING CORE IMPORTS:\n")

try:
    from src.text_preprocessor import TextPreprocessor
    print("  ✅ TextPreprocessor ........ OK")
except Exception as e:
    print(f"  ❌ TextPreprocessor ....... ERROR: {e}")
    all_good = False

try:
    from src.qa_dataset import QA_DATASET
    print(f"  ✅ QA_DATASET ............. OK ({len(QA_DATASET)} pairs)")
except Exception as e:
    print(f"  ❌ QA_DATASET ............. ERROR: {e}")
    all_good = False

try:
    from src.chatbot import RetrievalChatbot
    print("  ✅ RetrievalChatbot ....... OK")
except Exception as e:
    print(f"  ❌ RetrievalChatbot ....... ERROR: {e}")
    all_good = False

# Test chatbot functionality
print("\n🤖 TESTING CHATBOT:\n")

try:
    from src.chatbot import RetrievalChatbot

    chatbot = RetrievalChatbot()
    print("  ✅ Chatbot initialized .... OK")

    # Test a query
    result = chatbot.chat("What is machine learning?")
    print(f"  ✅ Chat query ............. OK")
    print(f"     Answer: {result['answer'][:60]}...")
    print(f"     Score: {result['similarity_score']:.2%}")

except Exception as e:
    print(f"  ❌ Chatbot test failed: {e}")
    all_good = False

print("\n" + "="*70)

if all_good:
    print("\n✅ ALL TESTS PASSED!")
    print("\n🎉 Chatbot is ready to use!")
    print("\nNext steps:")
    print("  1. python main.py       (Run demo)")
    print("  2. python main.py -i    (Interactive mode)")
    print("  3. streamlit run ui/streamlit_chatbot.py")
else:
    print("\n❌ SOME TESTS FAILED")
    print("\nFix issues:")
    print("  pip install -r requirements.txt")

print("\n" + "="*70 + "\n")
