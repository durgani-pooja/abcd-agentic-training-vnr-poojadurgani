

**Time Complexity:**
- `get_vocab(corpus)` → O(n), n = total characters  
- `get_pairs(vocab)` → O(m * k), m = number of words, k = avg word length  
- `merge_vocab(pair, vocab)` → O(m * k)  
- Total for r merges → O(r * m * k)  

**Space Complexity:** O(m * k) — stores intermediate vocabularies  

> BPE efficiently handles rare words and reduces vocabulary size for NLP models.

---

## 🛠 Technologies Used
- Python 3  
- `collections.defaultdict`  
- `re` module for regex-based tokenization  

---

## ▶️ How to Run
```bash
python tokenization.py