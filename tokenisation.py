# tokenization.py
# Assignment 6 - Tokenization Implementation
# Name: Pooja Durgani
# Repo: abcd-agentic-training-vnr-poojadurgani

from collections import defaultdict
import re

# ─────────────────────────────────────────
# ALGORITHM: Byte Pair Encoding (BPE)
# ─────────────────────────────────────────

def get_vocab(corpus):
    """Convert corpus into character-level vocabulary"""
    vocab = defaultdict(int)
    for word in corpus.split():
        vocab[' '.join(list(word)) + ' </w>'] += 1
    return vocab


def get_pairs(vocab):
    """Get frequency of all adjacent symbol pairs"""
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pairs[(symbols[i], symbols[i + 1])] += freq
    return pairs


def merge_vocab(pair, vocab):
    """Merge the most frequent pair"""
    new_vocab = {}
    bigram = ' '.join(pair)
    replacement = ''.join(pair)
    for word in vocab:
        new_word = word.replace(bigram, replacement)
        new_vocab[new_word] = vocab[word]
    return new_vocab


def bpe_tokenizer(corpus, num_merges=10):
    """Byte Pair Encoding Tokenizer"""
    print("=" * 55)
    print("   BPE TOKENIZATION - Pooja Durgani - Assignment 6")
    print("=" * 55)

    vocab = get_vocab(corpus)
    print(f"\n📌 Initial Vocabulary (character-level):")
    for word, freq in vocab.items():
        print(f"   '{word}'  →  freq: {freq}")

    for i in range(num_merges):
        pairs = get_pairs(vocab)
        if not pairs:
            break
        best_pair = max(pairs, key=pairs.get)
        vocab = merge_vocab(best_pair, vocab)
        print(f"\n🔁 Merge #{i+1}: {best_pair[0]} + {best_pair[1]} → {''.join(best_pair)}   (freq: {pairs[best_pair]})")

    print(f"\n✅ Final Vocabulary after {num_merges} merges:")
    for word in vocab:
        print(f"   {word}")
    return vocab


# ─────────────────────────────────────────
# BONUS: Other Tokenization Methods
# ─────────────────────────────────────────

def whitespace_tokenizer(text):
    """Basic whitespace tokenization"""
    return text.lower().split()


def word_tokenizer(text):
    """Regex-based word tokenizer"""
    return re.findall(r'\b\w+\b', text.lower())


def char_tokenizer(text):
    """Character-level tokenizer"""
    return list(text)


# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────
if __name__ == "__main__":

    sample_text = "low lower newest widest low lower"

    print("\n" + "="*55)
    print("  INPUT TEXT:", sample_text)
    print("="*55)

    print("\n📌 1. WHITESPACE TOKENIZER:")
    print("  ", whitespace_tokenizer(sample_text))

    print("\n📌 2. WORD TOKENIZER (regex):")
    tokens = word_tokenizer(sample_text)
    print("   Tokens :", tokens)
    print("   Unique  :", list(set(tokens)))

    print("\n📌 3. CHARACTER TOKENIZER:")
    print("  ", char_tokenizer(sample_text))

    print("\n📌 4. BPE TOKENIZER (Main Algorithm):")
    bpe_tokenizer(sample_text, num_merges=8)

    print("\n✅ Assignment 6 complete - Pooja Durgani!")