# import numpy as np
# import csv

# class WordAnalogy:
#     def __init__(self):
#         self.embeddings = {}

#     def extract_needed_words(self, train_file, test_file):
#         needed = set()
#         for file in [train_file, test_file]:
#             with open(file, 'r', encoding='utf-8') as f:
#                 for line in f:
#                     if not line.strip():
#                         continue
#                     parts = line.strip().split(',')
#                     if len(parts) >= 4:
#                         needed.update(w.lower() for w in parts[1:4])
#         return needed

#     def filter_glove(self, original_path, output_path, needed_words):
#         with open(original_path, 'r', encoding='utf-8') as fin, open(output_path, 'w', encoding='utf-8') as fout:
#             for line in fin:
#                 word = line.split()[0].lower()
#                 if word in needed_words:
#                     fout.write(line)

#     def load_glove_embeddings(self, filepath):
#         with open(filepath, 'r', encoding='utf-8') as f:
#             for line in f:
#                 parts = line.strip().split()
#                 word = parts[0].lower()
#                 vector = np.array(parts[1:], dtype=np.float32)
#                 self.embeddings[word] = vector

#     def cosine_similarity(self, v1, v2):
#         return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

#     def solve_analogy(self, A, B, C):
#         A, B, C = A.lower(), B.lower(), C.lower()
#         if A not in self.embeddings or B not in self.embeddings or C not in self.embeddings:
#             return 'UNKNOWN'
#         target_vector = self.embeddings[B] - self.embeddings[A] + self.embeddings[C]
#         best_word = None
#         best_score = -1
#         for word, vec in self.embeddings.items():
#             if word in [A, B, C]:
#                 continue
#             score = self.cosine_similarity(target_vector, vec)
#             if score > best_score:
#                 best_score = score
#                 best_word = word
#         return best_word if best_word else 'UNKNOWN'

#     def run(self, input):
#         # File paths
#         original_glove = 'wiki_giga_2024_100_MFT20_vectors_seed_2024_alpha_0.75_eta_0.05.050_combined.txt'
#         filtered_glove = 'glove.filtered.txt'
#         train_file = 'word-analogy-train.txt'
#         test_file = 'word-analogy-test.csv'

#         # Step 1: Extract needed words
#         needed_words = self.extract_needed_words(train_file, test_file)

#         # Step 2: Filter GloVe
#         self.filter_glove(original_glove, filtered_glove, needed_words)

#         # Step 3: Load filtered embeddings
#         self.load_glove_embeddings(filtered_glove)

#         # Step 4: Solve analogies and write output
#         with open('submission.csv', 'w', encoding='utf-8', newline='') as fout:
#             writer = csv.writer(fout)
#             writer.writerow(['category', 'word4'])

#             for parts in input:
#                 if parts[1] == 'word1':  # Skip header
#                     continue
#                 category, A, B, C = parts[0], parts[1], parts[2], parts[3]
#                 embedding_is_city_or_country = A[0].isupper()
#                 answer = self.solve_analogy(A, B, C)
#                 if embedding_is_city_or_country and answer != 'UNKNOWN':
#                     answer = answer[0].upper() + answer[1:]
#                 writer.writerow([category, answer])

# Load GloVe embeddings into a dictionary
# def load_embeddings(file_path):
#     embeddings = {}
#     with open(file_path, 'r', encoding='utf-8') as f:
#         for line in f:
#             values = line.split()
#             word = values[0]
#             vector = np.asarray(values[1:], dtype='float32')
#             embeddings[word] = vector
#     return embeddings

# glove_embeddings_path = 'wiki_giga_2024_100_MFT20_vectors_seed_2024_alpha_0.75_eta_0.05.050_combined.txt'  # Adjust the path to your downloaded GloVe file
# glove_embeddings = load_embeddings(glove_embeddings_path)
