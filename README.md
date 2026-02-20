# 🔎 Search Algorithms & Cosine Similarity

## 👩‍💻 Author
**Pooja Durgani**  
Repository: abcd-agentic-training-vnr-poojadurgani  

---

## 📌 Project Overview

This project implements multiple classical search algorithms along with a Cosine Similarity based text search system in Python.

It demonstrates:
- Fundamental searching techniques
- Algorithm time complexity comparison
- Basic vector space model for document similarity

---

## 🚀 Algorithms Implemented

### 1️⃣ Linear Search
- Sequential search
- Time Complexity: O(n)

### 2️⃣ Binary Search
- Divide and conquer approach
- Works on sorted arrays
- Time Complexity: O(log n)

### 3️⃣ Jump Search
- Block-based search using √n steps
- Time Complexity: O(√n)

### 4️⃣ Interpolation Search
- Uses interpolation formula
- Best for uniformly distributed sorted arrays
- Average Time Complexity: O(log log n)

### ⭐ 5️⃣ Cosine Similarity Search
- Converts documents into term-frequency vectors
- Uses cosine similarity formula:

Cosine Similarity = (A · B) / (|A||B|)

- Returns most similar document for a given query
- Used in NLP and search engines

---

## 🛠 Technologies Used
- Python 3
- math module
- collections.defaultdict

---

## ▶️ How to Run

```bash
python search_algorithms.py