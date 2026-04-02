"# cogsci-rsa" 
# CogSci Project — Visual Representations & Human Conceptual Space
**Course:** Computational Cognitive Science (Spring 2026)  
**Team:** Sihan Ma, Daniel Enriquez, Ayush Sarkar  
**Advisor feedback:** Prof. Mark K. Ho  
**Last updated:** April 2, 2026

---

## Research Question

Do representations learned by modern vision models align with the conceptual similarity structure humans use to organize objects — and specifically, do they recover psychologically meaningful organizational features like **taxonomic structure**?

> **Why this matters:** RSA correlation alone (aggregate alignment score) is a weak test. The professor's feedback pushes us toward asking *which* aspects of human conceptual space are recovered. Taxonomic structure (animacy, size, category membership) is an empirically grounded target from the cognitive science literature.

---

## Dataset

**THINGS** (Hebart et al., 2019/2023)
- ~1,854 object concepts with natural images
- Human similarity judgments via triplet odd-one-out paradigm
- 66-dimensional embedding of human conceptual space (THINGS-data)
- Publicly available: https://things-initiative.org

**What we use from THINGS:**
- The 66-dim human embedding as our behavioral reference representation
- The similarity matrix derived from it (for RSA)
- Category labels for taxonomic analysis (animate/inanimate, basic-level categories)

---

## Models to Compare

| Model | Type | Learning objective | Why included |
|---|---|---|---|
| ResNet-50 (ImageNet) | Supervised | Cross-entropy classification | Baseline; trained with explicit labels |
| DINO (ViT-S/8) | Self-supervised | Self-distillation, no labels | Tests whether label-free objectives recover human structure |
| CLIP (ViT-B/32) | Multimodal | Image-text contrastive | Tests whether language grounding helps |

> **Open question for team:** Do we add a 4th model (e.g. SimCLR or MAE)? Keep scope realistic — 3 is defensible for a class project.

---

## Core Method: Representational Similarity Analysis (RSA)

### Steps
1. For each model, extract embeddings for the ~1,854 THINGS object images (one embedding per concept, e.g. average-pool across images of the same concept)
2. Compute pairwise cosine similarity matrix for each model → **model RDM** (representational dissimilarity matrix)
3. Compute pairwise distance matrix from the 66-dim THINGS human embedding → **human RDM**
4. Measure correlation between human RDM and each model RDM (Spearman's ρ)
5. Compare correlations across models

### What RSA tells us
RSA correlation = how much the *geometry* of model representations matches human similarity judgments. A high score means the model's internal distances between concepts track the distances humans perceive.

---

## Extended Analysis: Taxonomic Structure (Prof. Ho's feedback)

This is the part that elevates the project from "run RSA" to something cognitively meaningful.

### What to look for
- **Animate vs. inanimate axis:** Is there a principal axis in model embedding space that separates living from non-living things? Does it match the human embedding?
- **Basic-level category clustering:** Do objects cluster by category (dogs together, chairs together) in model space the way they do in human judgments?
- **Taxonomic hierarchy:** Does the model represent broader taxonomic groupings (mammals vs. birds vs. furniture) in a hierarchically organized way?

### Optional Extension: Barycentric Alignment (Ayush's task)

Saha et al. (2026) propose barycentric alignment as an instance-level comparison tool — goes beyond pairwise RSA by finding optimal transport mappings between representation spaces. More fine-grained and mathematically interesting.

**Deliverable:** Ayush implements a barycentric alignment comparison for ≥1 model vs. human, producing one figure + 1-paragraph writeup. If he doesn't deliver, core results are unaffected.

**Why keep it in scope:** Gives the write-up a methodological contribution angle and gives Ayush a concrete, bounded task that plays to his math interest.

### How to test this
- **Qualitative:** PCA/t-SNE of model embeddings colored by THINGS category labels — do clusters visually match taxonomic groupings?
- **Quantitative:** Category-level RSA — compute within-category vs. between-category similarity and compare to human data
- **Optional:** Probe for animacy dimension using a linear classifier trained on model embeddings

### Why this matters for the write-up
The professor cited neural network research on taxonomic representations (from the neural networks unit of the class). We should connect our results to that literature — e.g., does CLIP recover more human-like taxonomic structure than ResNet because of language grounding?

---

## Team Roles & Division of Labor

| Person | Responsibility |
|---|---|
| **Sihan Ma** | RSA pipeline (similarity matrices, correlation computation), taxonomic analysis, write-up lead |
| **Daniel Enriquez** | Model embeddings (ResNet + DINO extraction), infrastructure setup |
| **Ayush Sarkar** | CLIP embeddings, visualization (PCA/t-SNE), evaluation figures |

> **Coordination note:** All three need to agree on a shared embedding format before anyone writes extraction code. Propose: numpy array of shape `(N_concepts, D_model)` saved as `.npy`, with a matching `concept_names.txt`.

---

## Milestones & Internal Deadlines

| Milestone | Target date | Owner |
|---|---|---|
| Methods doc shared with group | Apr 4, 2026 | Sihan |
| Shared embedding format agreed | Apr 7, 2026 | All |
| THINGS data downloaded + human RDM computed | Apr 9, 2026 | Sihan |
| ResNet + DINO embeddings extracted | Apr 11, 2026 | Daniel |
| CLIP embeddings extracted | Apr 11, 2026 | Ayush |
| RSA correlations computed (core result) | Apr 14, 2026 | Sihan |
| Taxonomic analysis (PCA + category RSA) | Apr 18, 2026 | All |
| Draft write-up | Apr 23, 2026 | All |
| Final submission | End of semester | All |

---

## Literature

### Core / must-cite

- **Peterson, J. C., Abbott, J. T., & Griffiths, T. L. (2018).** Evaluating (and improving) the correspondence between deep neural networks and human representations. *Cognitive Science, 42*(8), 2648–2669. https://doi.org/10.1111/cogs.12670
  > **The anchor paper.** Compares DNNs to human psychological similarity judgments on natural images using a triplet paradigm. Finds DNNs are surprisingly close to humans but diverge in systematic ways — notably they **lack taxonomic representational information** (citing Mur et al., 2013). This directly motivates our taxonomic analysis question and gives us a baseline to beat/compare.

- **Kriegeskorte, N., Mur, M., & Bandettini, P. A. (2008).** Representational similarity analysis — connecting the branches of systems neuroscience. *Frontiers in Systems Neuroscience.* https://doi.org/10.3389/NEURO.06.004.2008
  > RSA methodology paper. Cite for the method itself.

### Dataset

- **Hebart, M. N., et al. (2019).** THINGS: A database of 1,854 object concepts and more than 26,000 naturalistic object images. *PLOS ONE.*
  > Core dataset paper.

- **Mukherjee, K., Huey, H., Stoinski, L. M., Qiuyi, Fan, J. E., & Bainbridge, W. A. (2026).** Drawings of THINGS: A large-scale drawing dataset of 1854 object concepts. *Behavior Research Methods.* https://doi.org/10.3758/S13428-025-02887-W
  > Same 1854 concepts as THINGS but with drawings. Potentially useful if we want to probe shape-based vs. texture-based representations across models.

### Relevant alignment / extension work

- **Saha, S., He, Z. W., & Khosla, M. (2026).** Barycentric alignment for instance-level comparison of neural representations. *arXiv.* https://doi.org/10.48550/ARXIV.2602.09225
  > The barycentric alignment paper. Proposes a finer-grained comparison tool beyond pairwise RSA distances — operates at the instance level. **Assigned to Ayush as optional extension task.** If he implements this, it gives us a 3rd comparison method alongside RSA and category-level analysis.

- **Du, Y., Dai, S., Song, Y., Thompson, P. M., Tang, H., & Zhan, L. (2026).** Deep models, shallow alignment: Uncovering the granularity mismatch in neural decoding. *arXiv (Cornell University).*
  > Directly relevant — argues that neural decoding (and by extension, alignment between model and human representations) suffers from granularity mismatches. Useful framing for why aggregate RSA may be insufficient and why we want taxonomic/structured analysis.

- **Otsuka, K., Nagano, Y., & Kamitani, Y. (2025).** Overcoming output dimension collapse: When sparsity enables zero-shot brain-to-image reconstruction at small data scales. *arXiv.*
  > Less central — about brain-to-image reconstruction with sparse embeddings. Potentially relevant if we look at intrinsic dimensionality, but probably background reading only for now.

### Broad motivation

- **Chollet, F. (2019).** On the measure of intelligence. *arXiv.* https://doi.org/10.48550/arXiv.1911.01547
  > ARC paper arguing that skill ≠ intelligence, and that generalization ability is what matters. Useful as broad framing for why it matters whether models capture *structured* human knowledge rather than just surface similarity. Use sparingly — it's a bit tangential unless you write a strong motivating paragraph connecting it.

---

## Course Context & Framing Requirements

**Critical constraint from the course page:** The project cannot be a purely ML/data science project. It must connect to the human mind and model internal mental processes — representations and processes, not just behavioral prediction.

**What this means for our write-up:**
- Don't frame it as "we compared three models on a benchmark." Frame it as: *what does the geometry of learned visual representations reveal about how the mind organizes conceptual knowledge?*
- Every result needs a cognitive science interpretation, not just an accuracy number
- The taxonomic structure analysis is the cognitive science contribution — lean into it

**Theoretical anchor — Rogers & McClelland (2003):** The course explicitly covers this model (Lecture 2 on neural networks). They showed that a simple neural network trained on semantic facts develops hierarchical taxonomic representations (animate/inanimate, then finer categories) through learning alone. Our project is essentially asking: do modern vision models trained on different objectives rediscover this same taxonomic structure? That framing connects us directly to course content and will resonate with Gureckis.

**On the Chollet ARC paper:** It's project suggestion #1 on the course website — not tangential at all. Use it in the intro to motivate why structured, human-like representations matter beyond benchmark performance.

**Compute resource:** The course JupyterHub at `psychua300-011-spring.rcnyu.org` is likely accessible to the whole class. Check if it has GPU. If it does, this is where to run embedding extraction. No personal machine setup required.

---

## Presentation / Website Plan

The course has a strong culture of interactive demos (Bayesian Number Game, MDP demo, IAC model, etc. are all built into the course site). A project website would fit naturally.

**Proposed interactive visualization:**
- Interactive t-SNE / PCA plot of each model's embedding space
- Hover over a point → see the object image and its category label
- Toggle coloring: by THINGS category vs. animacy vs. model (ResNet / DINO / CLIP)
- Optionally: show human RDM alongside model RDM as a heatmap

**Implementation:** Plotly + static HTML, or a simple React page. Sihan builds this after core analysis is complete. One afternoon of work once the embeddings and RSA results exist.

**Why this is worth doing:** For the final presentation it lets you *show* rather than tell what taxonomic structure looks like in each model's space. It's also a genuinely useful artifact that could go in a portfolio.

---

## Open Questions

- [ ] Do we need institutional access to full THINGS image set, or is the embedding sufficient?
- [ ] Which layer of ResNet/DINO do we extract embeddings from? (penultimate layer standard for RSA)
- [ ] How do we handle multiple images per concept when computing a single concept-level embedding?
- [ ] Is intrinsic dimensionality analysis still in scope, or do we drop it?

---

## Notes & Raw Ideas

*(Use this section as a scratchpad — dump anything here, organize later)*

- Prof. Ho specifically mentioned taxonomic representations from the neural networks unit — worth re-reading those slides before writing up results
- "Barycentric alignment" mentioned in original proposal email — probably drop this, it's not in the core scope