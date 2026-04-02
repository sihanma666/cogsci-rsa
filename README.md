"# cogsci-rsa" 

**Computational Cognitive Science (Spring 2026)**  
**Team:** Sihan Ma, Daniel Enriquez, Ayush Sarkar  
**Advisor:** Prof. Mark K. Ho

---

## The Question

Do vision models trained on different objectives learn concepts that match how humans organize them? And more specifically — do they pick up on **taxonomic structure** (like animacy, category membership, hierarchies)?

We're asking this because just comparing overall RSA scores is kinda boring. Prof. Ho was right to push us toward: what *aspects* of human conceptual space do models actually recover? Taxonomic structure is a solid target because it's grounded in actual cognitive science literature.

---

## Data: THINGS

We're using [THINGS](https://things-initiative.org) (Hebart et al., 2019) — 1,854 object concepts with human similarity judgments from a triplet paradigm.

For us:
- **Human embedding:** 66-dimensional representation derived from human judgments
- **Concept list:** 1,854 object names (in matching order)
- **Human RDM:** Pairwise distances computed from the 66-d embedding (our reference for RSA)

---

## Models

We're comparing three to cover different training regimes:

- **ResNet-50 (ImageNet)** — Supervised learning (the baseline). Trained with explicit class labels.
- **DINO (ViT-S/8)** — Self-supervised (no labels). Just predicts what other augmented versions of the image look like.
- **CLIP (ViT-B/32)** — Multimodal. Trained on image-text pairs. Language-grounded.

The question: does one of these recover human conceptual structure better than the others? And if so, why?

---

## The Pipeline

**Step 1: Get embeddings for each model**
- For each model, feed it the ~1,854 THINGS images (one embedding per concept, averaged across images of the same thing)

**Step 2: Compute RDMs**
- For each model embedding space, compute pairwise distances (cosine)
- This gives us a **model RDM** — how different each model thinks two concepts are
- We already have the **human RDM** from the THINGS embedding

**Step 3: Correlate**
- How well do the model RDMs match the human RDM? (Spearman ρ)
- Compare across the three models

**Result:** RSA correlation scores for each model. Higher = the model thinks about concepts more like humans do.

---

## Going Deeper: Taxonomic Structure

RSA gives us a single number. But what if one model scores higher just because of texture, and misses the hierarchical structure that humans use?

**What we're actually looking for:**
- **Animacy axis:** Is there a direction in the embedding space that separates living from non-living things? Does it match the human space?
- **Category clusters:** Do dogs cluster together? Chairs together? Like they do for humans?
- **Hierarchy:** Do higher-level groupings (all mammals vs. all furniture) appear in the geometry?

**How we test:**
- PCA/t-SNE visualization colored by category — visual check that clusters make sense
- Category-level RSA — within-category vs. between-category distances, compared to humans
- (Optional) Linear classifier for animacy — can we decode "alive or not" from the embeddings?

**Why this matters:** Prof. Ho's original feedback. Plus — Rogers & McClelland (2003) showed that simple neural networks trained on semantic relations develop taxonomic structure *automatically*. We're asking: do modern vision models rediscover this too?

---

## Who Does What

- **Sihan** — RSA pipeline (compute RDMs, correlations), taxonomic analysis, write-up lead
- **Daniel** — Extract ResNet-50 and DINO embeddings, save as `.npy` files
- **Ayush** — Extract CLIP embeddings, make the visualizations (PCA/t-SNE plots)

**Key:** Embeddings must be shape `(1854, D)` saved as `.npy` files in `embeddings/` folder. Concept order must match `concept_names.txt`.

---

## Timeline

| What | When | Who |
|---|---|---|
| Human RDM + THINGS preprocessing done | Apr 2 | Sihan |
| ResNet + DINO embeddings ready | Daniel |
| CLIP embeddings ready | Ayush |
| RSA correlations computed | Sihan |
| Taxonomic analysis done (PCA + clustering) | All |
| Draft written | All |
| Final version | End of semester | All |

---

## References

**The foundations:**
- Peterson, Abbott & Griffiths (2018) on DNNs vs. human representations (the anchor paper)
- Kriegeskorte, Mur & Bandettini (2008) on RSA methodology
- Hebart et al. (2019) on the THINGS dataset

**Taxonomic structure inspiration:**
- Rogers & McClelland (2003) — neural networks spontaneously develop taxonomies. This is our theoretical anchor.
- Chollet (2019) on the measure of intelligence — why structured representations matter (mentioned on course website as motivation)
- Saha et al. (2026) on barycentric alignment (if we get to it)