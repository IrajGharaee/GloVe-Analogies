# Word Analogy Solver using GloVe Embeddings

##  Overview
This project implements a **word analogy reasoning system** using **GloVe word embeddings**.  
It aims to solve verbal analogy questions such as:  
> *“Boy is to Man as Girl is to ___?”*  

I used a pretrained GloVE model to solve this problem.

## ⚙️ Key Features
- Utilizes **pre-trained GloVe embeddings** to capture semantic and syntactic relationships between words.  
- Computes vector relationships using the classic analogy formula:  
  > **B - A + C ≈ D**  
- Supports analogies across multiple categories, including:
  - **Countries and Capitals** (e.g., *Athens : Greece :: Beijing : China*)  
  - **Countries and Currencies** (e.g., *Denmark : krone :: Japan : yen*)  
  - **Verb Tenses** (e.g., *walk : walked :: dance : danced*)  
  - **Irregular Verbs** (e.g., *fly : flew :: feed : fed*)  

## 🧮 Methodology
1. **Load Pre-trained GloVe Model** (e.g., `wiki_giga_2024_100_MFT20_vectors_seed_2024_alpha_0.75_eta_0.05.050_combined.txt`)  
2. **Parse analogy dataset** (A, B, C, D format)  
3. **Compute predicted vector:**  
   ```python
   predicted_vector = embedding(B) - embedding(A) + embedding(C)
