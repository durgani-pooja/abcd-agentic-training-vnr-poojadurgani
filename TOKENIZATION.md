# 📝 Text Tokenization & Byte Pair Encoding (BPE) in Python

## 👩‍💻 Author
**Pooja Durgani**  
B.Tech Student – Computer Science  
Repository: abcd-agentic-training-vnr-poojadurgani  

---

## 📌 Project Overview

This project demonstrates various **tokenization techniques** in Python, including a **Byte Pair Encoding (BPE)** tokenizer, widely used in modern NLP systems.  

Tokenization is the process of splitting text into smaller units (tokens), which is a critical first step in text preprocessing for tasks like:

- Text classification  
- Search engines  
- Chatbots  
- Language modeling  

---

## 🧠 Tokenization Techniques Implemented

### 1️⃣ Whitespace Tokenizer
- Splits text by spaces.  
- Example: `"low lower newest"` → `['low', 'lower', 'newest']`  
- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)  

### 2️⃣ Word Tokenizer (Regex-based)
- Uses `re.findall(r'\b\w+\b', text)` to extract words.  
- Handles punctuation and special characters efficiently.  
- **Time Complexity:** O(n)  
- **Space Complexity:** O(k) — k = number of tokens  

### 3️⃣ Character Tokenizer
- Splits text into individual characters.  
- Example: `"low"` → `['l', 'o', 'w']`  
- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)  

### 4️⃣ Byte Pair Encoding (BPE) Tokenizer ⭐
- Subword tokenization algorithm used in modern NLP (e.g., GPT, BERT).  

**Pipeline:**
1. Convert corpus into **character-level vocabulary**  
2. Count **frequency of adjacent symbol pairs**  
3. Merge the **most frequent pair**  
4. Repeat merges for a fixed number of iterations  
5. Generate **subword-level vocabulary**

**Example:**