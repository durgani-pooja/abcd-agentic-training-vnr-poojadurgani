# ============================================================
# Assignment 7: Search Algorithms including Cosine Search
# Name: Pooja Durgani
# Repo: abcd-agentic-training-vnr-poojadurgani
# ============================================================

import math
from collections import defaultdict


# ─────────────────────────────────────────────
# 1. LINEAR SEARCH
# ─────────────────────────────────────────────
def linear_search(arr, target):
    """
    Searches element one by one from start to end.
    Time Complexity: O(n)
    """
    for i, val in enumerate(arr):
        if val == target:
            return i  # returns index if found
    return -1  # not found


# ─────────────────────────────────────────────
# 2. BINARY SEARCH (Array must be sorted)
# ─────────────────────────────────────────────
def binary_search(arr, target):
    """
    Divides the sorted array into halves to find the target.
    Time Complexity: O(log n)
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# ─────────────────────────────────────────────
# 3. JUMP SEARCH (Array must be sorted)
# ─────────────────────────────────────────────
def jump_search(arr, target):
    """
    Jumps ahead by fixed steps, then does linear search.
    Time Complexity: O(√n)
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1


# ─────────────────────────────────────────────
# 4. INTERPOLATION SEARCH (Sorted + Uniformly distributed)
# ─────────────────────────────────────────────
def interpolation_search(arr, target):
    """
    Uses a formula to estimate where the element might be.
    Time Complexity: O(log log n) average
    """
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if arr[low] == arr[high]:
            if arr[low] == target:
                return low
            return -1

        # Interpolation formula
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1


# ─────────────────────────────────────────────
# 5. COSINE SIMILARITY SEARCH  ⭐ (Main Algorithm)
# ─────────────────────────────────────────────

def get_tfidf_vector(document, vocab):
    """
    Converts a document (sentence) into a simple term-frequency vector
    based on a given vocabulary.
    """
    vector = []
    words = document.lower().split()
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1

    for word in vocab:
        vector.append(word_count[word])
    return vector


def dot_product(vec_a, vec_b):
    """Calculates dot product of two vectors."""
    return sum(a * b for a, b in zip(vec_a, vec_b))


def magnitude(vec):
    """Calculates magnitude (length) of a vector."""
    return math.sqrt(sum(x ** 2 for x in vec))


def cosine_similarity(vec_a, vec_b):
    """
    Cosine Similarity Formula:
    cosine_sim = (A · B) / (|A| * |B|)

    Returns value between 0 and 1:
      1 = identical direction (very similar)
      0 = completely different
    """
    dp = dot_product(vec_a, vec_b)
    mag_a = magnitude(vec_a)
    mag_b = magnitude(vec_b)

    if mag_a == 0 or mag_b == 0:
        return 0.0  # avoid division by zero

    return dp / (mag_a * mag_b)


def cosine_search(query, documents):
    """
    Finds the most similar document to the query using Cosine Similarity.

    Steps:
    1. Build vocabulary from all documents + query
    2. Convert each document and query into word vectors
    3. Calculate cosine similarity between query and each document
    4. Return the most similar document

    Args:
        query (str): The search query
        documents (list): List of documents to search in

    Returns:
        best_match (str): The most similar document
        scores (list): Similarity scores for all documents
    """
    # Step 1: Build vocabulary (unique words from all text)
    all_text = [query] + documents
    vocab = sorted(set(word.lower() for text in all_text for word in text.split()))

    # Step 2: Create vectors
    query_vector = get_tfidf_vector(query, vocab)
    doc_vectors = [get_tfidf_vector(doc, vocab) for doc in documents]

    # Step 3: Calculate cosine similarity
    scores = [cosine_similarity(query_vector, doc_vec) for doc_vec in doc_vectors]

    # Step 4: Find the best match
    best_index = scores.index(max(scores))
    best_match = documents[best_index]

    return best_match, scores


# ─────────────────────────────────────────────
# MAIN: Run All Search Algorithms
# ─────────────────────────────────────────────

if __name__ == "__main__":

    print("=" * 60)
    print("       SEARCH ALGORITHMS - POOJA DURGANI")
    print("=" * 60)

    # ── Linear Search ──
    print("\n📌 1. LINEAR SEARCH")
    data = [10, 25, 30, 45, 60, 75, 90]
    target = 45
    result = linear_search(data, target)
    print(f"   Array : {data}")
    print(f"   Target: {target}")
    print(f"   Found at index: {result}")

    # ── Binary Search ──
    print("\n📌 2. BINARY SEARCH")
    sorted_data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    target = 60
    result = binary_search(sorted_data, target)
    print(f"   Array : {sorted_data}")
    print(f"   Target: {target}")
    print(f"   Found at index: {result}")

    # ── Jump Search ──
    print("\n📌 3. JUMP SEARCH")
    target = 80
    result = jump_search(sorted_data, target)
    print(f"   Array : {sorted_data}")
    print(f"   Target: {target}")
    print(f"   Found at index: {result}")

    # ── Interpolation Search ──
    print("\n📌 4. INTERPOLATION SEARCH")
    target = 30
    result = interpolation_search(sorted_data, target)
    print(f"   Array : {sorted_data}")
    print(f"   Target: {target}")
    print(f"   Found at index: {result}")

    # ── Cosine Similarity Search ──
    print("\n📌 5. COSINE SIMILARITY SEARCH ⭐")

    documents = [
        "Python is a programming language",
        "Machine learning uses algorithms and data",
        "Deep learning is a subset of machine learning",
        "Python is widely used in data science and machine learning",
        "Football is a popular sport",
    ]

    query = "Python machine learning"

    print(f"\n   Query    : '{query}'")
    print(f"\n   Documents:")
    for i, doc in enumerate(documents):
        print(f"     [{i}] {doc}")

    best_match, scores = cosine_search(query, documents)

    print(f"\n   Similarity Scores:")
    for i, (doc, score) in enumerate(zip(documents, scores)):
        bar = "█" * int(score * 20)
        print(f"     [{i}] Score: {score:.4f}  {bar}  → {doc}")

    print(f"\n   ✅ Best Match: '{best_match}'")
    print("=" * 60)