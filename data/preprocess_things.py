"""
Preprocess THINGS data into standardized format for RSA pipeline.

input:
- words.csv: plain object names (1,854 lines)
- spose_embedding_66d_sorted.txt: human embedding (1,854 x 66)

output:
- concept_names.txt: one concept per line, matching embedding order
- human_embedding.npy: numpy array (1854, 66)
- human_rdm.npy: representational dissimilarity matrix (1854, 1854)
"""

import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist, squareform

print("THINGS Data Preprocessing")

#load from TSV metadata instead of words.csv
things_df = pd.read_csv('concepts-metadata_things.tsv', sep='\t') # Load concept names
concepts = things_df['uniqueID'].values  # extract as numpy array

np.savetxt('concept_names.txt', concepts, fmt='%s') # Save concept names as text file

human_embedding = np.loadtxt('spose_embedding_66d_sorted.txt') # Load human embedding
assert human_embedding.shape[0] == len(concepts), "embedding and concepts count mismatch :("
np.save('human_embedding.npy', human_embedding)

# Compute representational dissimilarity matrix (RDM)
distances = pdist(human_embedding, metric='cosine')
human_rdm = squareform(distances)
np.save('human_rdm.npy', human_rdm) # Save RDM

