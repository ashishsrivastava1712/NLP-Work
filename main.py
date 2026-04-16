"""
Main Entry Point for Retrieval-Based Chatbot

Run this file to start the chatbot demo or interactive mode.

Usage:
    python main.py          (Demo mode - 5 test queries)
    python main.py -i       (Interactive mode - chat with bot)
    python main.py -web     (Web UI - streamlit interface)
"""

import sys
from src.chatbot import RetrievalChatbot


def run_demo():
    """Run chatbot with predefined test queries."""
    print("\n" + "🤖 "*15)
    print("RETRIEVAL-BASED CHATBOT DEMO")
    print("🤖 "*15 + "\n")

    # Initialize chatbot
    chatbot = RetrievalChatbot()

    # Test queries
    test_queries = [
        "What is machine learning?",
        "Tell me about Python",
        "How do I learn programming?",
        "What is the weather today?",  # Unknown query
        "Explain tokenization and NLP",
    ]

    print("Testing with sample queries:\n")

    for i, query in enumerate(test_queries, 1):
        print(f"\n[Test {i}/5]")
        result = chatbot.chat(query)
        chatbot.print_response(result)


def run_interactive():
    """Run interactive chatbot loop."""
    print("\n" + "🤖 "*15)
    print("INTERACTIVE RETRIEVAL-BASED CHATBOT")
    print("Type 'quit' or 'exit' to end conversation")
    print("🤖 "*15 + "\n")

    # Initialize chatbot
    chatbot = RetrievalChatbot()

    conversation_count = 0

    while True:
        try:
            user_input = input("\n👤 You: ").strip()

            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\n🤖 Bot: Goodbye! Have a great day!")
                break

            if not user_input:
                print("🤖 Bot: Please enter a question.")
                continue

            conversation_count += 1
            result = chatbot.chat(user_input)
            print(f"\n🤖 Bot: {result['answer']}")
            print(f"📊 Similarity: {result['similarity_score']:.2%}")
            if result['matched_question']:
                print(f"🎯 Matched: {result['matched_question']}")

        except KeyboardInterrupt:
            print("\n\n🤖 Bot: Session interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            continue


def show_help():
    """Show help message."""
    print("""
📖 RETRIEVAL-BASED CHATBOT
═════════════════════════════════════════════════════════════

USAGE:
    python main.py          (Demo mode - Run 5 test queries)
    python main.py -i       (Interactive mode - Chat with bot)
    python main.py -web     (Web UI - Open streamlit interface)
    python main.py -h       (Show this help)

MODES:
    Demo:           Quick demonstration with predefined questions
    Interactive:    Chat with the bot in real-time
    Web:            Beautiful web interface (require streamlit)

FEATURES:
    ✓ Tokenization & Preprocessing
    ✓ TF-IDF Vectorization
    ✓ Cosine Similarity Matching
    ✓ Similarity Score Display
    ✓ Fallback for Unknown Queries
    ✓ 20 Q&A Pairs Dataset

EXAMPLES:
    $ python main.py
    $ python main.py -i
    $ python main.py -web

═════════════════════════════════════════════════════════════
    """)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()

        if mode in ['-h', '--help', 'help']:
            show_help()
        elif mode in ['-i', '--interactive', 'interactive']:
            run_interactive()
        elif mode in ['-web', '--web', 'web']:
            print("\n✨ Starting Web Interface...")
            print("Run: streamlit run ui/streamlit_chatbot.py\n")
            import subprocess
            subprocess.run([
                "streamlit",
                "run",
                "ui/streamlit_chatbot.py"
            ])
        else:
            print(f"Unknown option: {mode}")
            show_help()
    else:
        run_demo()
