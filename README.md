# GenAI Content Pipeline — README

## Overview
This project is a **hands-on GenAI playground** designed to understand how modern Generative AI systems work end-to-end.  
The focus is **learning and experimentation**, not guaranteed correctness of outputs.

The system is organized into **three major execution paths**, each representing a core capability commonly found in real-world GenAI platforms.

```
.
├── ingestion/
│ └── components
│ └── content
│ │ └── generators
│ └── entities
│ └── workflow
│ └── main.py
├── duplicate_content_detector/
│ └── main.py
├── content_consumer/
│ └── main.py
├── chroma_store/
│ └── ...
├── faiss_chunks.index 
└── README.md
```

---

## 1. Content Generator (Corpus Builder)

### Purpose
This is the **starting point of the system**.  
It generates the **initial data corpus** that is consumed by all downstream components.

** What it does **
- Creates synthetic or generated content
- Stores questions, phrases, or text samples
- Acts as a **data source** for duplicate detection and content generation
- The amount of data to be generated can be adjusted using the file inside `/ingestion/content/generator_builder.py`. By default it will create 2000 unique paragraphs of content for various topics.

** How to run **

```
cd ingestion
python main.py
```

** Output **

- Generated content stored in the data/corpus/ directory
- This corpus is reused across the entire project

CAUTION: ⚠️ You must run this step before running the other paths.

### 2. Duplicate Content Detector ###

#### Purpose ####

Identifies duplicate or near-duplicate content within the existing corpus.

** What it does **
  - Takes a phrase or sentence as input
  - Compares it against the stored corpus
  - Uses semantic similarity (embeddings + cosine similarity)

** Helps in: **
  - Detecting redundant data
  - Cleaning and deduplicating content
  - Improving corpus quality

** Typical use cases **
  - Finding duplicate questions
  - Removing repeated or highly similar content
  - Data hygiene before GenAI inference

** How to run **

```
cd similar_questions
python main.py 
```

** Output **

- List of similar or duplicate entries
- Similarity scores for analysis


### 3. Content Generator (GenAI Inference)
** Purpose ** 
Generates content for a given scenario using GenAI techniques.

** Scenario examples **
  - A question
  - A problem statement
  - A phrase or prompt

** What it does **
  - Takes an input scenario
  - Uses the generated corpus and embeddings
  - Produces an answer or explanation

CAUTION: ⚠️ The generated answer may not be 100% correct.

This is intentional.

The goal is to:
  - Understand how GenAI systems behave
  - Observe hallucinations and inaccuracies
  - Learn prompt-to-output dynamics
  - Study real-time GenAI behavior, not perfection

** How to run **
```
cd answer
python main.py 
```

#### Design Philosophy

  - Learning-first, not accuracy-first
  - Real-world GenAI behavior over ideal outputs
  - Simple, modular, and extensible architecture
  - Easy to experiment with embeddings, similarity, and generation

#### What This Project Is NOT
  - ❌ A production-ready GenAI system
  - ❌ A factually perfect answer engine
  - ❌ A fine-tuned domain expert model

What This Project IS
  - ✅ A GenAI experimentation framework
  - ✅ A learning tool for embeddings, similarity, and generation
  - ✅ A foundation for building larger RAG or AI systems

Next Possible Extensions
  - Add chunking and long-document support
  - Introduce reranking models
  - Store embeddings in a vector database
  - Add evaluation and feedback loops
  - Plug into LangChain / LangGrap
